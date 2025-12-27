"""
BigQuery Validation Runner
Executes SQL-based validations and applies Python assertions
"""

def assert_equal(actual, expected, message):
    if actual != expected:
        raise ValueError(f"{message}. Actual={actual}, Expected={expected}")

def assert_zero(value, message):
    if value != 0:
        raise ValueError(f"{message}. Value={value}")


def run_bigquery_validations(
    source_count,
    target_count,
    duplicate_count,
    null_count
):
    """
    Central validation controller for BigQuery checks
    """

    # Row count validation
    assert_equal(
        target_count,
        source_count,
        "Row count mismatch between source and BigQuery target"
    )

    # Duplicate validation
    assert_zero(
        duplicate_count,
        "Duplicate visit_id found in BigQuery"
    )

    # NULL validation
    assert_zero(
        null_count,
        "NULL values found in mandatory columns"
    )

    print("All BigQuery validations passed successfully")
