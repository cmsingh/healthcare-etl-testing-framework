from config.schema_config import EXPECTED_SCHEMA

def validate_schema(actual_schema):
    assert EXPECTED_SCHEMA == actual_schema, \
        "Schema drift detected"
