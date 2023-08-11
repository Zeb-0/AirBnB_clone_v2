#!/usr/bin/python3
"""A unit test module for the console (command interpreter).
"""

import unittest
from unittest.mock import patch
from console import HBNBCommand
from io import StringIO
import sys
import os

class TestHBNBCommand(unittest.TestCase):
    def test_quit(self):
        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            HBNBCommand().onecmd("quit")
            self.assertEqual(mock_stdout.getvalue().strip(), "")

    def test_EOF(self):
        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            HBNBCommand().onecmd("EOF")
            self.assertEqual(mock_stdout.getvalue().strip(), "")

    def test_emptyline(self):
        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            HBNBCommand().onecmd("")
            self.assertEqual(mock_stdout.getvalue().strip(), "")

    def test_create(self):
        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            HBNBCommand().onecmd("create BaseModel")
            self.assertTrue(len(mock_stdout.getvalue().strip()) == 36)

    def test_show(self):
        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            HBNBCommand().onecmd("create BaseModel")
            obj_id = mock_stdout.getvalue().strip()
            HBNBCommand().onecmd(f"show BaseModel {obj_id}")
            expected_output = f"[BaseModel] ({obj_id}) "
            self.assertEqual(mock_stdout.getvalue().strip(), expected_output)

    def test_destroy(self):
        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            HBNBCommand().onecmd("create BaseModel")
            obj_id = mock_stdout.getvalue().strip()
            HBNBCommand().onecmd(f"destroy BaseModel {obj_id}")
            self.assertTrue(len(mock_stdout.getvalue().strip()) == 0)

    def test_all(self):
        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            HBNBCommand().onecmd("create BaseModel")
            HBNBCommand().onecmd("create User")
            HBNBCommand().onecmd("all")
            self.assertTrue("BaseModel" in mock_stdout.getvalue().strip())
            self.assertTrue("User" in mock_stdout.getvalue().strip())

    def test_update(self):
        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            HBNBCommand().onecmd("create BaseModel")
            obj_id = mock_stdout.getvalue().strip()
            HBNBCommand().onecmd(f"update BaseModel {obj_id} name 'New Name'")
            HBNBCommand().onecmd(f"show BaseModel {obj_id}")
            expected_output = f"[BaseModel] ({obj_id}) {{'name': 'New Name'}}"
            self.assertEqual(mock_stdout.getvalue().strip(), expected_output)

if __name__ == '__main__':
    unittest.main()
