import matplotlib.pyplot

def plotEnsemble(ensembleDict):
    plt = matplotlib.pyplot
    fig, ax = plt.subplots()
    n = len(ensembleDict["parties"])
    voteSharesD = [ensembleDict["voteShares"][i] for i in range(n) \
            if ensembleDict["parties"][i] == "D"]
    winProbsD = [ensembleDict["winProbs"][i] for i in range(n) \
            if ensembleDict["parties"][i] == "D"]
    voteSharesR = [100 - ensembleDict["voteShares"][i] for i in range(n) \
            if ensembleDict["parties"][i] == "R"]
    winProbsR = [100 - ensembleDict["winProbs"][i] for i in range(n) \
            if ensembleDict["parties"][i] == "R"]
    size = 50
    plt.scatter(voteSharesD, winProbsD, s=size)
    plt.scatter(voteSharesR, winProbsR, s=size)
    plt, ax = constructLabels(plt, ax)
    plt.show()
    plt.close(fig)

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
