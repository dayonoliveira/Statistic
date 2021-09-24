import math

#
# Calculating the absolute frequency of a dataset.
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
# Calculation of the midpoints of a dataset.
#

def MidPoint(set:list):
    aux:list = []

    for x in set:
            if aux.count(x) == 0:
                aux.append(x)
    
    return aux

#
# Calculating the midpoint of classes for large sets.
#

def GranMidPoint(classes:list):
    aux:list = []

    for x in classes:
        aux.append((x[0] + x[1]) / 2)
    
    return aux

#
# Calculation of the total amplitude.
#

def FullRange(classes:list):
    return float(classes[len(classes) - 1][1]) - float(classes[0][0])

#
# Class amplitude calculation.
#

def ClassBreadth(fullRange:float, classes:list):
    return fullRange / len(classes)

#
# Function that organizes the data of the class vector.
#

def OrganizeClass(classes:list):
    aux:list = []
    for x in range(0, int(len(classes)), 2):
        aux.append([classes[x], classes[x + 1]])
    
    return aux

#
# Calculating the average of a dataset.
#

def Mean(set:list):
    aux:float
    
    for x in set:
        aux += x
    
    return aux / len(set)

#
# Calculating the mode of a dataset.
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
            mostRepeatingValue[0] = aux[x]

    for x in range(len(aux)):
        if aux[x] != mostRepeatingValue:
            if set.count(aux[x]) == highestOccurrence:
                mostRepeatingValue.append(aux[x])
    
    return mostRepeatingValue
            
#
# Calculating the median of a dataset.
#

def Median(set:list):
    aux:float = 0.0

    if len(set) % 2 == 0:
        set.sort()
        aux = set[len(set)] - set[len(set) + 1]
        aux /= 2
    else:
        set.sort()
        aux = set[math.ceil(len(set) / 2)]
    
    return aux

#
# Calculation of total samples.
#

def SampleQtt(fi:list):
    aux:int = 0

    for x in fi:
        aux += x
    
    return aux
#
# Arithmetic mean calculation for large data sets.
#

def GranMean(midPoint:list, fi:list, sampleQtt:int):
    value1:float = 0
    
    for x in range(len(midPoint)):
        value1 += float(midPoint[x]) * float(fi[x])

    return round(value1 / sampleQtt, 2)

#
# Mode calculation for large data sets.
#
    
def GranMode(classes:list, fi:list, classBreadth:float):
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
# Calculating the median for large data sets.
#

def GranMedian(classes:list, fi:list, fac:list, classBreadth:float):
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

def Variance(midPoint:list, fi:list, mean:float, sampleQtt:int):
    value1:float = 0

    for x in range(len(midPoint)):
        value1 += pow(float(midPoint[x]) - mean, 2) * float(fi[x])

    return round(value1 / (sampleQtt - 1), 2)

#
# Calculation of standard deviation.
#

def StandartDeviation(varianceResult:float):
    return round(math.sqrt(varianceResult), 2)

#
# Calculation of the coefficient of variation.
#

def CoefficientVariation(stanDevDResult:float, mean:float):
    return round((stanDevDResult / mean) * 100, 1)

#
# General calculation of a large dataset.
#

def GeralCalculationLargeSets(set:list, fi:list, printData:bool = True):
    classes:list = OrganizeClass(set)
    fac = Fac(fi)
    fad = Fad(fi)
    fir = Fir(fi)
    facr = Facr(fir)
    fadr = Fadr(fir)
    granMidPoint = GranMidPoint(classes)
    fullRange = FullRange(classes)
    classBreadth = ClassBreadth(fullRange, classes)
    sampleQtt = SampleQtt(fi)
    granMean = GranMean(granMidPoint, fi, sampleQtt)
    granMode = GranMode(classes, fi, classBreadth)
    granMedian = GranMedian(classes, fi, fac, classBreadth)
    variance = Variance(granMidPoint, fi, granMean, sampleQtt)
    standartDeviation = StandartDeviation(variance)
    coefficientVariation = CoefficientVariation(standartDeviation, granMean)

    if printData == True:
        print("Classes: " + str(classes))
        print("Fi: " + str(fi))
        print("Fir: " + str(fir))
        print("Fac: " + str(fac))
        print("Fad: " + str(fad))
        print("Facr: " + str(facr))
        print("Fadr: " + str(fadr))
        print("Mid points: " + str(granMidPoint))
        print("Full range: " + str(fullRange))
        print("Class breadth: " + str(classBreadth))
        print("Total samples: " + str(sampleQtt))
        print("Mean: " + str(granMean))
        print("Mode: " + str(granMode))
        print("Median: " + str(granMedian))
        print("Variance: " + str(variance))
        print("Standart deviation: " + str(standartDeviation))
        print("Coefficient variation: " + str(coefficientVariation))


GeralCalculationLargeSets([1.5,1.7,1.7,1.9,1.9,2.1,2.1,2.3,2.3,2.5], [7,16,35,24,18])
