import math

#
# Calculating the absolute frequency of a set of discrete data.
#

def Fi(set:list, respectiveValues:bool = False):
    aux:list = []
    freq:list = []

    if respectiveValues == False:
        for x in set:
            if aux.count(x) == 0:
                aux.append(x)
        
        for x in aux:
            freq.append(set.count(x))
    else:
        for x in set:
            if aux.count(x) == 0:
                aux.append(x)
        
        for x in aux:
            freq.append([x, set.count(x)])
    
    return freq

#
# Calculation of the accumulated increasing frequency.
#

def Fac(fi:list):
    aux:list = []

    for x in range(len(fi)):
        if x == 0:
            aux.append(fi[x])
        else:
            aux.append(aux[x - 1] + fi[x])
    
    return aux

#
# Calculation of accumulated decreasing frequency.
#

def Fad(fi:list):
    aux:list = []

    for x in reversed(range(len(fi))):
        if x == len(fi) - 1:
            aux.append(fi[x])
        else:
            aux.insert(0, aux[0] + fi[x])

    return aux

#
# Calculation of relative frequency.
#

def Fir(fi:list):
    aux:list = []
    total:int = 0

    for x in fi:
        total += x
    
    for x in fi:
        aux.append(x / total)
    
    return aux

#
# Calculation of the relative increasing accumulated frequency.
#

def Facr(fir:list):
    aux:list = []

    for x in range(len(fir)):
        if x == 0:
            aux.append(fir[x])
        else:
            aux.append(aux[x - 1] + fir[x])
    
    return aux

#
# Calculation of the relative decreasing accumulated frequency.
#

def Fadr(fir:list):
    aux:list = []

    for x in reversed(range(len(fir))):
        if x == len(fir) - 1:
            aux.append(fir[x])
        else:
            aux.insert(0, aux[0] + fir[x])

    return aux

#
# Calculation of variable values ​​from a set of discrete data.
#

def VarValues(set:list):
    aux:list = []

    for x in set:
        if aux.count(x) == 0:
            aux.append(x)
    
    return aux

#
# Calculating the midpoint of classes for continuous sets.
#

def MidPoints(classes:list):
    aux:list = []

    for x in classes:
        aux.append((x[0] + x[1]) / 2)
    
    return aux

#
# Calculation of the total amplitude.
#

def FullRange(classes:list, simple:bool = False):
    if simple == False:
        return float(classes[len(classes) - 1][1]) - float(classes[0][0])
    else:
        classes.sort()
        return float(classes[len(classes) - 1]) - float(classes[0])

#
# Class amplitude calculation.
#

def ClassBreadth(fullRange:float, classes:list, simple:bool = False):    
    if simple == False:
        return fullRange / len(classes)
    else:
        if len(classes) <= 25:
            return fullRange / 5
        else:
            return fullRange / math.sqrt(len(classes))

#
# Function that organizes the data of the class vector.
#

def OrganizeSet(classes:list):
    aux:list = []
    for x in range(0, int(len(classes)), 2):
        aux.append([classes[x], classes[x + 1]])
    
    return aux

#
# Calculating the mean of a set of discrete data.
#

def Mean(set:list):
    aux:float = 0.0
    
    for x in set:
        aux += x
    
    return aux / len(set)

#
# Calculating the mode of a set of discrete data.
#

def Mode(set:list):
    mostRepeatingValue:list = []
    highestOccurrence:int = 0
    aux:list = []

    for x in set:
        if aux.count(x) == 0:
            aux.append(x)
    
    for x in range(len(aux)):
        if set.count(aux[x]) > highestOccurrence:
            highestOccurrence = set.count(aux[x])
            mostRepeatingValue.insert(0, aux[x])

    for x in range(len(aux)):
        if aux[x] != mostRepeatingValue:
            if set.count(aux[x]) == highestOccurrence and aux[x] != mostRepeatingValue[0]:
                mostRepeatingValue.append(aux[x])
    
    return mostRepeatingValue
            
