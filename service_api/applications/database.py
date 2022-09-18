import arrow
import boto3


class Database:
    table = boto3.resource("dynamodb").Table("Announcement")

    @classmethod
    def put_item(cls, item):
        return cls.table.put_item(Item={
            "title": item["title"],
            "description": item["description"],
            "date": arrow.get(item["date"]).format("YYYY-MM-DD")
        })

    @classmethod
    def batch_writer(cls, items):
        with cls.table.batch_writer() as batch:
            for item in items:
                batch.put_item(Item={
                    "title": item["title"],
                    "description": item["description"],
                    "date": arrow.get(item["date"]).format("YYYY-MM-DD")
                })

    @classmethod
    def scan(cls, *args, **kwargs):
        return cls.table.scan(*args, **kwargs)

    @classmethod
    def delete_item(cls):
        cls.table.delete()
