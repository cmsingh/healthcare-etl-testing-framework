def validate_row_count(source_data, target_count):
    assert len(source_data) == target_count, \
        "Row count mismatch between source and target"
