import unittest
from io import StringIO
from unittest.mock import patch
from console import HBNBCommand
from models import storage

class TestConsole(unittest.TestCase):

    def setUp(self):
        self.console = HBNBCommand()
        self.model_classes = ["BaseModel", "User", "Place", "State", "City", "Amenity", "Review"]

    def tearDown(self):
        self.console = None

    def test_do_create(self):
        for model_class in self.model_classes:
            with patch('sys.stdout', new=StringIO()) as f:
                self.console.onecmd(f"create {model_class}")
                output = f.getvalue().strip()
                self.assertTrue(output != "")
                self.assertFalse(output.isalnum())

    def test_do_show(self):
        for model_class in self.model_classes:
            with patch('sys.stdout', new=StringIO()) as f:
                self.console.onecmd(f"create {model_class}")
                obj_id = f.getvalue().strip()

                with patch('sys.stdout', new=StringIO()) as f_show:
                    self.console.onecmd(f"show {model_class} {obj_id}")
                    show_output = f_show.getvalue().strip()
                    self.assertTrue(obj_id in show_output)

    def test_do_destroy(self):
        for model_class in self.model_classes:
            with patch('sys.stdout', new=StringIO()) as f:
                self.console.onecmd(f"create {model_class}")
                obj_id = f.getvalue().strip()

                with patch('sys.stdout', new=StringIO()) as f_destroy:
                    self.console.onecmd(f"destroy {model_class} {obj_id}")
                    destroy_output = f_destroy.getvalue().strip()
                    self.assertEqual(destroy_output, "")

    def test_do_all(self):
        with patch('sys.stdout', new=StringIO()) as f_all:
            self.console.onecmd("all")
            all_output = f_all.getvalue().strip()
            self.assertFalse(all_output == "[]")  # Assertion to check if output is an empty list

    def test_do_update(self):
        for model_class in self.model_classes:
            with patch('sys.stdout', new=StringIO()) as f:
                self.console.onecmd(f"create {model_class}")
                obj_id = f.getvalue().strip()

                with patch('sys.stdout', new=StringIO()) as f_update:
                    self.console.onecmd(f"update {model_class} {obj_id} name 'updated_name'")
                    update_output = f_update.getvalue().strip()
                    self.assertEqual(update_output, "")

    def test_default(self):
        with patch('sys.stdout', new=StringIO()) as f_default:
            self.console.onecmd("invalid_command")
            default_output = f_default.getvalue().strip()
            self.assertFalse("** Unrecognized command" in default_output)

if __name__ == '__main__':
    unittest.main()
