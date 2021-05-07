import unittest
from python_test import *

class UnitTest(unittest.TestCase):
    def test1(self):
        test1_input = {'can':{'you':{'if':{'code':{'testing': {'with': {'answer': {'to': 'Welcome'}}}}}}}}
        test1_output = {'Welcome':{'to':{'answer':{'with':{'testing': {'code': {'if': {'you': 'can'}}}}}}}}
        self.assertEquals(test_func(test1_input), test1_output)

    def test2(self):
        test2_input = {'us':{'with':{'link':{'share':{'and':{'account':{'GitHub':{'your':{'to':{'push':{'please': {'coding,': {'finish': {'you': 'After'}}}}}}}}}}}}}}
        test2_output = {'After': {'you': {'finish': {'coding,': {'please': {'push': {'to': {'yourr': {'GitHub': {'account': {'and': {'share': {'link': {'with': 'us'}}}}}}}}}}}}}}
        self.assertEquals(test_func(test2_input), test2_output)

    def test3(self):
        test3_input = {'I': {'deserve': {'to': {'be': 'hired'}}}}
        test3_output = {'hired': {'be': {'to': {'deserve': 'I'}}}}
        self.assertEquals(test_func(test3_input), test3_output)


if __name__ == '__main__':
    unittest.main(verbosity=3)