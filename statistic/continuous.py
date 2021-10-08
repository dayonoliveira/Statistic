import math


def fac(fi:list):
    aux:list = []

    for x in range(len(fi)):
        if x == 0:
            aux.append(fi[x])
        else:
            aux.append(aux[x - 1] + fi[x])
    
    return aux


def fad(fi:list):
    aux:list = []

    for x in reversed(range(len(fi))):
        if x == len(fi) - 1:
            aux.append(fi[x])
        else:
            aux.insert(0, aux[0] + fi[x])

    return aux


def fir(fi:list):
    aux:list = []
    total:int = 0

    for x in fi:
        total += x
    
    for x in fi:
        aux.append(x / total)
    
    return aux


def facr(fir:list):
    aux:list = []

    for x in range(len(fir)):
        if x == 0:
            aux.append(fir[x])
        else:
            aux.append(aux[x - 1] + fir[x])
    
    return aux


def fadr(fir:list):
    aux:list = []

    for x in reversed(range(len(fir))):
        if x == len(fir) - 1:
            aux.append(fir[x])
        else:
            aux.insert(0, aux[0] + fir[x])

    return aux


def mid_points(classes:list):
    aux:list = []

    for x in classes:
        aux.append((x[0] + x[1]) / 2)
    
    return aux


def full_range(classes:list):
    return float(classes[len(classes) - 1][1]) - float(classes[0][0])


def class_breadth(full_range:float, classes:list):    
    return full_range / len(classes)


def organize_set(classes:list):
    aux:list = []
    for x in range(0, int(len(classes)), 2):
        aux.append([classes[x], classes[x + 1]])
    
    return aux


def sample_qtt(fi:list):
    aux:int = 0

    for x in fi:
        aux += x
    
    return aux


def max_min(set:list):
    max_min:list = []

    max_min.append(set[0][0])
    max_min.append(set[len(set) - 1][1]) 
    
    return max_min


def mean(mid_point:list, fi:list, sample_qtt:int):
    value1:float = 0
    
    for x in range(len(mid_point)):
        value1 += float(mid_point[x]) * float(fi[x])

    return round(value1 / sample_qtt, 2)


def mode(classes:list, fi:list, class_breadth:float):
    bigger_index:list = []
    bigger_freq:float = 0.0
    modes:float = 0.0

    for x in range(len(fi)):
        if float(fi[x]) > bigger_freq:
            bigger_index.clear()
            bigger_index.append(x)
            bigger_freq = fi[x]
    
    for x in range(len(fi)):
        if float(fi[x]) == bigger_freq and bigger_index[0] != x:
            bigger_index.append(x)
    
    for x in bigger_index:
        if x == 0:
            aux:float = fi[x] - 0
            aux /= fi[x] - 0 + fi[x] - fi[x + 1]
            aux *= class_breadth
            aux += classes[x][0]
        elif x == len(fi) - 1:
            aux:float = fi[x] - fi[x - 1]
            aux /= fi[x] - fi[x - 1] + fi[x] - 0
            aux *= class_breadth
            aux += classes[x][0]
        else:
            aux:float = fi[x] - fi[x - 1]
            aux /= fi[x] - fi[x - 1] + fi[x] - fi[x + 1]
            aux *= class_breadth
            aux += classes[x][0]

        modes = aux
    
    return modes


def median(classes:list, fi:list, fac:list, class_breadth:float):
    aux:int = fac[len(fac) - 1]
    median_index:int  = 0
    median:float = 0.0
    
    if aux % 2 != 0:
        aux /= 2

        for x in fac:
            if aux > x:
                median_index += 1

        median = aux - fac[median_index - 1]
        median /= fi[median_index]
        median *= class_breadth
        median += classes[median_index][0]

        return round(median, 2)
    else:
        aux /= 2

        for x in fac:
            if aux > x and aux + 1 > x:
                median_index += 1

        median = aux - fac[median_index - 1]
        median /= fi[median_index]
        median *= class_breadth
        median += classes[median_index][0]

        return round(median, 2)


