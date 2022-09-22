import json
from unittest.mock import patch
from http import HTTPStatus

import pytest

from service_api.api_v1 import get_announcements, create_announcements
from service_api.applications.database import Database
from tests import BaseTestCase


""" Examples of unit tests.
Actually there are should be more cases, however as example I guess this will be enough
"""

MOCK_ITEMS = [
    {"title": "foo", "date": "2013-05-18", "description": "dfoo"},
    {"title": "bar", "date": "2013-05-18", "description": "dbar"},
    {"title": "spam", "date": "2013-05-18", "description": "dspam"},
]


class TestGetAnnouncement(BaseTestCase):

    @patch.object(Database, "scan", return_value={
        "Items": MOCK_ITEMS,
        "LastEvaluatedKey": {"title": "spam", "date": "2013-05-29"}
    })
    def test_successfully_get_announcements_lambda_handler_with_offset(self, db_scan):
        announcements = get_announcements({"queryStringParameters": {"limit": 3}}, {})
        self.assertEqual(announcements["statusCode"], HTTPStatus.OK)
        self.assertEqual(
            announcements["headers"],
            {'Content-Type': 'application/json', 'next_offset': 'eyJ0aXRsZSI6ICJzcGFtIiwgImRhdGUiOiAiMjAxMy0wNS0yOSJ9'}
        )
        self.assertEqual(len(json.loads(announcements["body"])), 3)

    @patch.object(Database, "scan", return_value={
        "Items": MOCK_ITEMS,
    })
    def test_successfully_get_announcements_lambda_handler_without_offset(self, db_scan):
        announcements = get_announcements({"queryStringParameters": {}}, {})
        self.assertEqual(announcements["statusCode"], HTTPStatus.OK)
        self.assertIsNone(announcements["headers"].get("next_offset"))
        self.assertEqual(len(json.loads(announcements["body"])), 3)

    @patch.object(Database, "scan", return_value={
        "Items": [],
    })
    def test_successfully_get_announcements_lambda_handler_empty(self, db_scan):
        announcements = get_announcements({"queryStringParameters": {}}, {})
        self.assertEqual(announcements["statusCode"], HTTPStatus.OK)
        self.assertIsNone(announcements["headers"].get("next_offset"))
        self.assertEqual(len(json.loads(announcements["body"])), 0)

    @patch.object(Database, "scan", return_value=None)
    def test_dynamodb_failed_when_get_announcements(self, db_scan):
        # It should be successfully
        # Because we catch all exception at lambda handler, logging exception
        # and return internal server error status code
        try:
            response = get_announcements({"queryStringParameters": {}}, {})
        except Exception as e:
            pytest.fail(e)
        else:
            self.assertEqual(response["statusCode"], HTTPStatus.INTERNAL_SERVER_ERROR)


class TestCreateAnnouncement(BaseTestCase):

    @patch.object(Database, "put_item", return_value={
        "Items": MOCK_ITEMS[0],
        "LastEvaluatedKey": {"title": "spam", "date": "2013-05-29"}
    })
    def test_successfully_create_item(self, db):
        payload = {"title": "foo", "date": "2013-05-18", "description": "dfoo"}
        announcement = create_announcements({"body": json.dumps(payload)}, {})
        self.assertEqual(
            json.loads(announcement["body"])["title"],
            payload["title"]
        )

    def test_wrong_payload_create_item(self):
        payload = {"wrong": "foo", "date": "2013-05-18", "description": "dfoo"}
        announcement = create_announcements({"body": json.dumps(payload)}, {})
        self.assertEqual(announcement["statusCode"], HTTPStatus.BAD_REQUEST)
