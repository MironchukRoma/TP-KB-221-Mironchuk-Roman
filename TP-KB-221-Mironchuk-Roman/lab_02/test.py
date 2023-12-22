import unittest
from unittest.mock import patch
from io import StringIO
import csv

from lab2 import *

class TestPhoneDirectory(unittest.TestCase):

    def setUp(self):
        # Initialize an empty list before each test
        self.students_list = [
            {"name": "Alina", "phone": "123456789", "age": "25", "city": "Texas"},
            {"name": "Harry", "phone": "123456789", "age": "20", "city": "Los Angeles"},
        ]

    def test_add_new_element(self):
        with patch('builtins.input', side_effect=['Angel', '123456789', '12', 'New York']):
            addNewElement(self.students_list)

        self.assertEqual(self.students_list[2]["name"], "Angel")

    def test_delete_element(self):
        with patch('builtins.input', return_value='Alina'):
            deleteElement(self.students_list)

        self.assertIn('Alina', [student['name'] for student in self.students_list])
        
    def test_update_element(self):
        with patch('builtins.input', side_effect=['Alina', 'NewAlina', '987654321', '23', 'Ukraine']):
            updateElement(self.students_list)

        updated_student_names = [student['name'] for student in self.students_list]
        self.assertIn('Alina', updated_student_names)


    def test_read_from_csv(self):
        csv_filename = 'test_data.csv'
        saveToCSV(csv_filename, self.students_list)
        self.students_list.clear()
        with open(csv_filename, 'a') as file:
            file.write('Invalid Data\n')
        with self.assertRaises(Exception): 
            loaded_students_list = loadFromCSV(csv_filename)

        self.assertEqual(len(self.students_list), 0)


    def tearDown(self):
        # Clean up after each test
        self.students_list.clear()

if __name__ == '__main__':
    unittest.main()