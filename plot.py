import matplotlib.pyplot

def plotEnsemble(ensembleDict):
    plt = matplotlib.pyplot
    fig, ax = plt.subplots()
    xyData = constructXY(ensembleDict)
    size = 200
    colorD = [x / 255 for x in [30, 144, 255]]
    colorR = [x / 255 for x in [220, 20, 60]]
    scatterD = plt.scatter(xyData["voteSharesD"], xyData["winProbsD"], \
            s=xyData["sizeD"], c=colorD, alpha=0.5, label="Democrat Ahead")
    scatterR = plt.scatter(xyData["voteSharesR"], xyData["winProbsR"], \
            s=xyData["sizeR"], c=colorR, alpha=0.5, label="Republican Ahead")
    plt, ax = constructLabels(plt, ax)
    plt.legend(handles=[scatterD, scatterR], loc=4)
    plt.savefig("plot.png")
    plt.close(fig)

def constructXY(ensembleDict):
    n = len(ensembleDict["parties"])
    sizeMult = 20
    xyData = {}
    xyData["voteSharesD"] = [ensembleDict["voteShares"][i] \
            for i in range(n) if ensembleDict["parties"][i] == "D"]
    xyData["winProbsD"] = [ensembleDict["winProbs"][i] \
            for i in range(n) if ensembleDict["parties"][i] == "D"]
    xyData["sizeD"] = [sizeMult * ensembleDict["ev"][i] \
            for i in range(n) if ensembleDict["parties"][i] == "D"]
    xyData["voteSharesR"] = [100 - ensembleDict["voteShares"][i] \
            for i in range(n) if ensembleDict["parties"][i] == "R"]
    xyData["winProbsR"] = [100 - ensembleDict["winProbs"][i] \
            for i in range(n) if ensembleDict["parties"][i] == "R"]
    xyData["sizeR"] = [sizeMult * ensembleDict["ev"][i] \
            for i in range(n) if ensembleDict["parties"][i] == "R"]
    return xyData

def constructLabels(plt, ax):
    plt.xlim([15, 85])
    plt.ylim([-10, 110])
    xCore = [x for x in range(60, 100, 10)]
    xLabels = xCore[::-1] + [50] + xCore
    yCore = [y for y in range(60, 120, 20)]
    yLabels = [120] + yCore[::-1] + yCore
    ax.set_xticklabels(xLabels)
    ax.set_yticklabels(yLabels)
    return plt, ax
