class Response:
    DEFAULT_HEADERS = {
        "Content-Type": "application/json"
    }

    def __init__(self, status_code, body=None, headers=None):
        self.status_code = status_code
        self.headers = headers or {}
        self.body = body or {}

    @property
    def json(self):
        response = {
            "statusCode": self.status_code,
            "headers": {**self.DEFAULT_HEADERS, **self.headers},
            "body": self.body,
        }
        return response
