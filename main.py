import csv

def constructEnsemble(models, parties):
    ensemble = {}

    for model in models:
        srcFile = "{}{}{}".format("data/", model, ".csv")
        csvFile = open(srcFile, "r")
        reader = csv.DictReader(csvFile)
		
        for stateData in reader:
            state = stateData["State"]
            
            if state not in ensemble:
                ensemble = addState(ensemble, state, parties)

            ensemble = addStateData(ensemble, parties, state, stateData)

    csvFile.close()
    return ensemble

def addState(ensemble, state, parties):
    ensemble[state] = {}

    for party in parties:
        ensemble[state]["{}{}".format("voteShare", party)] = 0                           
        ensemble[state]["{}{}".format("winProb", party)] = 0

    ensemble[state]["numVoteShares"] = 0
    ensemble[state]["numWinProbs"] = 0
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
ensemble = constructEnsemble(models, parties)
ensemble = processEnsemble(ensemble, parties)
