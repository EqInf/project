# Daily Calorie & Macronutrient Calculator
### Video DEMO:
## Description:
### Overview:

A Python-based application called the Daily Calorie & Macronutrient Calculator assists users in figuring out their Total Daily Energy Expenditure (TDEE) and the best way to break down the macronutrients—protein, carbs, and fats in order to achieve their fitness objectives. Users are given a customized calorie and macronutrient consumption suggestion by entering basic personal information such as weight, height, age, gender, exercise level, and intended fitness objective.

Those who wish to increase, maintain, or decrease their weight while making sure they eat the proper ratio of macronutrients will find this tool helpful. The project uses existing activity multipliers for TDEE estimation and industry-standard formulae such as the Mifflin-St Jeor Equation for BMR (Basal Metabolic Rate) calculation.

### Files and Their Purpose

The project consists of the following key files:

#### ```project.py```

This file contains the main program logic and function definitions. It includes:

* ```calculate_bmr(weight_kg, height_cm, age, gender)```: Computes the Basal Metabolic Rate (BMR) using the Mifflin-St Jeor Equation.

* ```calculate_tdee(bmr, activity_level)```: Calculates Total Daily Energy Expenditure (TDEE) based on activity level multipliers.

* ```macronutrient_distribution(tdee, goal)```: Determines daily calorie intake and macronutrient distribution (protein, carbs, fats) based on the selected goal (gain, maintain, or lose weight).

* ```main()```: A function that interacts with the user, takes inputs, calls other functions to perform calculations, and prints the results in a structured format.

#### ```test_project.py```

This file contains unit tests written using pytest to verify the correctness of the three key functions in project.py. It includes:

* ```test_calculate_bmr()```: Tests different cases of BMR calculations to ensure accuracy.

* ```test_calculate_tdee()```: Validates TDEE calculations using various activity levels.

* ```test_macronutrient_distribution()```: Ensures that calorie and macronutrient breakdown calculations produce expected results.

#### ```requirements.txt```

This file lists the external dependencies required to run the project. In this case, it contains:

* ```pytest```: Required for running the test cases.

#### ```README.md```

This file (the one you are currently reading) serves as documentation for the project. It provides an overview, explains the functionality of each file, and describes key design choices.

### Design Choises and Consideration

#### Why the Mifflin-St Jeor Equation?

The Mifflin-St Jeor Equation is widely regarded as one of the most accurate BMR estimation formulas. Other equations, such as the Harris-Benedict equation, exist but tend to be slightly outdated or less precise. Since this project focuses on providing accurate calorie recommendations, Mifflin-St Jeor was the best choice.

#### Activity Level Multipliers

We used standard multipliers to estimate TDEE based on activity level:

* Sedentary (little to no exercise): 1.2

* Lightly active (light exercise 1–3 days/week): 1.375

* Moderately active (moderate exercise 3–5 days/week): 1.55

* Very active (hard exercise 6–7 days/week): 1.725

* Extremely active (very intense daily exercise): 1.9

These multipliers are widely used in fitness communities and provide reasonable approximations of daily calorie needs.

#### Macronutrient Split Choices

For macronutrient distribution, we chose the following breakdown based on common dietary recommendations:

* Protein: 30% of daily calories (4 kcal per gram)

* Carbohydrates: 50% of daily calories (4 kcal per gram)

* Fats: 20% of daily calories (9 kcal per gram)

This split is commonly used in balanced meal plans and ensures sufficient protein intake while keeping fats and carbohydrates at reasonable levels.

#### Why pytest?

The pytest framework was used for testing because:

* It provides a clean and structured way to write unit tests.

* It allows automatic test discovery and informative failure messages.

* It is widely used in professional software development.

### How to Run the Project

#### 1. Set Up the Virtual Environment

It is recommended to use a virtual environment to keep dependencies organized:

```python -m venv venv```

Activate it:

* Windows: ```venv\Scripts\activate```

* Mac/Linux: ```source venv/bin/activate```

#### 2. Install Dependencies

```pip install -r requirements.txt```

#### 3. Run the Program

To execute the calorie calculator:

```python project.py```

Follow the on-screen prompts to input your details and receive personalized recommendations.

#### 4. Run Tests

To verify correctness using pytest:

```pytest test_project.py```

All tests should pass successfully.

### Conclusion

For anyone trying to control their caloric intake according to their goals and lifestyle, this project is an easy-to-use yet powerful tool. This tool offers a helpful and realistic method of monitoring dietary requirements by combining organized macronutrient recommendations, standard activity multipliers, and scientifically confirmed formulas.

The project is easily extendable; future improvements could include:

* Adding more precise activity level options (e.g., differentiating between strength training and cardio).

* Allowing users to select different macronutrient ratios (e.g., ketogenic, high-carb, etc.).

* Implementing a graphical user interface (GUI) for a more user-friendly experience.

