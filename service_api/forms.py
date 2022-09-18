import arrow
from marshmallow import Schema, fields, pre_dump, pre_load


class AnnouncementDeserializer(Schema):
    title = fields.String(required=True)
    description = fields.String(required=True)
    date = fields.Date(required=True)

    @pre_load
    def convert_dt(self, data, **kwargs):
        data["date"] = arrow.get(data["date"], "YYYY-MM-DD").format("YYYY-MM-DD")
        return data


class AnnouncementSerializer(Schema):
    title = fields.String(required=True)
    description = fields.String(required=True)
    date = fields.String(required=True)

    @pre_dump
    def convert_dt(self, data, **kwargs):
        data["date"] = arrow.get(data["date"]).format("YYYY-MM-DD")
        return data
