import math


def fi(set:list, respective_values:bool = False):
    aux:list = []
    freq:list = []

    if respective_values == False:
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


def var_values(set:list):
    aux:list = []

    for x in set:
        if aux.count(x) == 0:
            aux.append(x)
    
    return aux


def full_range(set:list):
    set.sort()
    return float(set[len(set) - 1]) - float(set[0])


def class_breadth(full_range:float, set:list):    
    if len(set) <= 25:
        return full_range / 5
    else:
        return full_range / math.sqrt(len(set))


def organize_set(set:list):
    aux:list = []
    for x in range(0, int(len(set)), 2):
        aux.append([set[x], set[x + 1]])
    
    return aux


def mean(set:list):
    aux:float = 0.0
    
    for x in set:
        aux += x
    
    return aux / len(set)


def mode(set:list):
    most_repeating_value:float = 0.0
    highest_occurrence:int = 0
    aux:list = []

    for x in set:
        if aux.count(x) == 0:
            aux.append(x)
    
    for x in range(len(aux)):
        if set.count(aux[x]) > highest_occurrence:
            highest_occurrence = set.count(aux[x])
            most_repeating_value = aux[x]
    
    return most_repeating_value


def median(set:list):
    aux:float = 0.0

    if len(set) % 2 == 0:
        set.sort()
        aux = set[int(len(set) / 2)] + set[int((len(set) / 2) - 1)]
        aux /= 2
    else:
        set.sort()
        aux = set[math.floor(len(set) / 2)]
    
    return aux


def sample_qtt(set:list):
    return len(set)


def max_min(set:list):
    max_min:list = []

    set.sort()
    max_min.append(set[0])
    max_min.append(set[len(set) - 1])
    
    return max_min



def quartiles(set:list):
    quartile:list = [0.0, 0.0]
    
    set.sort()

    if len(set) % 2 != 0:
        q1:int = int(math.floor(len(set) * 0.25))
        q2:int = int(math.floor(len(set) * 0.5))
        q3:int = int(math.floor(len(set) * 0.75))

        quartile[0] = set[q1]
        quartile[1] = set[q3]

        return quartile
    else:
        q1:int = int(math.floor(len(set) * 0.25))
        q2:int = int(math.floor(len(set) * 0.5))
        q3:int = int(math.floor(len(set) * 0.75))

        if q2 % 2 != 0:
            quartile[0] = set[q1]
            quartile[1] = set[q3]
        else:
            quartile[0] = (set[q1] + set[q1 - 1]) / 2
            quartile[1] = (set[q3] + set[q3 - 1]) / 2

        return quartile


def create_class_table(set:list, class_qtt:int = 0):

    if class_qtt == 0:
        class_list:list = []
        mxmn:list = max_min(set, True)
        classes_qtt:int = 0
        c_b:float = class_breadth(full_range(set, True), set, True)

        if len(set) <= 25:
            classes_qtt = 5
        else:
            classes_qtt = int(math.floor(math.sqrt(len(set))))
        
        class_list.append(float(mxmn[0]))

        for x in range(0,classes_qtt * 2,2):
            class_list.append(class_list[x] + c_b)
            class_list.append(class_list[x] + c_b)
        
        class_list.pop()
    else:
        class_list:list = []
        mxmn:list = max_min(set, True)
        c_b:float = full_range(set, True) / class_qtt

        class_list.append(float(mxmn[0]))

        for x in range(0, class_qtt * 2, 2):
            class_list.append(class_list[x] + c_b)
            class_list.append(class_list[x] + c_b)
        
        class_list.pop()
    
    return organize_set(class_list)


def variance(mid_point:list, fi:list, mean:float, sample_qtt:int):
    value_1:float = 0

    for x in range(len(mid_point)):
        value_1 += pow(float(mid_point[x]) - mean, 2) * float(fi[x])

    return value_1 / (sample_qtt - 1)


def sd(variance_result:float):
    return math.sqrt(variance_result)


def cv(stan_dev_result:float, mean:float):
    return (stan_dev_result / mean) * 100



def gen_calc_discrete_sets(set:list, print_data:bool = False):
    class_table = create_class_table(set)
    fa = fi(set)
    fr = fir(fa)
    fc = fac(fa)
    fd = fad(fa)
    fcr = facr(fr)
    fdr = fadr(fr)
    v_v = var_values(set)
    f_r = full_range(set)
    c_b = class_breadth(f_r, set)
    sampleQtt = sample_qtt(fa)
    maxMin = max_min(set)
    average = mean(set)
    mod = mode(set)
    med = median(set)
    quart = quartiles(set)
    var = variance(v_v, fi, average, sampleQtt)
    standard_deviation = sd(var)
    coefficient_variation = cv(standard_deviation, average)
    result_vector:list = []

    result_vector.append(set)
    result_vector.append(class_table)
    result_vector.append(fa)
    result_vector.append(fr)
    result_vector.append(fc)
    result_vector.append(fd)
    result_vector.append(fcr)
    result_vector.append(fdr)
    result_vector.append(v_v)
    result_vector.append(f_r)
    result_vector.append(c_b)
    result_vector.append(sampleQtt)
    result_vector.append(maxMin)
    result_vector.append(average)
    result_vector.append(mod)
    result_vector.append(med)
    result_vector.append(quart)
    result_vector.append(var)
    result_vector.append(standard_deviation)
    result_vector.append(coefficient_variation)

    if print_data == True:
        print("Set: " + str(set))
        print("Class table: " + str(class_table))
        print("Fi: " + str(fi))
        print("Fir: " + str(fir))
        print("Fac: " + str(fac))
        print("Fad: " + str(fad))
        print("Facr: " + str(facr))
        print("Fadr: " + str(fadr))
        print("Mid points: " + str(v_v))
        print("Full range: " + str(f_r))
        print("Class breadth: " + str(c_b))
        print("Total samples: " + str(sampleQtt))
        print("Min: " + str(maxMin[0]) + " | Max: " + str(maxMin[1]))
        print("Mean: " + str(average))
        print("Mode: " + str(mod))
        print("Median: " + str(med))
        print("Q1: " + str(quart[0]) + " | Q3: " + str(quart[1]))
        print("Variance: " + str(var))
        print("Standart deviation: " + str(standard_deviation))
        print("Coefficient variation: " + str(coefficient_variation))

        return result_vector
    else:
        return result_vector
