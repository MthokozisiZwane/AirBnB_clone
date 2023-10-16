import unittest
from models.base_model import BaseModel
from datetime import datetime
import json

class TestBaseModel(unittest.TestCase):
    def test_init(self):
        # Test the initialization of the BaseModel instance
        obj = BaseModel()
        self.assertIsInstance(obj, BaseModel)
        self.assertIsInstance(obj.id, str)
        self.assertIsInstance(obj.created_at, datetime)
        self.assertIsInstance(obj.updated_at, datetime)

    def test_str(self):
        # Test the __str__ method
        obj = BaseModel()
        expected_str = f"[BaseModel] ({obj.id}) {obj.__dict__}"
        self.assertEqual(str(obj), expected_str)

    def test_save(self):
        # Test the save method
        obj = BaseModel()
        original_updated_at = obj.updated_at
        obj.save()
        self.assertNotEqual(obj.updated_at, original_updated_at)

    def test_to_dict(self):
        # Test the to_dict method
        obj = BaseModel()
        obj_dict = obj.to_dict()
        self.assertIsInstance(obj_dict, dict)
        self.assertEqual(obj_dict['id'], obj.id)
        self.assertEqual(obj_dict['created_at'], obj.created_at.isoformat())
        self.assertEqual(obj_dict['updated_at'], obj.updated_at.isoformat())
        self.assertEqual(obj_dict['__class__'], 'BaseModel')

    def test_to_dict_serialization(self):
        # Test serialization of BaseModel to_dict to JSON
        obj = BaseModel()
        obj_dict = obj.to_dict()
        obj_json = json.dumps(obj_dict)
        self.assertIsInstance(obj_json, str)

    def test_reload(self):
        # Test reloading from a dictionary
        obj = BaseModel()
        obj_dict = obj.to_dict()

        new_obj = BaseModel(**obj_dict)
        self.assertEqual(obj.id, new_obj.id)
        self.assertEqual(obj.created_at, new_obj.created_at)
        self.assertEqual(obj.updated_at, new_obj.updated_at)

if __name__ == '__main__':
    unittest.main()
