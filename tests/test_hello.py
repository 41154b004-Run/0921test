import unittest
import sys
import os

# 確保可以匯入上一層目錄的 hello 模組
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from hello import calculate_bmi, get_bmi_category

class TestBMICalculator(unittest.TestCase):
    def test_calculate_bmi(self):
        # 175cm, 70kg -> 70 / (1.75^2) = 22.857...
        bmi = calculate_bmi(175, 70)
        self.assertAlmostEqual(bmi, 22.86, places=2)

    def test_bmi_categories(self):
        self.assertIn("過輕", get_bmi_category(18.0))
        self.assertIn("健康體位", get_bmi_category(22.0))
        self.assertIn("過重", get_bmi_category(25.0))
        self.assertIn("肥胖", get_bmi_category(30.0))

if __name__ == '__main__':
    unittest.main()
