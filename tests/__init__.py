from unittest import TestCase


class BaseTestCase(TestCase):
    DEFAULT_EVENT = {
        "queryStringParameters": None
    }
    DEFAULT_CONTEXT = {}

