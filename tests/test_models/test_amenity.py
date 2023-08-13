#!/usr/bin/python3
"""
Unittest module for Amenity class
"""

import unittest
import pep8
import os
from models.amenity import Amenity


class TestAmenity(unittest.TestCase):
    """Comprehensive Unittest for the class Amenity"""

    def test_docstring(self):
        """Checks for docstring"""
        self.assertTrue(len(Amenity.__doc__) > 1)
        self.assertTrue(len(Amenity.__init__.__doc__) > 1)
        self.assertTrue(len(Amenity.__str__.__doc__) > 1)
        self.assertTrue(len(Amenity.save.__doc__) > 1)
        self.assertTrue(len(Amenity.to_dict.__doc__) > 1)

    def test_pep8(self):
        """test pep8 comes back clean"""
        style = pep8.StyleGuide(quiet=True)
        result = style.check_files(['models/amenity.py'])
        self.assertEqual(result.total_errors, 0, "fix pep8")

    def setUp(self):
        """Setup test"""
        pass

    def tearDown(self):
        """Resets tests"""
        try:
            os.remove("file.json")
        except:
            pass

    def test_object_instantiation(self):
        """Instantiates class"""
        self.amenity = Amenity()

    def test_attributes(self):
        """Test Class: Amenity attributes"""
        self.amenity = Amenity()
        self.assertTrue(hasattr(self.amenity, "created_at"))
        self.assertTrue(hasattr(self.amenity, "updated_at"))
        self.assertFalse(hasattr(self.amenity, "random_attr"))
        self.assertTrue(hasattr(self.amenity, "name"))
        self.assertTrue(hasattr(self.amenity, "id"))
        self.assertEqual(self.amenity.__class__.__name__, "Amenity")

    def test_save_method(self):
        """Testing method: save"""
        self.amenity = Amenity()
        self.amenity.save()
        self.assertTrue(hasattr(self.amenity, "updated_at"))

    def test_to_dict_method(self):
        """Testing method: to_dict"""
        self.amenity = Amenity()
        self.assertTrue(hasattr(self.amenity, "to_dict"))
        self.assertTrue(isinstance(self.amenity.to_dict(), dict))

    def test_str_method(self):
        """Testing __str__ return format of Amenity"""
        self.amenity = Amenity()
        s = "[{}] ({}) {}".format(self.amenity.__class__.__name__,
                                  str(self.amenity.id), self.amenity.__dict__)
        self.assertEqual(print(s), print(self.amenity))

    def test_init_arg(self):
        """Pass in arg to new instance"""
        b1 = Amenity(23)
        self.assertEqual(type(b1).__name__, "Amenity")
        self.assertFalse(hasattr(b1, "23"))

    def test_init_kwarg(self):
        """Pass kwargs into the instance"""
        b1 = Amenity(name="AC")
        self.assertEqual(type(b1).__name__, "Amenity")
        self.assertTrue(hasattr(b1, "name"))
        self.assertFalse(hasattr(b1, "id"))
        self.assertFalse(hasattr(b1, "created_at"))
        self.assertFalse(hasattr(b1, "updated_at"))
        self.assertTrue(hasattr(b1, "__class__"))

    def test_before_todict(self):
        """Tests instances before using to_dict conversion"""
        b1 = Amenity()
        b1_dict = b1.__dict__
        self.assertEqual(type(b1).__name__, "Amenity")
        self.assertTrue(hasattr(b1, '__class__'))
        self.assertEqual(str(b1.__class__),
                         "<class 'models.amenity.Amenity'>")
        self.assertTrue(type(b1_dict['created_at']), 'datetime.datetime')
        self.assertTrue(type(b1_dict['updated_at']), 'datetime.datetime')
        self.assertTrue(type(b1_dict['id']), 'str')

    def test_after_todict(self):
        """Test instances after using to_dict conversion"""
        my_model = Amenity()
        new_model = Amenity()
        test_dict = my_model.to_dict()
        self.assertIsInstance(my_model, Amenity)
        self.assertEqual(type(my_model).__name__, "Amenity")
        self.assertEqual(test_dict['__class__'], "Amenity")
        self.assertTrue(type(test_dict['__class__']), 'str')
        self.assertTrue(type(test_dict['created_at']), 'str')
        self.assertTrue(type(test_dict['updated_at']), 'str')
        self.assertTrue(type(test_dict['id']), 'str')
        self.assertNotEqual(my_model.id, new_model.id)

    def test_hasattribute(self):
        """Tests if the instance of BaseModel has been correctly made"""
        b1 = Amenity()
        self.assertTrue(hasattr(b1, "__init__"))
        self.assertTrue(hasattr(b1, "created_at"))
        self.assertTrue(hasattr(b1, "updated_at"))
        self.assertTrue(hasattr(b1, "id"))


if __name__ == '__main__':
    unittest.main()
