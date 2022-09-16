import datetime


class Announcements:

    @staticmethod
    def get_announcements():
        return [
            {
                "title": "mock",
                "description": "DMock",
                "date": datetime.date(2020, 2, 2)
            }
        ]

    @staticmethod
    def create_announcements(payload):
        return payload

    @staticmethod
    def get_announcement(announcement_id):
        return {
                "title": "mock",
                "description": "DMock",
                "date": datetime.date(2020, 2, 2)
            }
