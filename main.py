from plot import plotEnsemble
import csv

def constructEnsemble(parties, dataPath):
    ensemble = {}
    srcFile = "{}{}".format(dataPath, "ev.csv")
    csvFile = open(srcFile, "r")
    reader = csv.DictReader(csvFile)

    for stateData in reader:
        state = stateData["State"]
        ensemble[state] = {}
        ensemble[state]["ev"] = int(stateData["EV"])
        ensemble[state]["voteShares"] = {}
        ensemble[state]["winProbs"] = {}

        for party in parties:
            ensemble[state]["voteShares"][party] = 0
            ensemble[state]["winProbs"][party] = 0
        
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
            ensemble[state]["voteShares"][party] += voteShare

        if winProb >= 0:
            ensemble[state]["winProbs"][party] += winProb

    ensemble[state]["numVoteShares"] += int(voteSharesIsWhole)
    ensemble[state]["numWinProbs"] += int(winProbsIsWhole)    
    return ensemble

def processEnsemble(ensemble, parties):
    for state in ensemble:
        for party in parties:
            ensemble[state]["voteShares"][party] /= \
                    ensemble[state]["numVoteShares"]
            ensemble[state]["winProbs"][party] /= \
                    ensemble[state]["numWinProbs"]

    return ensemble

def summarize(ensemble, parties):
    summary = {}
    fields = ["evProb", "evDet", "voteShares", "winProbs"]

    for field in fields:
        summary[field] = {key: 0 for key in parties}

    for state in ensemble:
        if state != "US":
            stateEv = ensemble[state]["ev"]

            for party in parties:
                winProbParty = ensemble[state]["winProbs"][party]
                summary["evProb"][party] += (winProbParty / 100) * stateEv
            
            winProbs = ensemble[state]["winProbs"]
            stateFav = max(winProbs, key=winProbs.get)
            summary["evDet"][stateFav] += stateEv

    summary["voteShares"] = ensemble["US"]["voteShares"]
    summary["winProbs"] = ensemble["US"]["winProbs"]
    return summary

def toDict(ensemble):
    ensembleDict = {"states": [], "parties": [],\
            "ev": [], "voteShares": [], "winProbs": []}

    for state in ensemble:
        if state != "US":
            voteShares = ensemble[state]["voteShares"]
            winProbs = ensemble[state]["winProbs"]
            stateFav = max(winProbs, key=winProbs.get)
            ensembleDict["states"].append(state)
            ensembleDict["ev"].append(ensemble[state]["ev"])
            ensembleDict["parties"].append(stateFav)
            ensembleDict["voteShares"].append(voteShares[stateFav])
            ensembleDict["winProbs"].append(winProbs[stateFav])

    return ensembleDict

models = ["538", "dk", "pec"]
parties = ["D", "R", "L"]
dataPath = "data/"
ensemble = constructEnsemble(parties, dataPath)
ensemble = addModels(ensemble, models, parties, dataPath)
ensemble = processEnsemble(ensemble, parties)
summary = summarize(ensemble, parties)
ensembleDict = toDict(ensemble)
plotEnsemble(ensembleDict)
