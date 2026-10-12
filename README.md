# BMI Calculator

A simple **BMI (Body Mass Index) Calculator** written in Python.

This is my first Python project, created as a practical way to learn Python fundamentals while helping me keep track of my own and my family's health measurements.

## Features

* Calculates BMI using height and weight.
* Accepts height in centimeters (cm).
* Accepts weight in kilograms (kg).
* Rounds the BMI result to 2 decimal places.
* Categorizes BMI into Underweight, Healthy, Overweight, and Obese.
* Validates user input to handle invalid entries.
* Allows repeated calculations without restarting the program.
* Displays height, weight, calculated BMI, and BMI category.

## How It Works

The program calculates BMI using the following formula:

**BMI = weight (kg) / height (m)²**

Since the program accepts height in centimeters, it converts the measurement to meters before calculating BMI.

For more information, see the [CDC's official explanation of BMI and its formula](https://www.cdc.gov/bmi/about/index.html).

The calculation is implemented in the `calculate()` function:

```python
def calculate(h, w):
    result = round(w / ((h / 100) ** 2), 2)
    return result
```

### BMI Categories

The program classifies BMI using the following adult BMI categories:

| BMI              | Category    |
| ---------------- | ----------- |
| Below 18.5       | Underweight |
| 18.5 to below 25 | Healthy     |
| 25 to below 30   | Overweight  |
| 30 or above      | Obese       |

**Reference:** [CDC - Adult BMI Categories](https://www.cdc.gov/bmi/adult-calculator/bmi-categories.html)

> **Important:** These categories are intended for adults aged 20 and older. Children and teenagers require a different assessment based on age and sex. BMI is a screening tool, not a complete assessment of health.

## Program Flow

When the program starts, it displays a welcome message and begins the calculator.

### Example Output

```text
Welcome to the BMI Calculator!

Enter your height (in cm): 170
Enter your weight (in kg): 60

You are 170 cm and weigh 60 kg.
Body Mass Index: 20.76
BMI Category: Healthy
```

After displaying the result, the program asks whether the user wants to calculate another BMI.

```text
1 to try again
or just press ENTER to exit.
```

* Entering `1` starts another calculation.
* Pressing `ENTER` exits the program.

## Input Validation

The program uses the `ask()` function to request input until the user enters a valid integer.

```python
def ask(value, unit):
    while True:
        try:
            value = int(input(f"Enter your {value} (in {unit}): "))
            return value
        except ValueError:
            print("Invalid input! Please enter a valid integer.")
```

If the user enters something that cannot be converted into an integer, Python raises a `ValueError`. The program catches the error and asks the user to try again.

For example:

```text
Enter your height (in cm): abc
Invalid input! Please enter a valid integer.
Enter your height (in cm): 170
```

This prevents certain invalid inputs from crashing the program. However, the current implementation does not validate whether height and weight are positive or within a realistic range.

## Python Concepts Practiced

This project helped me practice several fundamental Python concepts.

### 1. Functions

The program is divided into three main functions:

* `calculate()` calculates BMI.
* `ask()` handles user input and validation.
* `calculator()` manages one complete BMI calculation.

### 2. User Input and Type Conversion

The `input()` function collects information from the user, while `int()` converts the input into an integer.

### 3. Exception Handling

The `try` and `except` statements handle invalid integer input using `ValueError`.

### 4. While Loops

The program uses `while True` loops to repeatedly request valid input and allow multiple calculations.

### 5. Conditional Statements

The `if`, `elif`, and `else` statements determine the BMI category based on the calculated result.

### 6. F-Strings

F-strings allow variables to be inserted directly into strings, making it easier to display results.

### 7. The `__name__ == "__main__"` Pattern

The program uses:

```python
if __name__ == "__main__":
```

This ensures that the main calculator loop runs when the file is executed directly. It is a common Python convention that also allows the file to be imported as a module without automatically starting the calculator.

## Project Structure

The project currently consists of one Python file:

```text
BMI-Calculator/
└── bmi.py
```

### `bmi.py`

Contains the complete program, including BMI calculation, input validation, categorization, result display, and the main program loop.

## Requirements

* Python 3.x
* No external libraries required.

The program uses Python's built-in functionality.

## How to Run

1. Clone or download this repository.
2. Open a terminal in the project directory.
3. Run the following command:

```bash
python bmi.py
```

Depending on your system, you may need to use:

```bash
python3 bmi.py
```

The calculator will start in the terminal.

## Example Calculation

For a person who is 175 cm tall and weighs 70 kg:

```text
BMI = 70 / (1.75)²
BMI = 22.86
```

The program displays:

```text
You are 175 cm and weigh 70 kg.
Body Mass Index: 22.86
BMI Category: Healthy
```

## Limitations

The current version has several limitations:

* Only accepts integer values for height and weight.
* Does not save measurements after the program closes.
* Does not maintain a history of measurements.
* Does not support multiple family member profiles.
* Does not validate realistic height and weight ranges.
* Uses adult BMI categories, which are not appropriate for assessing children and teenagers.
* Runs entirely in the terminal without a graphical user interface.

Additionally, BMI does not directly measure body fat or provide a complete picture of someone's health. Other factors, such as medical history, physical activity, and body composition, are also important.

For further information, see the [CDC's explanation of BMI and its limitations](https://www.cdc.gov/bmi/about/index.html).

## Future Improvements

Possible improvements include:

* Allow decimal values for height and weight.
* Create profiles for individual family members.
* Save measurements to a file or database.
* Record the date of each measurement.
* Track changes over time.
* Visualize measurement history using charts.
* Add a graphical user interface.
* Improve input validation.
* Expand the application with additional health-tracking features.

## References

The following official CDC resources were used as references for the BMI formula and categories implemented in this project.

1. [About Body Mass Index (BMI) - CDC](https://www.cdc.gov/bmi/about/index.html)
   Explains BMI, its calculation, and its use as a screening tool.

2. [Adult BMI Categories - CDC](https://www.cdc.gov/bmi/adult-calculator/bmi-categories.html)
   Defines adult BMI categories and their corresponding numerical ranges.

3. [Adult BMI Calculator - CDC](https://www.cdc.gov/bmi/adult-calculator/)
   Provides an official calculator for adults aged 20 and older.

## Disclaimer

This project is intended for educational and personal tracking purposes. It is not a medical diagnostic tool.

BMI should be interpreted alongside other relevant health information. For children and teenagers, use an age-appropriate assessment rather than adult BMI categories.
