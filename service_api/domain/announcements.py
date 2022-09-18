import base64
import datetime
import json

from service_api.applications.database import Database


class Announcements:

    @staticmethod
    def get_announcements(limit=None, offset=None):
        last_evaluated_key = None

        if not offset:
            response = Database.scan(Limit=limit)
        else:
            response = Database.scan(
                Limit=limit,
                ExclusiveStartKey=json.loads(base64.b64decode(offset+"="))
            )

        if "LastEvaluatedKey" in response:
            blek = json.dumps(response["LastEvaluatedKey"]).encode()
            base64_blek = base64.b64encode(blek)
            last_evaluated_key = base64_blek.decode()

        return response["Items"], last_evaluated_key

    @staticmethod
    def create_announcements(payload):
        if isinstance(payload, list):
            Database.batch_writer(payload)
            return payload

        Database.put_item(payload)
        return payload

    @staticmethod
    def get_announcement(announcement_id):
        return {
                "title": "mock",
                "description": "DMock",
                "date": datetime.date(2020, 2, 2)
            }
