from bs4 import BeautifulSoup
import csv, json, re, requests

url = "http://projects.fivethirtyeight.com/2016-election-forecast/"
response = requests.get(url)
soup = BeautifulSoup(response.content, "html.parser")
posSummary = 9
dataSoup = soup.findAll("script")[posSummary]
pattern = re.compile("race.summary = (\[.+\])")
matches = pattern.search(dataSoup.string)
matchedStr = matches.groups()[0]
dataJson = json.loads(matchedStr)
fieldNames = ["State"]
parties = ["D", "R", "L"]

for party in parties:
    fieldNames.append("{}{}".format("VoteShare", party))
    fieldNames.append("{}{}".format("WinProb", party))

csvFile = open("data/538.csv", "w", newline="")
writer = csv.DictWriter(csvFile, fieldnames=fieldNames)
writer.writeheader()

for stateSoup in dataJson:
    state = stateSoup["state"]
    row = {"State": state}

    for party in parties:
        model = stateSoup["latest"][party]["models"]["plus"]
        voteShare = model["forecast"]
        winProb = model["winprob"]
        row["{}{}".format("VoteShare", party)] = voteShare
        row["{}{}".format("WinProb", party)] = winProb

    writer.writerow(row)

csvFile.close()
