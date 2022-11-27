import unittest
from models.base_model import BaseModel
class TestBaseModel(unittest.TestCase):
    def test_save(self):
        base_model = BaseModel()
        updated_at = base_model.updated_at
        base_model.save()
        updated_at_now = base_model.updated_at
        self.assertNotEqual(updated_at , updated_at_now)
        
   
