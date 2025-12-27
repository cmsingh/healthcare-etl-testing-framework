from datetime import date

def calculate_age(dob):
    dob = date.fromisoformat(dob)
    today = date.today()
    return today.year - dob.year

def convert_to_usd(amount, rate=0.012):
    return round(amount * rate, 2)

def transform_data(source_data):
    transformed = []
    for row in source_data:
        transformed.append({
            "patient_id": row["patient_id"],
            "age": calculate_age(row["dob"]),
            "gender": row["gender"],
            "visit_id": row["visit_id"],
            "visit_date": row["visit_date"],
            "billing_amount": row["billing_amount"],
            "billing_amount_usd": convert_to_usd(row["billing_amount"])
        })
    return transformed
