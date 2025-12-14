# Advent of Code

This repository collects all input files, solutions, template algorithms, data structures and other supporting information used to solve the [Advent of code](https://adventofcode.com) challenges in different years: 2022, 2023, 2015 (12/24 so far), 2024 (7/24). A generic script was written to run tests and main problem for a given year, day and challenge.

## Run script

Every solution can be called using the helper function designed to call any given challege (one or two) for a given day and year. Here is how it works:

```python
python aoc.py year.day.challenge_number type
```

Where:

- `year`: the year of the challenge
- `day`: the respective day of the challenge
- `challenge_number`: the challenge number for the day, can be `1` or `2`
- `type`: there are two types of calls, `test` to call the test and `main` to execute the main challenge problem

For example:

```python
python aoc.py 2022.1.1 test
```

This instruction will execute the `test` problem of day `1`, challenge `1` of year `2022`.

### tests

One or more tests can be added and specified for each particular challenge at the main execution section of the challenge's file. For more information, explore the utils file, `performTests` function.

## AOC 2024

This year's challenges will be solved in Python again.

### Initial goal

Maybe along the way I will give Mojo or Zig a try. My goal is to solve the challenges of 2024, one day at a time. I will also review concepts from algorithms and data structures. Goal is to keep improving in the art of coding.

### Update: Feb 5th, 2025

I have been working on my old Todo app written in React, with a Django backend. It has been fun, using the new AI systems at the same time. I stopped working on the challenges since a week ago but will continue. I have been using Python, my favorite programming language. It is always easy to come back and write code with easy in it.

## AOC 2023

Solved every challenge for the year 2023. The code has been categorized in three basic parts:

- parseInformation function
- the algorithm
- main function putting eveything together.

### Initial goal

My goal this year was to solve Advent of Code 2023 using the new programming language [Mojo](https://docs.modular.com/mojo/). Initially I will explore the language basics: variables, data types, control flow, loops, functions, classes?/structs, ownership. In parallel I will be solving the Advent challenges. Normally the first ones are quite easy, scaling in complexity at around challenge 16 or so. We'll see how it goes this year.

### Mojo basics

#### Run

You run mojo programs using `mojo filename.mojo`

#### Build

Programs can be build using `mojo build filaname.mojo`.

## AOC 2022

I solved every challenge for the year 2022. The code has been categorized in three basic parts:

- parseInformation function
- the algorithm
- main function putting eveything together.

### Go basics

I started learning the programming language Go. It is a typed, compiled programming language developed by Google. It was design with conconcurrency in mind. It is widely used in web development as a backend language and has a special place in the world of cloud computing.Its performance is superior to interpreted languages such as Python, Ruby or Javascript.
First program of the AOC 2022 challenge was written in Go. More programs will be written in Go in the future.

## AOC 2015

Started to solve challenge from Advent Of Code 2015. 12 problems have been solved so far. Problem 13 in progress. Goal is to complete 2015. Then 2024 and move to the latest challenge, 2025.

### Solutions

Each solution is categorized in three basic parts:

- parseInformation function
- the algorithm
- main function putting eveything together.

Using the same solution structure used in previous challenges. Python is the main programming language being used in this challenge.
