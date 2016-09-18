import csv

def constructEnsemble(parties, dataPath):
    ensemble = {}
    srcFile = "{}{}".format(dataPath, "ev.csv")
    csvFile = open(srcFile, "r")
    reader = csv.DictReader(csvFile)

    for stateData in reader:
        state = stateData["State"]
        ensemble[state] = {}
        ensemble[state]["ev"] = stateData["EV"]

        for party in parties:
            ensemble[state]["{}{}".format("voteShare", party)] = 0
            ensemble[state]["{}{}".format("winProb", party)] = 0
        
        ensemble[state]["numVoteShares"] = 0
        ensemble[state]["numWinProbs"] = 0

    return ensemble

def addModels(ensemble, models, parties, dataPath):

    for model in models:
        srcFile = "{}{}{}".format(dataPath, model, ".csv")
        csvFile = open(srcFile, "r")
        reader = csv.DictReader(csvFile)
		
        for stateData in reader:
            state = stateData["State"]
            ensemble = addStateData(ensemble, parties, state, stateData)

    csvFile.close()
    return ensemble

def addStateData(ensemble, parties, state, stateData):
    voteSharesIsWhole = True
    winProbsIsWhole = True

    for party in parties:
        voteShare = float(stateData["{}{}".format("VoteShare", party)])
        winProb = float(stateData["{}{}".format("WinProb", party)])
        voteSharesIsWhole = voteSharesIsWhole and voteShare >= 0
        winProbsIsWhole = winProbsIsWhole and winProb >= 0

        if voteShare >= 0:
            ensemble[state]["{}{}".format("voteShare", party)] += \
                    voteShare

        if winProb >= 0:
            ensemble[state]["{}{}".format("winProb", party)] += winProb

    ensemble[state]["numVoteShares"] += int(voteSharesIsWhole)
    ensemble[state]["numWinProbs"] += int(winProbsIsWhole)    
    return ensemble

def processEnsemble(ensemble, parties):
    for state in ensemble:
        for party in parties:
            ensemble[state]["{}{}".format("voteShare", party)] /= \
                    ensemble[state]["numVoteShares"]
            ensemble[state]["{}{}".format("winProb", party)] /= \
                    ensemble[state]["numWinProbs"]

    return ensemble

models = ["538", "dk", "pec"]
parties = ["D", "R", "L"]
dataPath = "data/"
ensemble = constructEnsemble(parties, dataPath)
ensemble = addModels(ensemble, models, parties, dataPath)
ensemble = processEnsemble(ensemble, parties)
