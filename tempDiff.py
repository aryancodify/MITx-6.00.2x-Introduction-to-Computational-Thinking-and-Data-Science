import pylab

def load_temperatures():
    PATH_TO_FILE = 'temperatures.txt'
    lowList = []
    highList = []
    inFile = open(PATH_TO_FILE,'r')
    for line in inFile:
        fields = line.split(' ')
        if len(fields) == 3 and fields[0].isdigit():
            lowList.append(int(fields[2]))
            highList.append(int(fields[1]))

    return (highList,lowList)



def produce_plot(lowTemps, highTemps):
    """

    :type highTemps: list
    """
    diff = [highTemps[i]-lowTemps[i] for i in range(len(highTemps))]
    pylab.figure(1)
    pylab.plot(range(len(highTemps)),highTemps,'ro')
    pylab.plot(range(len(lowTemps)),lowTemps,'go')
    pylab.plot(range(len(diff)),diff,'bo')
    pylab.show()

tempDiff = load_temperatures()
produce_plot(tempDiff[1],tempDiff[0])