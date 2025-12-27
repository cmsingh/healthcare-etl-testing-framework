from etl.transform import calculate_age, convert_to_usd

def validate_transformations():
    assert calculate_age("2000-01-01") > 0
    assert convert_to_usd(1000) == 12.00
