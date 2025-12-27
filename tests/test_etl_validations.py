from etl.extract import extract_data
from etl.transform import transform_data
from etl.load import load_to_target
from validations.row_count_validation import validate_row_count
from validations.schema_validation import validate_schema
from validations.duplicate_validation import validate_duplicates
from validations.null_validation import validate_nulls
from validations.transformation_validation import validate_transformations

def test_end_to_end_etl():
    source = extract_data("data/source_emr_data.json")
    transformed = transform_data(source)
    target_count = load_to_target(transformed)

    validate_row_count(source, target_count)
    validate_duplicates(source)
    validate_nulls(source)
    validate_schema(tuple(transformed[0].keys()))
    validate_transformations()