#
# Calculating the median of a set of discrete data.
#

def Median(set:list):
    aux:float = 0.0

    if len(set) % 2 == 0:
        set.sort()
        aux = set[int(len(set) / 2)] + set[int((len(set) / 2) - 1)]
        aux /= 2
    else:
        set.sort()
        aux = set[math.ceil(len(set) / 2)]
    
    return aux

#
# Calculation of total samples.
#

def SampleQtt(setOrFi:list, simple: bool = False):
    aux:int = 0

    if simple == False:
        for x in set:
            aux += x
        
        return aux
    else:
        return len(set)
#
# Arithmetic mean calculation for continuous data sets.
#

def ContMean(midPoint:list, fi:list, sampleQtt:int):
    value1:float = 0
    
    for x in range(len(midPoint)):
        value1 += float(midPoint[x]) * float(fi[x])

    return round(value1 / sampleQtt, 2)

#
# Mode calculation for continuous data sets.
#
    
def ContMode(classes:list, fi:list, classBreadth:float):
    biggerIndex:list = []
    biggerFreq:float = 0.0
    modes:list = []

    for x in range(len(fi)):
        if float(fi[x]) > biggerFreq:
            biggerIndex.clear()
            biggerIndex.append(x)
            biggerFreq = fi[x]
    
    for x in range(len(fi)):
        if float(fi[x]) == biggerFreq and biggerIndex[0] != x:
            biggerIndex.append(x)
    
    for x in biggerIndex:
        if x == 0:
            aux:float = fi[x] - 0
            aux /= fi[x] - 0 + fi[x] - fi[x + 1]
            aux *= classBreadth
            aux += classes[x][0]
        else:
            aux:float = fi[x] - fi[x - 1]
            aux /= fi[x] - fi[x - 1] + fi[x] - fi[x + 1]
            aux *= classBreadth
            aux += classes[x][0]

        modes.append(round(aux, 2))
    
    return modes

#
# Calculating the median for continuous data sets.
#

def ContMedian(classes:list, fi:list, fac:list, classBreadth:float):
    aux:int = fac[len(fac) - 1]
    medianIndex:int  = 0
    median:float = 0.0
    
    if aux % 2 != 0:
        aux /= 2

        for x in fac:
            if aux > x:
                medianIndex += 1

        median = aux - fac[medianIndex - 1]
        median /= fi[medianIndex]
        median *= classBreadth
        median += classes[medianIndex][0]

        return round(median, 2)
    else:
        aux /= 2

        for x in fac:
            if aux > x and aux + 1 > x:
                medianIndex += 1

        median = aux - fac[medianIndex - 1]
        median /= fi[medianIndex]
        median *= classBreadth
        median += classes[medianIndex][0]

        return round(median, 2)

#
# Calculation of variance.
#

def SPTwo(midPoint:list, fi:list, mean:float, sampleQtt:int, simple:bool = False):
    value1:float = 0

    if simple == False:
        for x in range(len(midPoint)):
            value1 += pow(float(midPoint[x]) - mean, 2) * float(fi[x])

        return round(value1 / (sampleQtt - 1), 2)
    else:
        for x in range(len(midPoint)):
            value1 += pow(float(midPoint[x]) - mean, 2)

        return round(value1 / (sampleQtt - 1), 2)

#
# Calculation of standard deviation.
#

def SD(varianceResult:float):
    return round(math.sqrt(varianceResult), 2)

#
# Calculation of the coefficient of variation.
#

def CV(stanDevResult:float, mean:float):
    return round((stanDevResult / mean) * 100, 1)

#
# General calculation of a continuous dataset.
#

