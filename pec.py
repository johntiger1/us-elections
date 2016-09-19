from bs4 import BeautifulSoup
import csv, re, requests

url = "http://election.princeton.edu/code/data/EV_stateprobs.csv"
response = requests.get(url)
reader = csv.reader(response.content.decode("utf-8").splitlines())
voteDiffI = 1
stateI = 4
winProbI = 5
fieldNames = ["State"]
parties = ["D", "R", "L"]

for party in parties:
    fieldNames.append("{}{}".format("VoteShare", party))
    fieldNames.append("{}{}".format("WinProb", party))

csvFile = open("data/pec.csv", "w", newline="")
writer = csv.DictWriter(csvFile, fieldnames=fieldNames)
writer.writeheader()

for stateData in reader:
    row = {}
    row["State"] = stateData[stateI]
    voteDiff = float(stateData[voteDiffI])
    row["VoteShareD"] = 50 + voteDiff / 2
    row["WinProbD"] = float(stateData[winProbI])
    row["VoteShareR"] = 100 - row["VoteShareD"]
    row["WinProbR"] = 100 - row["WinProbD"]
    row["VoteShareL"] = 0
    row["WinProbL"] = 0
    writer.writerow(row)

row = {}
row["State"] = "US"
url = "http://election.princeton.edu/state-by-state-probabilities/"
response = requests.get(url)
soup = BeautifulSoup(response.content, "html.parser")
dataSoup = soup.find("a", {"href": "/faq/#metamargin"})
forecastData = dataSoup.getText()
pattern = re.compile("Meta-margin: (Clinton|Trump) \+(\d+\.\d)%")
matches = pattern.search(forecastData)
voteShare = 50 + float(matches.groups()[1]) / 2

if matches.groups()[0] == "Clinton":
    row["VoteShareD"] = voteShare
else:
    row["VoteShareD"] = 100 - voteShare

row["VoteShareR"] = 100 - row["VoteShareD"]
row["VoteShareL"] = 0

dataSoup = soup.find("li", {"style": \
        "clear: both; padding-top: 0px; /*padding-left: 60px*/; " +\
        "color: black; float: none"})
forecastData = dataSoup.getText()
pattern = re.compile("(Clinton|Trump) Nov. win probability: " +\
        "random drift (\d\d)%, Bayesian \d\d%")
matches = pattern.search(forecastData)
winProb = float(matches.groups()[1])

if matches.groups()[0] == "Clinton":
    row["WinProbD"] = winProb
else:
    row["WinProbD"] = 100 - winProb

row["WinProbR"] = 100 - row["WinProbD"]
row["WinProbL"] = 0
writer.writerow(row)
csvFile.close()
