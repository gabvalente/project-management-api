from bson.errors import InvalidId
from bson.objectid import ObjectId


def is_valid(oid):
    try:
        ObjectId(oid)
        return True
    except (InvalidId, TypeError):
        return False
