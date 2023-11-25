#!/usr/bin/python3
""" documentation """
from tests.test_models.test_base_model import test_basemodel
from models.user import User


class test_User(test_basemodel):
    """ documentation """

    def __init__(self, *args, **kwargs):
        """ documentation """
        super().__init__(*args, **kwargs)
        self.name = "User"
        self.value = User

    def test_first_name(self):
        """ documentation """
        new = self.value()
        self.assertEqual(type(new.first_name), str)

    def test_last_name(self):
        """ documentation """
        new = self.value()
        self.assertEqual(type(new.last_name), str)

    def test_email(self):
        """ documentation """
        new = self.value()
        self.assertEqual(type(new.email), str)

    def test_password(self):
        """ documentation """
        new = self.value()
        self.assertEqual(type(new.password), str)
