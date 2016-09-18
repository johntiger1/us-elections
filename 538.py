from bs4 import BeautifulSoup
import csv, json, re, requests

if __name__ == "__main__":
    url = "http://projects.fivethirtyeight.com/2016-election-forecast/"
    request = requests.get(url)
    soup = BeautifulSoup(request.content, "html.parser")
    posSummary = 3
    dataSoup = soup.findAll("script")[posSummary]
    pattern = re.compile("race.summary = (\[.+\])")
    matches = pattern.search(dataSoup.string)
    matchedStr = matches.groups()[0]
    dataJson = json.loads(matchedStr)
    parties = ["D", "R", "L"]
    fieldNames = ["State"]

    for party in parties:
        fieldNames.append("{}{}".format("WinProb", party))
        fieldNames.append("{}{}".format("VoteShare", party))

    csvFile = open("538.csv", "w", newline="")
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
