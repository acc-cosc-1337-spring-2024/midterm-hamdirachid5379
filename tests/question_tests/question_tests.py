#write function tests here, don't add input('') statements here!
import unittest



#follow this example to add questions b, c, and d for testing including their functions
from src.question_a.question_a import  test_config, get_sum_of_evens
from src.question_b.question_b import get_fahrenheit
from question_c.question_c import is_prime
from question_d.question_d import get_bonus_pay_amount


class Test_Config(unittest.TestCase):

    def test_question_a_config(self):
        self.assertEqual(True, test_config())

    def test_get_sum_of_evens(self):
        self.assertEqual(get_sum_of_evens(11), 30)
        self.assertEqual(get_sum_of_evens(10), 30)
        self.assertEqual(get_sum_of_evens(8), 20)

    def test_get_fahrenheit(self):
        self.assertEqual(get_fahrenheit(0), 32)
        self.assertEqual(get_fahrenheit(5), 41)
        self.assertEqual(get_fahrenheit(10), 50)

    def test_is_prime(self):
        self.assertEqual(is_prime(4), True)
        self.assertEqual(is_prime(5), False)
        self.assertEqual(is_prime(11), True)

    def test_get_bonus_pay_amount(self):
        self.assertEqual(get_bonus_pay_amount(-1), "invalid arguments")
        self.assertEqual(get_bonus_pay_amount(200), 10)
        self.assertEqual(get_bonus_pay_amount(600), 36)
        self.assertEqual(get_bonus_pay_amount(1000), 70)
        self.assertEqual(get_bonus_pay_amount(1500), 120)
        self.assertEqual(get_bonus_pay_amount(2000), "invalid arguments")

        
        



