import math

def calculate_bmr(weight_kg: float, height_cm: float, age: int, gender: str) -> float: #This line was suggested by ChatGPT
    """
    Calculate Basal Metabolic Rate (BMR) using the Mifflin-St Jeor Equation.
    """
    if gender.lower() == "male":
        return 10 * weight_kg + 6.25 * height_cm - 5 * age + 5
    elif gender.lower() == "female":
        return 10 * weight_kg + 6.25 * height_cm - 5 * age - 161
    else:
        raise ValueError("Gender must be 'male' or 'female'")

def calculate_tdee(bmr: float, activity_level: str) -> float:
    """
    Calculate Total Daily Energy Expenditure (TDEE) based on activity level.
    """
    #Whole function "activity multipliers" was suggested by ChatGPT
    activity_multipliers = {
        "sedentary": 1.2,
        "light": 1.375,
        "moderate": 1.55,
        "active": 1.725,
        "very active": 1.9
    }
    
    if activity_level.lower() not in activity_multipliers:
        raise ValueError("Invalid activity level. Choose from sedentary, light, moderate, active, very active.")
    
    return bmr * activity_multipliers[activity_level.lower()]

def macronutrient_distribution(tdee: float, goal: str) -> dict:
    """
    Determine daily macronutrient breakdown based on fitness goal (gain, maintain, lose weight).
    """
    goals = {
        "gain": 1.2,  # 20% surplus
        "maintain": 1.0,
        "lose": 0.8   # 20% deficit
    }
    
    if goal.lower() not in goals:
        raise ValueError("Invalid goal. Choose from gain, maintain, lose.")
    
    target_calories = tdee * goals[goal.lower()]
    
    # 90% of the logic bellow was discovered through ChatGPT 
    macros = {
        "protein": math.ceil((target_calories * 0.3) / 4),  # 30% calories from protein (4 cal per gram)
        "carbs": math.ceil((target_calories * 0.5) / 4),   # 50% calories from carbs (4 cal per gram)
        "fats": math.ceil((target_calories * 0.2) / 9)     # 20% calories from fats (9 cal per gram)
    }
    return {"calories": math.ceil(target_calories), **macros}

def main():
    """
    Main function to interact with the user and calculate personalized nutritional needs.
    """
    print("Welcome to the Daily Calorie & Macronutrient Calculator!")
    weight = float(input("Enter your weight in kg: "))
    height = float(input("Enter your height in cm: "))
    age = int(input("Enter your age: "))
    gender = input("Enter your gender (male/female): ")
    activity = input("Enter your activity level (sedentary, light, moderate, active, very active): ")
    goal = input("Enter your fitness goal (gain, maintain, lose): ")
    
    bmr = calculate_bmr(weight, height, age, gender)
    tdee = calculate_tdee(bmr, activity)
    macros = macronutrient_distribution(tdee, goal)
    
    print(f"\nYour Total Daily Energy Expenditure (TDEE): {math.ceil(tdee)} kcal")
    print("Macronutrient Breakdown:")
    print(f"- Protein: {macros['protein']}g")
    print(f"- Carbs: {macros['carbs']}g")
    print(f"- Fats: {macros['fats']}g")

if __name__ == "__main__":
    main()
