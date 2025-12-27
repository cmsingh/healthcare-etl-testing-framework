def validate_duplicates(data):
    visit_ids = [row["visit_id"] for row in data]
    assert len(visit_ids) == len(set(visit_ids)), \
        "Duplicate visit_id found"
