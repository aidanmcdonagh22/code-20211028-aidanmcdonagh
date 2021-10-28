data = [
    { "Gender": "Male", "HeightCm": 171, "WeightKg": 96 },
    { "Gender": "Male", "HeightCm": 161, "WeightKg": 85 },
    { "Gender": "Male", "HeightCm": 180, "WeightKg": 77 },
    { "Gender": "Female", "HeightCm": 166, "WeightKg": 62 },
    { "Gender": "Female", "HeightCm": 150, "WeightKg": 70 },
    { "Gender": "Female", "HeightCm": 167, "WeightKg": 82 }
]

def calculateBMI(data=data):
    overweight = 0

    for i in data:
        mass: int = i["WeightKg"]
        heightCm: int = i["HeightCm"]
        # Calculate BMI
        bmi: float = round(mass / ((heightCm / 100)**2), 2)
        i["BMI"] = bmi
        # Do lookup
        if bmi <= 18.4:
            i["BMI Category"] = "Underweight"
            i["Health Risk"] = "Malnutrition Risk"
        elif 18.5 <= bmi <= 24.9:
            i["BMI Category"] = "Normal weight"
            i["Health Risk"] = "Low Risk"
        elif 25 <= bmi <= 29.9:
            i["BMI Category"] = "Overweight"
            i["Health Risk"] = "Enhanced Risk"
            overweight += 1
        elif 30 <= bmi <= 34.9:
            i["BMI Category"] = "Moderately obese"
            i["Health Risk"] = "Medium Risk"
            overweight += 1
        elif 35 <= bmi <= 39.9:
            i["BMI Category"] = "Severely obese"
            i["Health Risk"] = "High Risk"
            overweight += 1
        else:
            i["BMI Category"] = "Very severely obese"
            i["Health Risk"] = "Very high Risk"
            overweight += 1
    
    print(f'data: {data}')
    print(f'overweight: {overweight}')
    return data, overweight
