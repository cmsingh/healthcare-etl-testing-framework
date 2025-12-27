from config.schema_config import MANDATORY_FIELDS

def validate_nulls(data):
    for row in data:
        for field in MANDATORY_FIELDS:
            assert row[field] is not None, \
                f"NULL found in mandatory field: {field}"
