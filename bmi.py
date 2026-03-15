import os
import time
import sys

# to restart
def clear_screen():
    # 'cls' for Windows, 'clear' for Linux/macOS
    os.system('cls' if os.name == 'nt' else 'clear')
    print(f"BMI CALCULATOR v1.1 by AQIL\n") # title

def calculate(h, w):
    result = round(w / ((h/100) ** 2), 2)
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

    if bmi < 18.5:
        bmi_category = "Underweight"
    elif bmi < 25:
        bmi_category = "Healthy Weight"
    elif bmi < 30:
        bmi_category = "Overweight"
    else:
        bmi_category = "Obesity"
        
    for i in range(11):
        # The \r moves the cursor to the start of the line
        print(f"Calculating BMI: {i*10}%", end='\r', flush=True)
        time.sleep(0.1)

    # After the loop, print a final newline to move to the next line
    print("Calculation complete!        ")

    # result
    print(f'''
You are {height} cm tall and have a weight of {weight} kg.
Body Mass Index: {bmi}
BMI Category: {bmi_category}
''')

clear_screen()

while True:
    calculator()
    condition = input(f'''
1 to try again in a new line
2 to try again and clear all 
or just press ENTER to exit.
>>> ''')
    if condition == "":
        break
    elif condition == "1":
        continue
    elif condition == "2":
        clear_screen()
