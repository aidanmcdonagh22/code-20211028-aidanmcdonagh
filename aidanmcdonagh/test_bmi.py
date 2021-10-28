from django.test import TestCase
from .bmi import calculateBMI

class TestBMI(TestCase):
    def setUp(self):
        self.test_dataset1 = [
            { "Gender": "Male", "HeightCm": 171, "WeightKg": 96 },
            { "Gender": "Male", "HeightCm": 161, "WeightKg": 85 },
            { "Gender": "Male", "HeightCm": 180, "WeightKg": 77 },
            { "Gender": "Female", "HeightCm": 166, "WeightKg": 62 },
            { "Gender": "Female", "HeightCm": 150, "WeightKg": 70 },
            { "Gender": "Female", "HeightCm": 167, "WeightKg": 82 }
        ]
    
    def test_calculate_bmi(self):
        new_data, overweight_count = calculateBMI(self.test_dataset1)

        for x in new_data:
            self.assertIsNotNone(x["BMI"])
            self.assertIsNotNone(x["BMI Category"])
            self.assertIsNotNone(x["Health Risk"])
        
        # Test BMI
        # BMI = mass (kg) / height (m^2)
        self.assertEqual(new_data[0]["BMI"], 32.83)
        self.assertEqual(new_data[1]["BMI"], 32.79)
        self.assertEqual(new_data[2]["BMI"], 23.77)
        self.assertEqual(new_data[3]["BMI"], 22.50)
        self.assertEqual(new_data[4]["BMI"], 31.11)
        self.assertEqual(new_data[5]["BMI"], 29.40)

        # Test BMI Category
        self.assertEqual(new_data[0]["BMI Category"], "Moderately obese")
        self.assertEqual(new_data[1]["BMI Category"], "Moderately obese")
        self.assertEqual(new_data[2]["BMI Category"], "Normal weight")
        self.assertEqual(new_data[3]["BMI Category"], "Normal weight")
        self.assertEqual(new_data[4]["BMI Category"], "Moderately obese")
        self.assertEqual(new_data[5]["BMI Category"], "Overweight")

        # Test Health Risk
        self.assertEqual(new_data[0]["Health Risk"], "Medium Risk")
        self.assertEqual(new_data[1]["Health Risk"], "Medium Risk")
        self.assertEqual(new_data[2]["Health Risk"], "Low Risk")
        self.assertEqual(new_data[3]["Health Risk"], "Low Risk")
        self.assertEqual(new_data[4]["Health Risk"], "Medium Risk")
        self.assertEqual(new_data[5]["Health Risk"], "Enhanced Risk")

        # Test Overweight
        self.assertEqual(overweight_count, 4)

