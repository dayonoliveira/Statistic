# `discrete.py` module

## Introduction

This file aims to clarify the functioning of each function of the `discrete.py` module, so that the developer can solve all your doubts. If you have read the document and still do not understand something or have encountered a problem, please open a new [issue](https://github.com/dayonoliveira/Statistic/issues) reporting the problem or question.

In each function you will have examples of how they work. The examples will be based on a data set taken from a list of exercises in the Quantitative Methods in Computing course, from the Computer Science course at Universidade de Fortaleza.

- Discrete data set
  - Image of the set - Question 8:
    
    ![Questão 8](../../img/questao-8.png)
    
  - Set list:
    - `[1,3,-2,2,4,2,5,-2,4,3]`

### Summary

  - [`fi`](#fi)
  - [`fir`](#fir)
  - [`fac`](#fac)
  - [`fad`](#fad)
  - [`facr`](#facr)
  - [`fadr`](#fadr)
  - [`var_values`](#varvalues)
  - [`full_range`](#fullrange)
  - [`class_breadth`](#classbreadth)
  - [`mean`](#mean)
  - [`mode`](#mode)
  - [`median`](#median)
  - [`sample_qtt`](#sampleqtt)
  - [`max_min`](#maxmin)
  - [`percentile`](#percentile)
  - [`quartiles`](#quartiles)
  - [`create_class_table`](#createclasstable)
  - [`variance`](#sptwo)
  - [`sd`](#sd)
  - [`cv`](#cv)
  - [`organize_set`](#organizeset)
  - [`gen_calc_discrete_sets`](#gencalcdiscretesets)


## `fi`

This function calculates the absolute (simple) frequency of a set of discrete data. There is the possibility of returning a vector with only absolute frequencies or a vector with values ​​and their respective frequencies.

### Parameters:

- `set: list`: Here the raw dataset is entered. It has to be passed in `list` form.
- `respective_values: bool`: This option allows to alternate between the data return, allowing to return a vector with only the absolute frequencies (`False` by default) or the values ​​with their respective frequencies (`True`).

### Return:

- `freq: list`: Returns a list of absolute frequencies only, or a list of frequencies and their respective values.

### Examples:

Standard form:
```python
fa:list = fi([1,3,-2,2,4,2,5,-2,4,3])
print(fa)
```

```bash
[1, 2, 2, 2, 2, 1]
```

Form with the respective values:
```python
fa:list = fi([1,3,-2,2,4,2,5,-2,4,3], True)
print(fa)
```

```bash
[[1, 1], [3, 2], [-2, 2], [2, 2], [4, 2], [5, 1]]
```

## `fir`

Function that calculates the relative frequency of the discrete data set based on the absolute frequency. The return is a list of numbers like `float`.

### Parameters:

- `fi: list`: Receives the absolute frequency of the discrete data set.

### Return:

- `aux: list`: Returns a list of the relative frequencies of the data set.

### Example:

```python
fr:list = fir([1, 2, 2, 2, 2, 1])
print(fr)
```

```bash
[0.1, 0.2, 0.2, 0.2, 0.2, 0.1]
```

## `fac`

This is the function to calculate the accumulated frequencies in an increasing way. It uses the list of absolute frequencies as a basis.

### Parameters:

- `fi: list`: Like the previous function, it receives the list with the absolute frequencies of the discrete data set.

### Return:

- `aux: list`: Returns a list of increasing frequencies accumulated.

### Example:

```python
fc:list = fac([1, 2, 2, 2, 2, 1])
print(fc)
```

```bash
[1, 3, 5, 7, 9, 10]
```

## `fad`

As well as the function for calculating accumulated frequencies, this one also serves this purpose, but in a decreasing manner.

### Parameters:

- `fi: list`: Receives the list of absolute frequencies from the discrete or continuous data set.

### Return:

- `aux: list`: Returns a list of accumulated frequencies in decreasing order.

### Example:

```python
fd:list = fad([1, 2, 2, 2, 2, 1])
print(fd)
```

```bash
[10, 9, 7, 5, 3, 1]
```

## `facr`

This function calculates the accumulated relative frequencies in an increasing way.

### Parameters:

- `fir: list`: The list of relative frequencies from the discrete data set is received.

### Return:

- `aux: list`: Returns a list of increasing relative frequencies accumulated.

### Example:

```python
fcr:list = facr([0.1, 0.2, 0.2, 0.2, 0.2, 0.1])
print(fcr)
```

```bash
[0.1, 0.30000000000000004, 0.5, 0.7, 0.8999999999999999, 0.9999999999999999]
```

## `fadr`

It has the same purpose as the previous function, but the calculation of the accumulated relative frequencies is decreasing.

### Parameters:

- `fir: list`: Here the list of relative frequencies of the discrete data set is passed.

### Return:

- `aux: list`: Returns a list of decreasing relative frequencies.

### Example:

```python
fdr:list = fadr([0.1, 0.2, 0.2, 0.2, 0.2, 0.1])
print(fdr)
```

```bash
[0.9999999999999999, 0.8999999999999999, 0.7, 0.5, 0.30000000000000004, 0.1]
```

## `var_values`

This function collects the midpoints (variable values) of a set of discrete data.

### Parameters:

- `set: list`: Receives a list with the discrete data set.

### Return:

- `aux: list`: Returns a list of the midpoints (variable values) of the discrete data set.

### Example:

```python
var_val:list = var_values([1,3,-2,2,4,2,5,-2,4,3])
print(var_val)
```

```bash
[1, 3, -2, 2, 4, 5]
```

## `full_range`

Function responsible for calculating the total amplitude of the discrete data set.

### Parameters:

- `set: list`: Receives a list with a set of discrete data.

### Return:

- `</>: float`: Returns a result of a calculation to find the total amplitude.

### Example:

```python
f_r:float = full_range([1,3,-2,2,4,2,5,-2,4,3])
print(f_r)
```

```bash
7.0
```

## `class_breadth`

Function responsible for calculating the class amplitude of a set of discrete data.

### Parameters:

- `fullRange: float`: Receives the result of the calculation of the [full range](#fullrange).
- `classes: list`: Receives the discrete data set.

### Return:

- `</>: float`: Returns the result of a calculation to find the class span.

### Example:

```python
class_b:float = class_breadth(7.0, [1,3,-2,2,4,2,5,-2,4,3])
print(class_b)
```

```bash
1.4
```

## `mean`

Function that averages a set of discrete data.

### Parameters:

- `set: list`: Receives the list with the data of the set.

### Return:

- `aux: float`: Returns the average of a set of discrete data.

### Example:

```python
average:float = mean([1,3,-2,2,4,2,5,-2,4,3])
print(average)
```

```bash
2.0
```

## `mode`

Function that calculates the mode of a set of discrete data.

### Parameters:

- `set: list`: Receives the list of data from the data set.

### Return:

- `most_repeating_value: list`: Returns a list of all modes from a discrete data set.

### Example:

```python
mod:list = mode([1,3,-2,2,4,2,5,-2,4,3])
print(mod)
```

```bash
[-2, 2, 3, 4]
```

## `median`

Function that calculates the median of a set of discrete data.

### Parameters:

- `set: list`: Receives the list with the data from the data set.

### Return:

- `aux: float`: Returns the median of a set of discrete data.

### Example:

```python
med:float = median([1,3,-2,2,4,2,5,-2,4,3])
print(med)
```

```bash
2.5
```

## `sample_qtt`

Function that calculates total samples based on the size of a discrete data set.

### Parameters:

- `set: list`: Receives the discrete data set.

### Return:

- `#: int`: Returns the number of samples from a discrete data set.

### Example:

```python
sample_q:int = sample_qtt(
  [1,3,-2,2,4,2,5,-2,4,3]
)
print(sample_q)
```

```bash
10
```

## `max_min`

This function captures the maximum and minimum points of a set of discrete data.

### Parameters:

- `set: list`: Receives a list with the discrete data set.

### Return:

- `max_min: list`: Returns a list of two positions where the first is the minimum point of the set and the second is the maximum point of the set.

### Example:

```python
mx_mn:int = max_min([1,3,-2,2,4,2,5,-2,4,3])
print(mx_mn)
```

```bash
[-2, 5]
```

## `percentile`

It aims to calculate the percentile value passed by the user.

### Parameters:

- `perc: int`: Gets the percentile of the value you want to find.
- `set: list`: Get the set of discrete data.

### Return:

- `value: float`: Value referring to the percentile that was passed in the parameters.

### Example:

```python
perc:float = percentile(45, [1,3,-2,2,4,2,5,-2,4,3])
print(perc)
```

```bash
2.05
```

## `quartiles`

This function is responsible for calculating the quartiles of a set of discrete data.

### Parameters:

- `set: list`: Receives the discrete data set.

### Return:

- `quartile: list`: Returns a list of five positions, where:
  - i0 = Q0 (0%)
  - i1 = Q1 (25%)
  - i2 = Q2 (50%)
  - i3 = Q3 (75%)
  - i4 = Q4 (100%)

### Example:

```python
quart:list = quartiles([1,3,-2,2,4,2,5,-2,4,3])
print(quart)
```

```bash
[-2, 1.25, 2.5, 3.75, 5]
```

## `create_class_table`

This function aims to create a list simulating a class table for discrete data sets.

### Parameters:

- `set: list`: Receives the list with the discrete data set.
- `class_qtt: int` (`0` by default): Receives a fixed amount of classes to be created.

### Return:

- `class_list: list`: Returns a list of classes already organized.

### Examples:

Without passing the fixed number of classes:
```python
class_table:list = create_class_table([1,3,-2,2,4,2,5,-2,4,3])
print(class_table)
```

```bash
[[-2.0, -0.6], [-0.6, 0.79], [0.79, 2.19], [2.19, 3.59], [3.59, 5.0]]
```

Passing the fixed amount of classes:
```python
class_table:list = create_class_table([1,3,-2,2,4,2,5,-2,4,3], 3)
print(class_table)
```

```bash
[[-2.0, 0.33], [0.33, 2.66], [2.66, 5.0]]
```

## `variance`

This function calculates the variance of discrete data sets.

### Parameters:

- `mid_point: list`: Receives the list with the midpoints of the discrete dataset
- `fi: list`: Receives the list with absolute frequencies.
- `mean: float`: Here the average of the discrete dataset is passed.
- `sample_qtt: int`: Here the total of samples from the discrete data set is passed.

### Return:

- `</>: float`: Returns the result of a calculation to find the variance of a set of discrete data.

### Example:

```python
var:float = variance(
  [1, 3, -2, 2, 4, 5],
  [1, 2, 2, 2, 2, 1],
  2.0,
  10
)
print(var)
```

```bash
3.44
```

## `sd`

This function calculates the standard deviation of the discrete data set.

### Parameters:

- `variance_result: float`: Receives the result of the variance calculation.

### Return:

- `</>: float`: Returns the result of a calculation to find the standard deviation of a set of discrete data.

### Example:

```python
standard_deviation:float = sd(3.44)
print(standard_deviation)
```

```bash
1.85
```

## `cv`

This function calculates the coefficient of variation of a discrete data set.

### Parameters:

- `stan_dev_result: float`: Receives the result of the standard deviation calculation.
- `mean: float`: Receives the average of the discrete data set.

### Return:

- `</>: float`: Returns the result of a calculation to find the coefficient of variation of a set of discrete data.

### Example:

```python
coefficient_variation:float = cv(1.85, 2.0)
print(coefficient_variation)
```

```bash
92.5
```

## `organize_set`

This function has the purpose of organizing the data referring to the class table. It takes a normal list of limits and returns a list of organized classes.

### Parameters:

- `classes: list`: Receives an array with class boundaries from the class table.

### Return:

- `aux: list`: Returns a list of classes arranged in small vectors within the list, similar to a class table.

> Warning: It is only for the purpose of transforming a boundary vector into a class vector. If you pass a set of discrete data it will not return a correct value for your purpose.

### Example:

```python
organized_classes:list = organize_set(
  [-2.0, -0.6000000000000001, -0.6000000000000001, 0.7999999999999998, 0.7999999999999998, 2.1999999999999997, 2.1999999999999997, 3.5999999999999996, 3.5999999999999996, 5.0]
)
print(organized_classes)
```

```bash
[[-2.0, -0.6000000000000001], [-0.6000000000000001, 0.7999999999999998], [0.7999999999999998, 2.1999999999999997], [2.1999999999999997, 3.5999999999999996], [3.5999999999999996, 5.0]]
```

## `gen_calc_discrete_sets`

This function has the same purpose as the previous one, but its focus is on discrete data sets, large or small. It is also possible to choose whether the function will print the data when it is executed.

### Parameters:

- `set: list`: This is where the dataset goes. Unlike the previous function, this one does not receive data from the class table.
- `print_data: bool` (optional): This is responsible for dictating whether or not the function will print the results. By default it is set to `False`.

### Return:

- `result_vector: list`: Returns a list with the results of all possible calculations from the library.
- `print`: There is also the possibility to print the results after all calculations.

### Example:

```python
gen_disc_set:list = gen_calc_discrete_sets(
  [1,3,-2,2,4,2,5,-2,4,3],
  True
)
```

```bash
Set: [-2, -2, 1, 2, 2, 3, 3, 4, 4, 5]
Class table: [[-2.0, -0.6000000000000001], [-0.6000000000000001, 0.7999999999999998], [0.7999999999999998, 2.1999999999999997], [2.1999999999999997, 3.5999999999999996], [3.5999999999999996, 5.0]]
Fi: [2, 1, 2, 2, 2, 1]
Fir: [0.2, 0.1, 0.2, 0.2, 0.2, 0.1]
Fac: [2, 3, 5, 7, 9, 10]
Fad: [10, 8, 7, 5, 3, 1]
Facr: [0.2, 0.30000000000000004, 0.5, 0.7, 0.8999999999999999, 0.9999999999999999]
Fadr: [1.0, 0.7999999999999999, 0.7, 0.5, 0.30000000000000004, 0.1]
Mid points: [-2, 1, 2, 3, 4, 5]
Full range: 7.0
Class breadth: 1.4
Total samples: 6
Min: -2 | Max: 5
Mean: 2.0
Mode: -2
Median: 2.5
Q0: -2 | Q1: 1.25 | Q2: 2.5 | Q3: 3.75 | Q4: 5
Variance: 10.4
Standard deviation: 3.22490309931942
Coefficient variation: 161.245154965971
```