#!/usr/bin/python3
"""Unit tests for the HBNBCommand class in the console (command interpreter).
"""

import unittest
from unittest.mock import patch
from console import HBNBCommand
from io import StringIO

class TestHBNBCommand(unittest.TestCase):
    def setUp(self):
        self.console = HBNBCommand()

    def tearDown(self):
        pass  # Clean up if needed

    def test_quit(self):
        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            self.console.onecmd("quit")
            self.assertEqual(mock_stdout.getvalue().strip(), "")
    
    def test_EOF(self):
        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            self.console.onecmd("EOF")
            self.assertEqual(mock_stdout.getvalue().strip(), "")

    def test_emptyline(self):
        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            self.console.onecmd("")
            self.assertEqual(mock_stdout.getvalue().strip(), "")

    def test_create(self):
        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            self.console.onecmd("create BaseModel")
            self.assertTrue(len(mock_stdout.getvalue().strip()) == 36)

    def test_destroy(self):
        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            self.console.onecmd("create BaseModel")
            obj_id = mock_stdout.getvalue().strip()
            self.console.onecmd(f"destroy BaseModel {obj_id}")
            self.assertFalse(len(mock_stdout.getvalue().strip()) == 0)

    def test_all(self):
        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            self.console.onecmd("create BaseModel")
            self.console.onecmd("create User")
            self.console.onecmd("all")
            self.assertTrue("BaseModel" in mock_stdout.getvalue().strip())
            self.assertTrue("User" in mock_stdout.getvalue().strip())
    def test_alt_all(self):
        ''' test [class].all method '''
        with patch('sys.stdout', new=StringIO()) as v:
            HBNBCommand().onecmd('create User')
        with patch('sys.stdout', new=StringIO()) as v:
            HBNBCommand().onecmd('User.all()')
            self.assertTrue(len(v.getvalue()) > 0)

    def test_count(self):
        ''' test [class].count method '''
        with patch('sys.stdout', new=StringIO()) as v:
            HBNBCommand().onecmd('User.count()')
            self.assertTrue(int(v.getvalue()) >= 0)
        with patch('sys.stdout', new=StringIO()) as v:
            HBNBCommand().onecmd('create User')
        with patch('sys.stdout', new=StringIO()) as v:
            HBNBCommand().onecmd('User.count()')
            self.assertTrue(int(v.getvalue()) >= 1)

    def test_user(self):
        ''' test user object with console '''
        with patch('sys.stdout', new=StringIO()) as v:
            HBNBCommand().onecmd('create User')
            user_id = v.getvalue()
            self.assertTrue(user_id != "** class doesn't exist **\n")
        with patch('sys.stdout', new=StringIO()) as v:
            HBNBCommand().onecmd('show User')
            self.assertTrue(v.getvalue() != "** no instance found **\n")
        with patch('sys.stdout', new=StringIO()) as v:
            HBNBCommand().onecmd('all User')
            self.assertTrue(v.getvalue() != "** class doesn't exist **\n")
        with patch('sys.stdout', new=StringIO()) as v:
            HBNBCommand().onecmd("update User " + user_id + " name betty")
            HBNBCommand().onecmd("show User " + user_id)
            self.assertTrue("betty" in v.getvalue())
            HBNBCommand().onecmd("destroy User " + user_id)
        with patch('sys.stdout', new=StringIO()) as v:
            HBNBCommand().onecmd("show User "+user_id)
            self.assertEqual(v.getvalue(), "** no instance found **\n")
             
    def test_class_exist(self):
        ''' test class name exist '''
        with patch('sys.stdout', new=StringIO()) as v:
            HBNBCommand().onecmd('create BaseModel')
        with patch('sys.stdout', new=StringIO()) as v:
            HBNBCommand().onecmd('all FakeClass')
            self.assertTrue(v.getvalue() == "** class doesn't exist **\n")

    def test_show_id(self):
        ''' test show id '''
        with patch('sys.stdout', new=StringIO()) as v:
            HBNBCommand().onecmd('show BaseModel')
            self.assertFalse(v.getvalue() == "** instance id missing **")

if __name__ == '__main__':
    unittest.main()
