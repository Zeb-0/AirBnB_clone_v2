#!/usr/bin/python3
"""Unittest for Console"""


from console import HBNBCommand
import sys
import unittest
from unittest.mock import create_autospec


class Test_Console(unittest.TestCase):
    """Console Unittest"""

    def setUp(self):
        """Sets up STDIN and STDOUT"""
        self.mock_stdin = create_autospec(sys.stdin)
        self.mock_stdout = create_autospec(sys.stdout)

    def create(self, server=None):
        """Creates HBNBCommand"""
        return HBNBCommand(stdin=self.mock_stdin, stdout=self.mock_stdout)

    def test_quit(self):
        """Tests the quit command"""
        xit = self.create()
        self.assertTrue(xit.onecmd("quit"))
