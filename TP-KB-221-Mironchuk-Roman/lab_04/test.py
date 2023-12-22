import unittest
from Calculator import infix_to_postfix, evaluate_postfix

class TestCalculatorFunctions(unittest.TestCase):
    def test_infix_to_postfix(self):
        self.assertEqual(infix_to_postfix("3+5*2"), "352*+")
        self.assertEqual(infix_to_postfix("(3+5)*2"), "35+2*")
        self.assertEqual(infix_to_postfix("3^2*5"), "322*5^*")
        self.assertEqual(infix_to_postfix("7*(3+5)-6/2"), "735+*62/-")

    def test_evaluate_postfix(self):
        self.assertEqual(evaluate_postfix("352*+"), 13.0)
        self.assertEqual(evaluate_postfix("35+2*"), 16.0)
        self.assertEqual(evaluate_postfix("322*5^*"), 45.0)
        self.assertEqual(evaluate_postfix("735+*62/-"), 38.0)

if __name__ == '__main__':
    unittest.main()
