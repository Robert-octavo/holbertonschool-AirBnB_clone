#!/usr/bin/python3
""" Module of Unittests """
import unittest
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
from models import storage
import os
import json


class FileStorageTests(unittest.TestCase):
    """ Suite of File Storage Tests """

    basemodel = BaseModel()

    def testClassInstance(self):
        """ Check instance """
        self.assertIsInstance(storage, FileStorage)

    def testStoreBaseModel(self):
        """ Test save and reload functions """
        self.basemodel.full_name = "BaseModel Instance"
        self.basemodel.save()
        basemodel_dict = self.basemodel.to_dict()
        all_objs = storage.all()

        key = basemodel_dict['__class__'] + "." + basemodel_dict['id']
        self.assertEqual(key in all_objs, True)

    def testStoreBaseModel2(self):
        """ Test save, reload and update functions """
        self.basemodel.my_name = "First name"
        self.basemodel.save()
        basemodel_dict = self.basemodel.to_dict()

        key = basemodel_dict['__class__'] + "." + basemodel_dict['id']

        self.assertEqual(key in storage.all(), True)
        self.assertEqual(basemodel_dict['my_name'], "First name")

        create1 = basemodel_dict['created_at']
        update1 = basemodel_dict['updated_at']

        self.basemodel.my_name = "Second name"
        self.basemodel.save()
        basemodel_dict = self.basemodel.to_dict()

        self.assertEqual(key in storage.all(), True)

        create2 = basemodel_dict['created_at']
        update2 = basemodel_dict['updated_at']

        self.assertEqual(create1, create2)
        self.assertNotEqual(update1, update2)
        self.assertEqual(basemodel_dict['my_name'], "Second name")

    def testHasAttributes(self):
        """verify if attributes exist"""
        self.assertEqual(hasattr(FileStorage, '_FileStorage__file_path'), True)
        self.assertEqual(hasattr(FileStorage, '_FileStorage__objects'), True)

    def testsave(self):
        """verify if JSON exists"""
        self.basemodel.save()
        self.assertEqual(os.path.exists(storage._FileStorage__file_path), True)
        self.assertEqual(storage.all(), storage._FileStorage__objects)

    def testreload(self):
        """test reload """
        self.basemodel.save()
        self.assertEqual(os.path.exists(storage._FileStorage__file_path), True)
        dobj = storage.all()
        FileStorage._FileStorage__objects = {}
        self.assertNotEqual(dobj, FileStorage._FileStorage__objects)
        storage.reload()
        for key, value in storage.all().items():
            self.assertEqual(dobj[key].to_dict(), value.to_dict())

    def testSaveSelf(self):
        """ Check save self """
        msg = "save() takes 1 positional argument but 2 were given"
        with self.assertRaises(TypeError) as e:
            FileStorage.save(self, 100)

        self.assertEqual(str(e.exception), msg)

    def test_save_FileStorage(self):
        """ Test if 'new' method is working good """
        var1 = self.basemodel.to_dict()
        new_key = var1['__class__'] + "." + var1['id']
        storage.save()
        with open("file.json", 'r') as fd:
            var2 = json.load(fd)
        new = var2[new_key]
        for key in new:
            self.assertEqual(var1[key], new[key])

if __name__ == '__main__':
    unittest.main()
