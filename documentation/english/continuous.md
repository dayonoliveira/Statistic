# `continuous.py` module

## Introduction

This file is intended to clarify the functioning of each function of the `continuous.py` module, so that the developer can solve all your doubts. If you have read the document and still do not understand something or have encountered a problem, please open a new [issue](https://github.com/dayonoliveira/Statistic/issues) reporting the problem or question.

In each function you will have examples of how they work. The examples will be based on a data set taken from a list of exercises in the Quantitative Methods in Computing course, from the Computer Science course at Universidade de Fortaleza.


- Continuous data set:
  - Image of the set (class table) - Question 9:
      
      ![Questão 9](../../img/questao-9.png)
      
  - List of classes (unorganized):
      - `[50,60,60,70,70,80,80,90,90,100]`
  - List of absolute frequencies:
      - `[2,15,50,10,3]`

### Summary

  - [`fir`](#fir)
  - [`fac`](#fac)
  - [`fad`](#fad)
  - [`facr`](#facr)
  - [`fadr`](#fadr)
  - [`mid_points`](#midpoints)
  - [`full_range`](#fullrange)
  - [`class_breadth`](#classbreadth)
  - [`sample_qtt`](#sampleqtt)
  - [`max_min`](#maxmin)
  - [`mean`](#contmean)
  - [`mode`](#contmode)
  - [`median`](#contmedian)
  - [`percentile`](#percentile)
  - [`quartiles`](#quartiles)
  - [`variance`](#sptwo)
  - [`sd`](#sd)
  - [`cv`](#cv)
  - [`organize_set`](#organizeset)
  - [`gen_calc_continuous_sets`](#gencalccontinuoussets)


## `fir`

Function that calculates the relative frequency of classes, based on the absolute frequency. The return is a list of numbers like `float`.

### Parameters:

- `fi: list`: Receives the absolute frequency of the continuous dataset.

### Return:

- `aux: list`: Returns a list of relative frequencies from the dataset.

### Examples:

```python
fr:list = fir([2,15,50,10,3])
print(fr)
```

```bash
[0.025, 0.1875, 0.625, 0.125, 0.0375]
```

## `fac`

This is the function to calculate the accumulated frequencies in an increasing way. It uses the list of absolute frequencies as a basis.

### Parameters:

- `fi: list`: Like the previous function, it receives the list of absolute frequencies from the continuous dataset.

### Return:

- `aux: list`: Returns a list of increasing frequencies accumulated.

### Example:

```python
fc:list = fac([2,15,50,10,3])
print(fc)
```

```bash
[2, 17, 67, 77, 80]
```

## `fad`

As well as the function for calculating accumulated frequencies, this one also serves this purpose, but in a decreasing manner.

### Parameters:

- `fi: list`: Receives the list of absolute frequencies from the continuous dataset.

### Return:

- `aux: list`: Returns a list of accumulated frequencies in descending order.

### Example:

```python
fd:list = fad([2,15,50,10,3])
print(fd)
```

```bash
[80, 78, 63, 13, 3]
```

## `facr`

This function calculates the accumulated relative frequencies in an increasing way.

### Parameters:

- `fir: list`: The list of relative frequencies from the continuous dataset is received.

### Return:

- `aux: list`: Returns a list of increasing relative frequencies accumulated.

### Example:

```python
fcr:list = facr([0.025, 0.1875, 0.625, 0.125, 0.0375])
print(fcr)
```

```bash
[0.025, 0.2125, 0.8375, 0.9625, 1.0]
```

## `fadr`

It has the same purpose as the previous function, but the calculation of the accumulated relative frequencies is decreasing.

### Parameters:

- `fir: list`: Here the list of relative frequencies from the continuous dataset is passed.

### Return:

- `aux: list`: Returns a list of decreasing relative frequencies.

### Example:

```python
fdr:list = fadr([0.025, 0.1875, 0.625, 0.125, 0.0375])
print(fdr)
```

```bash
[1.0, 0.975, 0.7875, 0.1625, 0.0375]
```

## `mid_points`

This has the same purpose as the previous function, but it is used for class table (continuous dataset).

### Parameters:

- `classes: list`: Receives a list with already organized class boundaries (See [here](#organizeset) the function to organize classes) and returns a list with the midpoints of each class.

### Return:

- `aux: list`: Returns a list of the midpoints of the continuous dataset.

### Example:

```python
mid_p:list = mid_points(
  [[50, 60], [60, 70], [70, 80], [80, 90], [90, 100]]
)
print(mid_p)
```

```bash
[55.0, 65.0, 75.0, 85.0, 95.0]
```

## `full_range`

Function responsible for calculating the total amplitude of the classes of a continuous dataset.

### Parameters:

- `classes: list`: Receives a list with already organized class boundaries (See [here](#organizeset) the function to organize classes).

### Return:

- `</>: float`: Returns a result of a calculation to find the total amplitude.

### Example:

```python
f_r:float = full_range(
  [[50, 60], [60, 70], [70, 80], [80, 90], [90, 100]]
)
print(f_r)
```

```bash
50.0
```

## `class_breadth`

Function responsible for calculating the range of continuous dataset class.

### Parameters:

- `full_range: float`: Receives the result of the calculation of the [full range](#fullrange).
- `classes: list`: Receives a list with already organized class boundaries (See [here](#organizeset) the function to organize classes).

### Return:

- `</>: float`: Returns the result of a calculation to find the class breadth.

### Example:

```python
class_b:float = class_breadth(
  50.0,
  [[50, 60], [60, 70], [70, 80], [80, 90], [90, 100]]
)
print(class_b)
```

```bash
10.0
```

## `sample_qtt`

Function that calculates the total of samples based on the absolute frequency of a class table.

### Parameters:

- `fi: list`: Receives the list of absolute frequencies from the class table.

### Return:

- `#: int`: Returns the number of samples from a continuous dataset.

### Example:

```python
sample_q:int = sample_qtt([2, 15, 50, 10, 3])
print(sample_q)
```

```bash
80
```

## `max_min`

This function captures the maximum and minimum points of a continuous dataset.

### Parameters:

- `set: list`: Receives a list with the continuous dataset.

### Return:

- `max_min: list`: Returns a list of two positions where the first is the minimum point of the set and the second is the maximum point of the set.

### Example:

```python
mx_mn:list = max_min([[50, 60], [60, 70], [70, 80], [80, 90], [90, 100]])
print(mx_mn)
```

```bash
[50, 100]
```

## `mean`

This function calculates the average of a continuous data set (class table).

### Parameters:

- `mid_point: list`: Receives the list with the average points of the class table calculated in [this function](#midpoints).
- `fi: list`: Receives the list with absolute frequencies from the class table.
- `sample_qtt: int`: Receives the number of samples from the calculated class table [in this function](#sampleqtt).

### Return:

- `</>: float`: Returns the result of a calculation to find the mean of the continuous data set.

### Example:

```python
average:float = mean(
  [55.0, 65.0, 75.0, 85.0, 95.0],
  [2, 15, 50, 10, 3],
  80
)
print(average)
```

```bash
74.62
```

## `mode`

Function that calculates the mode of a continuous data set (class table).

### Parameters:

- `classes: list`: Receives a list of organized class boundaries (See [here](#organizeset) the function to organize classes).
- `fi: list`: Receives a list of absolute frequencies from the class table.
- `class_breadth: float`: Receives the result of calculating [class breadth](#classbreadth).

### Return:

- `modes: list`: Returns a list of all modes from the continuous dataset.

### Example:

```python
mod:list = mode(
  [[50, 60], [60, 70], [70, 80],
  [80, 90], [90, 100]],
  [2, 15, 50, 10, 3],
  10.0
)
print(mod)
```

```bash
[74.67]
```

## `median`

Function that calculates the median of a continuous data set (class table).

### Parameters:

- `classes: list`: Gets the list with the organized class boundaries (See [here](#organizeset) the function to organize the classes).
- `fi: list`: Here the list with the absolute frequencies of the class table is passed.
- `fac: list`: Here, the list with the accumulated frequencies from the class table is passed.
- `class_breadth`: Receives the result of calculating [class breadth](#classbreadth).

### Return:

- `median: float`: Returns the median of a continuous data set.

### Example:

```python
med:float = median(
  [[50, 60], [60, 70], [70, 80], [80, 90], [90, 100]],
  [2, 15, 50, 10, 3],
  [2, 17, 67, 77, 80],
  10.0
)
print(med)
```

```bash
74.6
```

## `percentile`

It aims to calculate the percentile value passed by the user.

### Parameters:

- `percentile: int`: Receives the percentile to be calculated.
- `set: list`: Gets the list of the continuous dataset.
- `fi: list`: Receives the list of absolute frequencies from the dataset.
- `fac: list`: Receives the list of accumulated frequencies in ascending order from the dataset.
- `class_breadth: float`: Receives the range of classes.

### Return:

- `perc_result: float`: Returns the value for the percentile passed as a parameter.

### Example:

```python
perc:float = percentile(23, [[50, 60], [60, 70], [70, 80], [80, 90], [90, 100]], [2, 15, 50, 10, 3], [2, 17, 67, 77, 80], 10.0)
print(perc)
```

```bash
70.28
```
## `quartiles`

This function is responsible for calculating the quartiles of a continuous dataset.

### Parameters:

- `set: list`: Receives the continuous dataset.
- `fi: list`: Receives a list with the absolute frequencies of the continuous dataset.
- `fac: list`: Receives a list with the accumulating increasing frequencies of the continuous dataset.
- `class_breadth: float`: Receives the class breadth.

### Return:

- `quartile: list`: Returns a list of five positions, where:
  - i0 = Q0 (0%)
  - i1 = Q1 (25%)
  - i2 = Q2 (50%)
  - i3 = Q3 (75%)
  - i4 = Q4 (100%)

### Example:

```python
quart:list = quartiles(
  [[50, 60], [60, 70], [70, 80], [80, 90], [90, 100]],
  [2, 15, 50, 10, 3],
  [2, 17, 67, 77, 80],
  10.0
)
print(quart)
```

```bash
[50, 70.6, 74.6, 78.6, 100]
```

## `variance`

This function calculates the variance of continuous data sets.

### Parameters:

- `mid_point: list`: Receives the list with the midpoints of the continuous dataset.
- `fi: list`: Receives the list with absolute frequencies.
- `mean: float`: Here the average of the continuous dataset is passed.
- `sample_qtt: int`: Here the total samples of the continuous dataset are passed.

### Return:

- `</>: float`: Returns the result of a calculation to find the variance of a continuous data set.

### Example:

```python
var:float = variance(
  [55.0, 65.0, 75.0, 85.0, 95.0],
  [2, 15, 50, 10, 3],
  74.62,
  80
)
print(var)
```

```bash
56.82
```

## `sd`

This function calculates the standard deviation of the class table.

### Parameters:

- `variance_result: float`: Receives the result of the variance calculation.

### Return:

- `</>: float`: Returns the result of a calculation to find the standard deviation of a continuous data set.

### Example:

```python
standard_deviation:float = sd(56.82)
print(standard_deviation)
```

```bash
7.54
```

## `cv`

This function calculates the coefficient of variation of the class table.

### Parameters:

- `stan_dev_result: float`: Receives the result of the standard deviation calculation.
- `mean: float`: Get the mean from the class table.

### Return:

- `</>: float`: Returns the result of a calculation to find the coefficient of variation of a set of continuous data.

### Example:

```python
coefficient_variation:float = cv(7.54, 74.62)
print(coefficient_variation)
```

```bash
10.1
```

## `organize_set`

This function has the purpose of organizing the data referring to the class table. It takes a normal list of limits and returns a list of organized classes.

### Parameters:

- `classes: list`: Receives an array with class boundaries from the class table.

### Return:

- `aux: list`: Returns a list of classes arranged in small vectors within the list, similar to a class table.

### Example:

```python
organized_classes:list = organize_set(
  [50,60,60,70,70,80,80,90,90,100]
)
print(organized_classes)
```

```bash
[[50, 60], [60, 70], [70, 80], [80, 90], [90, 100]]
```

## `gen_calc_continuous_sets`

This function does all possible library calculations for continuous datasets, large or small, and returns all values ​​in a list. You can choose whether or not to print the results in the output.

### Parameters:

- `set: list`: Set of data as it is in the class table.
- `fi: list`: Absolute (simple) frequency of the data set.
- `print_data: bool` (optional): This is responsible for dictating whether or not the function will print the results. By default it is set to `False`.

### Return:

- `result_vector: list`: Returns a list with all the results of all possible calculations from the library.
- `print` (optional): There is the possibility to print the results after calculations.

### Example:

```python
gen_cont_set:list = gen_calc_continuous_sets(
  [50,60,60,70,70,80,80,90,90,100],
  [2,15,50,10,3],
  True
)
```

```bash
Classes: [[50, 60], [60, 70], [70, 80], [80, 90], [90, 100]]
Fi: [2, 15, 50, 10, 3]
Fir: [0.025, 0.1875, 0.625, 0.125, 0.0375]
Fac: [2, 17, 67, 77, 80]
Fad: [80, 78, 63, 13, 3]
Facr: [0.025, 0.2125, 0.8375, 0.9625, 1.0]
Fadr: [1.0, 0.975, 0.7875, 0.1625, 0.0375]
Mid points: [55.0, 65.0, 75.0, 85.0, 95.0]
Full range: 50.0
Class breadth: 10.0
Total samples: 80
Mean: 74.62
Mode: [74.67]
Median: 74.6
Variance: 56.82
Standart deviation: 7.54
Coefficient variation: 10.1
```