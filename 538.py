import csv, json, re, requests
from bs4 import BeautifulSoup

if __name__ == "__main__":
    url = "http://projects.fivethirtyeight.com/2016-election-forecast/"
    request = requests.get(url)
    soup = BeautifulSoup(request.content, "html.parser")
    summaryPos = 3
    dataSoup = soup.findAll("script")[summaryPos]
    pattern = re.compile("race.summary = (\[.+\])")
    matches = pattern.search(dataSoup.string)
    matchedStr = matches.groups()[0]
    dataJson = json.loads(matchedStr)
    parties = ["D", "R", "L"]
    fieldNames = ["State"]

    for party in parties:
        fieldNames.append("{}{}".format(party, "WinProb"))
        fieldNames.append("{}{}".format(party, "VoteShare"))

    csvFile = open("538.csv", "w", newline="")
    writer = csv.DictWriter(csvFile, fieldnames=fieldNames)
    writer.writeheader()

    for dataState in dataJson:
        state = dataState["state"]
        row = {"State": state}
    
        for party in parties:
            model = dataState["latest"][party]["models"]["plus"]
            voteShare = model["forecast"]
            winProb = model["winprob"]
            row["{}{}".format(party, "VoteShare")] = voteShare
            row["{}{}".format(party, "WinProb")] = winProb

        writer.writerow(row)

    csvFile.close()
