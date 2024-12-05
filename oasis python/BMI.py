def calculate_bmi(weight, height):
    """Calculate BMI and return the BMI value."""
    return weight / (height ** 2)

def classify_bmi(bmi):
    """Classify the BMI into categories."""
    if bmi < 18.5:
        return "Underweight"
    elif 18.5 <= bmi < 24.9:
        return "Normal weight"
    elif 25 <= bmi < 29.9:
        return "Overweight"
    else:
        return "Obesity"

def main():
    """Main function to execute the BMI calculator."""
    print("Welcome to the BMI Calculator!")
    try:
        weight = float(input("Enter your weight in kilograms: "))
        height = float(input("Enter your height in meters: "))
        
        if weight <= 0 or height <= 0:
            print("Error: Weight and height must be positive numbers.")
            return
        
        bmi = calculate_bmi(weight, height)
        category = classify_bmi(bmi)
        
        print(f"\nYour BMI is: {bmi:.2f}")
        print(f"Category: {category}")
    except ValueError:
        print("Error: Please enter valid numerical values for weight and height.")

if __name__ == "__main__":
    main()
