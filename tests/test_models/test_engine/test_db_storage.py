#!/usr/bin/python3
"""Test file for testing database"""

from models.engine.db_storage import DBStorage
import os
import unittest


@unittest.skipIf(
    os.getenv("HBNB_TYPE_STORAGE") != "db",
    "Test is not relevant for DBStorage"
)
class test_DB_Storage(unittest.TestCase):
    """test database storage"""

    def test_documentation(self):
        """testing database document"""
        self.assertIsNot(DBStorage.__doc__, None)
