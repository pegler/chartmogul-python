from marshmallow import Schema, fields, post_load
from ..resource import Resource, _add_method
from collections import namedtuple


class Ping(Resource):
    """
    https://dev.chartmogul.com/docs/authentication
    """
    _path = "/ping"

    class _Schema(Schema):
        data = fields.String()

        @post_load
        def make(self, data):
            return Ping(**data)

    _schema = _Schema(strict=True)


_add_method(Ping, "ping", "get")
