# import os

def calculate(h, w):                      # calculating BMI = weight (kg) / height (m)^2
    result = round(w / ((h/100) ** 2), 2) # based on formula from https://www.cdc.gov/bmi/about/index.html
    return result
    
def ask(value, unit):
    while True:
        try:
            value = int(input(f"Enter your {value} (in {unit}): "))
            return value
            break # Exit the loop if input is valid
        except ValueError:
            print("Invalid input! Please enter a valid integer.")

def calculator():           

    # ask user input
    height = ask("height", "cm")
    weight = ask("weight", "kg")
    bmi = calculate(height, weight)

    if bmi < 18.5:                      # BMI calculations based on adult categories
        bmi_category = "Underweight"    # https://www.cdc.gov/bmi/adult-calculator/bmi-categories.html
    elif bmi < 25:
        bmi_category = "Healthy"
    elif bmi < 30:
        bmi_category = "Overweight"
    else:
        bmi_category = "Obese"

    # result
    print(f'''
You are {height} cm and weigh {weight} kg.
Body Mass Index: {bmi}
BMI Category: {bmi_category}
''')

# clear_screen()

if __name__ == "__main__":
    print(f"Welcome to the BMI Calculator!\n")
    while True:
        calculator()
        condition = input(f'''1 to try again
or just press ENTER to exit.
''')
        if condition == "":
            break
        elif condition == "1":
            continue
