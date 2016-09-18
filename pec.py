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

csvFile = open("pec.csv", "w", newline="")
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

csvFile.close()