def GenCalcContinuousSets(set:list, fi:list, printData:bool = False):
    classes:list = OrganizeSet(set)
    fac = Fac(fi)
    fad = Fad(fi)
    fir = Fir(fi)
    facr = Facr(fir)
    fadr = Fadr(fir)
    midPoints = MidPoints(classes)
    fullRange = FullRange(classes)
    classBreadth = ClassBreadth(fullRange, classes)
    sampleQtt = SampleQtt(fi)
    contMean = ContMean(midPoints, fi, sampleQtt)
    contMode = ContMode(classes, fi, classBreadth)
    contMedian = ContMedian(classes, fi, fac, classBreadth)
    variance = SPTwo(midPoints, fi, contMean, sampleQtt)
    standardDeviation = SD(variance)
    coefficientVariation = CV(standardDeviation, contMean)
    resultVector:list = []

    resultVector.append(classes)
    resultVector.append(fi)
    resultVector.append(fir)
    resultVector.append(fac)
    resultVector.append(fad)
    resultVector.append(facr)
    resultVector.append(fadr)
    resultVector.append(midPoints)
    resultVector.append(fullRange)
    resultVector.append(classBreadth)
    resultVector.append(sampleQtt)
    resultVector.append(contMean)
    resultVector.append(contMode)
    resultVector.append(contMedian)
    resultVector.append(variance)
    resultVector.append(standardDeviation)
    resultVector.append(coefficientVariation)

    if printData == True:
        print("Classes: " + str(classes))
        print("Fi: " + str(fi))
        print("Fir: " + str(fir))
        print("Fac: " + str(fac))
        print("Fad: " + str(fad))
        print("Facr: " + str(facr))
        print("Fadr: " + str(fadr))
        print("Mid points: " + str(midPoints))
        print("Full range: " + str(fullRange))
        print("Class breadth: " + str(classBreadth))
        print("Total samples: " + str(sampleQtt))
        print("Mean: " + str(contMean))
        print("Mode: " + str(contMode))
        print("Median: " + str(contMedian))
        print("Variance: " + str(variance))
        print("Standart deviation: " + str(standardDeviation))
        print("Coefficient variation: " + str(coefficientVariation))

        return resultVector
    else:
        return resultVector

#
# General calculation of a discrete dataset.
#

def GenCalcDiscreteSets(set:list, printData:bool = False):
    fi = Fi(set)
    fir = Fir(fi)
    fac = Fac(fi)
    fad = Fad(fi)
    facr = Facr(fir)
    fadr = Fadr(fir)
    varValues = VarValues(set)
    fullRange = FullRange(set, True)
    classBreadth = ClassBreadth(fullRange, set, True)
    sampleQtt = SampleQtt(fi)
    mean = Mean(set)
    mode = Mode(set)
    median = Median(set)
    variance = SPTwo(varValues, fi, mean, sampleQtt, True)
    standardDeviation = SD(variance)
    coefficientVariation = CV(standardDeviation, mean)
    resultVector:list = []

    resultVector.append(set)
    resultVector.append(fi)
    resultVector.append(fir)
    resultVector.append(fac)
    resultVector.append(fad)
    resultVector.append(facr)
    resultVector.append(fadr)
    resultVector.append(varValues)
    resultVector.append(fullRange)
    resultVector.append(classBreadth)
    resultVector.append(sampleQtt)
    resultVector.append(mean)
    resultVector.append(mode)
    resultVector.append(median)
    resultVector.append(variance)
    resultVector.append(standardDeviation)
    resultVector.append(coefficientVariation)

    if printData == True:
        print("Set: " + str(set))
        print("Fi: " + str(fi))
        print("Fir: " + str(fir))
        print("Fac: " + str(fac))
        print("Fad: " + str(fad))
        print("Facr: " + str(facr))
        print("Fadr: " + str(fadr))
        print("Mid points: " + str(varValues))
        print("Full range: " + str(fullRange))
        print("Class breadth: " + str(classBreadth))
        print("Total samples: " + str(sampleQtt))
        print("Mean: " + str(mean))
        print("Mode: " + str(mode))
        print("Median: " + str(median))
        print("Variance: " + str(variance))
        print("Standart deviation: " + str(standardDeviation))
        print("Coefficient variation: " + str(coefficientVariation))

        return resultVector
    else:
        return resultVector