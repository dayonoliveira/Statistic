import math

#
# Calculation of the accumulated increasing frequency.
#

def Fac(fi:list):
    pass

#
# Calculation of accumulated decreasing frequency.
#

def Fad(fi:list):
    pass

#
# Calculation of relative frequency.
#

def Fir(fi:list, total:int):
    pass

#
# Calculation of the relative increasing accumulated frequency.
#

def Facr(fir:list):
    pass

#
# Calculation of the relative decreasing accumulated frequency.
#

def Fadr(fir:list):
    pass

#
# Calculating the midpoint of classes for large sets.
#

def GranMidPoint(classes:list):
    pass

#
# Calculation of the total amplitude.
#

def FullRange(classes:list):
    pass

#
# Class amplitude calculation.
#

def ClassBreadth(fullRange:float, classes:list):
    pass

#
# Function that organizes the data of the class vector.
#

def OrganizeClass(classes:list):
    aux:list = []
    for x in range(0, int(len(classes)), 2):
        aux.append([classes[x], classes[x + 1]])
    
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
    
def GranMode(k:list, fi:list, classBreadth:float):
    classes:list = OrganizeClass(k)
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

def GranMedian(k:list, fi:list, fac:list, classBreadth:float):
    classes:list = OrganizeClass(k)
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

def GeralCalculationLargeSets():
    """ k = list(input("Limites das classes: ").split(","))
    fullRange:int
    classBreadth:float
    midPoint = list(input("Pontos médios: ").split(","))
    fi = list(input("Frequências simples: ").split(","))
    sampleQtt = int(input("Total de amostras: "))
    mean = float(GranMean(midPoint, fi, sampleQtt))
    aux:list = []

    for x in range(0, int(len(k)), 2):
        aux.append([k[x], k[x + 1]])
    
    k = aux

    fullRange = int(k[len(k) - 1][1]) - int(k[0][0])

    classBreadth = fullRange / len(k)

    variance = Variance(midPoint, fi, mean, sampleQtt)
    standart_deviation = StandartDeviation(variance)
    coefficient_variation = CoefficientVariation(standart_deviation, mean) """
