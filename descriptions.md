English | [Portuguese](descriptions_ptbr.md)

# Descriptions

### Summary

  - [`GeneralCalculationContinuousSets`](#generalcalculationcontinuoussets)
  - [`GeneralCalculationDiscreteSets`](#generalcalculationdiscretesets)
  - [`OrganizeClass`](#organizeclass)
  - [`Fi`](#fi)
  - [`Fir`](#fir)
  - [`Fac`](#fac)
  - [`Fad`](#fad)
  - [`Facr`](#facr)
  - [`Fadr`](#fadr)
  - [`MidPoint`](#midpoint)
  - [`GranMidPoint`](#granmidpoint)
  - [`FullRange`](#fullrange)
  - [`ClassBreadth`](#classbreadth)
  - [`Mean`](#mean)
  - [`Mode`](#mode)
  - [`Median`](#median)
  - [`SampleQtt`](#sampleqtt)
  - [`GranMean`](#granmean)
  - [`GranMode`](#granmode)
  - [`GranMedian`](#granmedian)
  - [`Variance`](#variance)
  - [`StandardDeviation`](#standarddeviation)
  - [`CoefficientVariation`](#coefficientvariation)


## `GeneralCalculationContinuousSets`

This function does all possible library calculations for continuous datasets, large or small, and returns all values ​​in a list. You can choose whether or not to print the results in the output.

### Parameters:

- `set: list`: Set of data as it is in the class table.
- `fi: list`: Absolute (simple) frequency of the data set.
- `printData: bool` (optional): This is responsible for dictating whether or not the function will print the results. By default it is set to `False`.

### Return:

- `resultVector: list`: Returns a list with all the results of all possible calculations from the library.
- `print` (Optional): There is the possibility to print the results after calculations.

Example of a class table:

<img alt="Class table" src="img/tabela-de-classes.png">

Classes are represented by the _Idades_ column and the data passed in the `set` parameter will look like this:

`[18,23,23,28,28,33,33,38,38,43,43,48,48,53]`

So they will be organized by [another function](#organizeclass) and look like this:

`[[18.23],[23.28],[28.33],[33.38],[38.43],[43.48],[48.53]]`

## `GeneralCalculationDiscreteSets`

This function has the same purpose as the previous one, but its focus is on discrete data sets, large or small. It is also possible to choose whether the function will print the data when it is executed.

### Parameters:

- `set: list`: This is where the dataset goes. Unlike the previous function, this one does not receive data from the class table.
- `printData: bool` (optional): This is responsible for dictating whether or not the function will print the results. By default it is set to `False`.

### Return:

- `resultVector: list`: Returns a list with the results of all possible calculations from the library.
- `print`: There is also the possibility to print the results after all calculations.

Discrete dataset example:

<img alt="Discrete dataset" src="img/conjunto-de-dados-discreto.png">

The data that will be passed in the `set` parameter are all the ones in the image above. They would be inside a vector just like the previous function.

## `OrganizeClass`

This function has the purpose of organizing the data referring to the class table. It takes a normal list of limits and returns a list of organized classes.

### Parameters:

- `classes: list`: Receives an array with class boundaries from the class table.

### Return:

- `aux: list`: Returns a list of classes arranged in small vectors within the list, similar to a class table.

Amount received:

`[18,23,23,28,28,33,33,38,38,43,43,48,48,53]`

Return Value:

`[[18.23],[23.28],[28.33],[33.38],[38.43],[43.48],[48.53]]`

> Warning: It is only for the purpose of transforming a boundary vector into a class vector. If you pass a set of discrete data it will not return a correct value for your purpose.

## `Fi`

This function calculates the absolute (simple) frequency of a set of discrete data. There is the possibility of returning a vector with only absolute frequencies or a vector with values ​​and their respective frequencies.

### Parameters:

- `set: list`: Here the raw dataset is inserted. It has to be passed in `list` form.
- `respectiveValues: bool`: This option allows you to alternate between the data return, allowing to return a vector with only the absolute frequencies (`False` by default) or the values ​​with their respective frequencies (`True`).

### Return:

- `freq: list`: Returns a list with only absolute frequencies, or a list of frequencies and their respective values.

## `Fir`

Function that calculates the relative frequency of the discrete dataset or classes, based on the absolute frequency. The return is a list of numbers like `float`.

### Parameters:

- `fi: list`: Receives the absolute frequency of the discrete dataset or the continuous dataset.

### Return:

- `aux: list`: Returns a list of the relative frequencies of the dataset.

## `Fac`

This is the function to calculate the accumulated frequencies in an increasing way. It uses the list of absolute frequencies as a basis.

### Parameters:

- `fi: list`: Just like the previous function, it receives the list with the absolute frequencies of the discrete or continuous dataset.

### Return:

- `aux: list`: Returns a list of increasing frequencies accumulated.

## `Fad`

As well as the function for calculating accumulated frequencies, this one also serves this purpose, but in a decreasing manner.

### Parameters:

- `fi: list`: Receives the list of absolute frequencies from the discrete or continuous dataset.

### Return:

- `aux: list`: Returns a list of accumulated frequencies in decreasing order.

## `Facr`

This function calculates the accumulated relative frequencies in an increasing way.

### Parameters:

- `fir: list`: The list of relative frequencies from the discrete or continuous dataset is received.

### Return:

- `aux: list`: Returns a list of increasing relative frequencies.

## `Fadr`

It has the same purpose as the previous function, but the calculation of the accumulated relative frequencies is decreasing.

### Parameters:

- `fir: list`: Here the list of relative frequencies of the discrete or continuous dataset is passed.

### Return:

- `aux: list`: Returns a list of relative frequencies accumulated in decreasing order.

## `MidPoint`

This function collects the midpoints (variable values) of a set of discrete data.

> Warning: Does not work for class table (continuous dataset) as focus is on discrete dataset.

### Parameters:

- `set: list`: Receives a list with the set of discrete data.

### Return:

- `aux: list`: Returns a list of the midpoints (variable values) of the discrete data set.

## `GranMidPoint`

This has the same purpose as the previous function, but it is used for class table (continuous dataset).

> Warning: Does not work for discrete dataset as focus is on classes from a class table (continuous dataset).

### Parameters:

- `classes: list`: Takes a list with already organized class boundaries (See [here](#organizeclass) the function to organize classes) and returns a list with the midpoints of each class.

### Return:

- `aux: list`: Returns a list with the midpoints of the continuous dataset.

## `FullRange`

Function responsible for calculating the total amplitude of the set of discrete data or classes of a set of continuous data.

### Parameters:

- `classes: list`: Receives a list with already organized class boundaries (See [here](#organizeclass) the function to organize classes) or a set of discrete data.
- `simple: bool` (`False` by default): This parameter dictates whether what will be passed is a set of discrete data (`True`) or a list of class boundaries (`False`).

### Return:

- `</>: float`: Returns a result of a calculation to find the total amplitude.

## `ClassBreadth`

Function responsible for calculating the class amplitude of a set of discrete data or classes (continuous data set).

### Parameters:

- `fullRange: float`: Receives the result of the calculation of the [full range](#fullrange).
- `classes: list`: Receives the set of discrete data or a list with already organized class boundaries (See [here](#organizeclass) the function to organize the classes).
- `simple: bool` (`False` by default): Dictates whether the previous parameter will be a discrete data set (`True`) or a list with class boundaries (`False`).

### Return:

- `</>: float`: Returns the result of a calculation to find the class amplitude.

## `Mean`

Function that averages a set of discrete data.

> Warning: Does not work for class boundary list (continuous dataset) as focus is on discrete dataset.

### Parameters:

- `set: list`: Receives the list with the set data.

### Return:

- `aux: float`: Returns the average of a set of discrete data.

## `Mode`

Function that calculates the mode of a set of discrete data.

> Warning: Does not work for class boundary list (continuous dataset) as focus is on discrete dataset.

### Parameters:

- `set: list`: Gets the list of data from the dataset.

### Return:

- `mostRepeatingValue: list`: Returns a list of all modes from a discrete dataset.

## `Median`

Function that calculates the median of a set of discrete data.

> Warning: Does not work for class boundary list (continuous dataset) as focus is on discrete dataset.

### Parameters:

- `set: list`: Gets the list with the data from the dataset.

### Return:

- `aux: float`: Returns the median of a set of discrete data.

## `SampleQtt`

Function that calculates total samples based on the absolute frequency of a class table or the size of a set of discrete data.

### Parameters:

- `set: list`: Gets the set of discrete data or the list of absolute frequencies from the class table.
- `simple: bool` (`False` by default): Dictates if what will be received in the previous parameter is a set of discrete data (`True`) or the list of absolute frequencies from the class table (`False`).

### Return:

- `#: int`: Returns the number of samples from a set of discrete or continuous data.

## `GranMean`

This function calculates the average of a continuous data set (class table).

> Warning: Does not work for a discrete dataset as the focus is on continuous dataset (class table).

### Parameters:

- `midPoint: list`: Gets the list with the midpoints of the class table calculated in [in this function](#granmidpoint).
- `fi: list`: Gets the list with the absolute frequencies from the class table.
- `sampleQtt: int`: Receives the number of samples from the calculated class table [in this function](#sampleqtt).

### Return:

- `</>: float`: Returns the result of a calculation to find the average of the continuous data set.

## `GranMode`

Function that calculates the mode of a continuous data set (class table).

> Warning: Does not work for a discrete dataset as the focus is on continuous dataset (class table).

### Parameters:

- `classes: list`: Gets a list with organized class boundaries (See [here](#organizeclass) the function to organize classes).
- `fi: list`: Receives a list of absolute frequencies from the class table.
- `classBreadth: float`: Receives the result of calculating the [class breadth](#classbreadth).

### Return:

- `modes: list`: Returns a list of all modes from the continuous dataset.

## `GranMedian`

Function that calculates the median of a continuous data set (class table).

> Warning: Does not work for a discrete dataset as the focus is on continuous dataset (class table).

### Parameters:

- `classes: list`: Gets the list with the organized class boundaries (See [here](#organizeclass) the function to organize the classes).
- `fi: list`: Here the list with the absolute frequencies of the class table is passed.
- `fac: list`: Here the list with the accumulated frequencies of the class table is passed.
- `classBreadth`: Receives the result of calculating the [class breadth](#classbreadth).

### Return:

- `median: float`: Returns the median of a continuous data set.

## `Variance`

This function calculates the variance of discrete and continuous data sets.

### Parameters:

- `midPoint: list`: Receives the list with the midpoints from the discrete dataset or from the class table.
- `fi: list`: Gets the list with the absolute frequencies from the class table.
- `mean: float`: Here the mean of the discrete dataset or the calculated class table is passed.
- `sampleQtt: int`: Here the total samples of the discrete dataset or class table are passed.
- `simple: bool` (`False` by default): This parameter defines whether the calculation will be for a discrete or continuous dataset.

### Return:

- `</>: float`: Returns the result of a calculation to find the variance of a set of discrete or continuous data.

## `StandardDeviation`

This function calculates the standard deviation of the discrete dataset or class table.

### Parameters:

- `varianceResult: float`: Receives the result of the variance calculation.

### Return:

- `</>: float`: Returns the result of a calculation to find the standard deviation of a set of discrete or continuous data.

## `CoefficientVariation`

This function calculates the coefficient of variation of a discrete dataset or class table.

### Parameters:

- `stanDevResult: float`: Receives the result of the standard deviation calculation.
- `mean: float`: Gets the mean of the discrete dataset or class table.

### Return:

- `</>: float`: Returns the result of a calculation to find the coefficient of variation of a set of discrete or continuous data.