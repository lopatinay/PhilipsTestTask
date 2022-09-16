from marshmallow import Schema, fields


class AnnouncementDeserializer(Schema):
    title = fields.String(required=True)
    description = fields.String(required=True)
    date = fields.Date(required=True)


class AnnouncementSerializer(Schema):
    title = fields.String(required=True)
    description = fields.String(required=True)
    date = fields.Date(required=True)