def percentile(percentile:int, set:list, fi:list, fac:list, class_breadth:float):
    
    if percentile == 0:
        return set[0][0]
    elif percentile == 100:
        return set[len(set) - 1][1]
    else:
        perc_result:float = 0.0
        element:int = 0

        element = (percentile * fac[len(fac) - 1]) / 100

        for x in range(len(fac)):
            if element < fac[x]:
                perc_result = element - fac[x - 1]
                perc_result *= class_breadth
                perc_result /= fi[x]
                perc_result += set[x][0]
                break

        return perc_result


def quartiles(set:list, fi:list, fac:list, class_breadth:float):
    quartile:list = []

    for x in range(0, 101, 25):
        quartile.append(percentile(x, set, fi, fac, class_breadth))
    
    return quartile


def variance(mid_point:list, fi:list, mean:float, sample_qtt:int):
    value_1:float = 0

    for x in range(len(mid_point)):
        value_1 += pow(float(mid_point[x]) - mean, 2) * float(fi[x])

    return value_1 / (sample_qtt - 1)


def sd(variance_result:float):
    return math.sqrt(variance_result)


def cv(stan_dev_result:float, mean:float):
    return (stan_dev_result / mean) * 100


def gen_calc_continuous_sets(set:list, fi:list, print_data:bool = False):
    classes:list = organize_set(set)
    fc = fac(fi)
    fd = fad(fi)
    fr = fir(fi)
    fcr = facr(fr)
    fdr = fadr(fr)
    m_p = mid_points(classes)
    f_r = full_range(classes)
    c_b = class_breadth(f_r, classes)
    s_q = sample_qtt(fi)
    mxmn = max_min(classes)
    average = mean(m_p, fi, s_q)
    mod = mode(classes, fi, c_b)
    med = median(classes, fi, fc, c_b)
    quart = quartiles(classes, fi, fc, c_b)
    var = variance(m_p, fi, average, s_q)
    standard_deviation = sd(var)
    coefficient_variation = cv(standard_deviation, average)
    result_vector:list = []

    result_vector.append(classes)
    result_vector.append(fi)
    result_vector.append(fr)
    result_vector.append(fc)
    result_vector.append(fd)
    result_vector.append(fcr)
    result_vector.append(fdr)
    result_vector.append(m_p)
    result_vector.append(f_r)
    result_vector.append(c_b)
    result_vector.append(s_q)
    result_vector.append(mxmn)
    result_vector.append(average)
    result_vector.append(mod)
    result_vector.append(med)
    result_vector.append(quart)
    result_vector.append(var)
    result_vector.append(standard_deviation)
    result_vector.append(coefficient_variation)

    if print_data == True:
        print("Classes: " + str(classes))
        print("Fi: " + str(fi))
        print("Fir: " + str(fr))
        print("Fac: " + str(fc))
        print("Fad: " + str(fd))
        print("Facr: " + str(fcr))
        print("Fadr: " + str(fdr))
        print("Mid points: " + str(m_p))
        print("Full range: " + str(f_r))
        print("Class breadth: " + str(c_b))
        print("Total samples: " + str(s_q))
        print("Min: " + str(mxmn[0]) + " | Max: " + str(mxmn[1]))
        print("Mean: " + str(average))
        print("Mode: " + str(mod))
        print("Median: " + str(med))
        print("Q0: " + str(quart[0]) + " | Q1: " + str(quart[1]) + " | Q2: " + str(quart[2]) + " | Q3: " + str(quart[3]) + " | Q4: " + str(quart[4]))
        print("Variance: " + str(variance))
        print("Standard deviation: " + str(standard_deviation))
        print("Coefficient variation: " + str(coefficient_variation))

        return result_vector
    else:
        return result_vector
