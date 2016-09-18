from bs4 import BeautifulSoup
import csv, re, requests, us

fieldNames = ["State"]
parties = ["D", "R", "L"]
dataDk = {}

for party in parties:
    fieldNames.append("{}{}".format("VoteShare", party))
    fieldNames.append("{}{}".format("WinProb", party))

csvFile = open("data/dk.csv", "w", newline="")
writer = csv.DictWriter(csvFile, fieldnames=fieldNames)
writer.writeheader()
url = "http://www.nytimes.com/interactive/2016/upshot/" + \
        "presidential-polls-forecast.html?action=" + \
        "click&contentCollection=upshot&region=rank&module=" + \
        "package&version=highlights&contentPlacement=2&pgtype=" + \
        "sectionfront&_r=0"
request = requests.get(url)
soup = BeautifulSoup(request.content, "html.parser")
dataSoup = soup.findAll("tr", {"class": "table-row"})
posDk = 3

for stateData in dataSoup:
    state = stateData.td.span.getText()
    forecastData = stateData.td.findNextSiblings("td")[posDk].getText()
    pattern = re.compile("(>?\d\d)%\s+(Dem|Rep)")
    matches = pattern.search(forecastData)

    if matches.groups()[0][0] == ">":
        winProb = 99.5
    else:
        winProb = float(matches.groups()[0])

    if matches.groups()[1] == "Dem":
        winProbD = winProb
        winProbR = 100 - winProb
    else:
        winProbR = winProb
        winProbD = 100 - winProb

    winProbL = 0
    dataDk[state] = {}
    stateObj = us.states.lookup(state.replace(".", ""))

    if stateObj is None:
        stateObj = us.states.lookup(state[:-1].replace(".", ""))
	
    dataDk[state]["State"] = stateObj.abbr
    dataDk[state]["VoteShareD"] = -1
    dataDk[state]["WinProbD"] = winProbD
    dataDk[state]["VoteShareR"] = -1
    dataDk[state]["WinProbR"] = winProbR
    dataDk[state]["VoteShareL"] = -1
    dataDk[state]["WinProbL"] = winProbL

url = "http://votamatic.org/2016-current-polling-averages/"
request = requests.get(url)
soup = BeautifulSoup(request.content, "html.parser")
dataSoup = soup.findAll("tr", \
		{"class": re.compile("row-[2-9]|(\d\d)")})

for stateData in dataSoup:
    stateStr = stateData.getText()
    pattern = re.compile("([a-zA-Z ]+)(\d\d.\d)%")
    matches = pattern.search(stateStr)
    state = matches.groups()[0]
    voteShareD = float(matches.groups()[1])
    voteShareR = 100 - voteShareD
    voteShareL = 0
    dataDk[state]["VoteShareD"] = voteShareD
    dataDk[state]["VoteShareR"] = voteShareR
    dataDk[state]["VoteShareL"] = voteShareL

for state in dataDk:
    writer.writerow(dataDk[state])

csvFile.close()
