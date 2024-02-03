# Advent of Code

This repository collects all input files, solutions, template algorithms, data structures and other supporting information used to solve the [Advent of code](https://adventofcode.com) challenges in different years: 2022, 2023.

## AOC 2023

My goal this year was to solve Advent of Code 2023 using the new programming language [Mojo](https://docs.modular.com/mojo/). Initially I will explore the language basics: variables, data types, control flow, loops, functions, classes?/structs, ownership. In parallel I will be solving the Advent challenges. Normally the first ones are quite easy, scaling in complexity at around challenge 16 or so. We'll see how it goes this year.

## Mojo basics

### Run
You run mojo programs using `mojo filename.mojo`

### Build
Programs can be build using `mojo build filaname.mojo`.

## AOC 2022
I solved every challenge for the year 2022. The code has been categorized in three basic parts: 
- parseInformation function 
- the algorithm
- main function putting eveything together.


### Run
Every solution can be called using the helper function designed to call any given challege (one or two) for a given day. Here is how it works:

```python
python aoc2022.py day.challenge_number type
```

Where:
-   `day`:  the respective day of the challenge
-   `challenge_number`: the challenge number for the day, can be `1` or `2`
-   `type`: there are two types of calls, `test` to call the test and `main` to execute the main challenge problem

For example:
```python
python aoc2022.py 1.1 test
```
This instruction will execute the `test` problem of day `1`, challenge `1`.
