processed_events = set()

def validate_stream_event(event):
    event_id = event["visit_id"]

    if event_id in processed_events:
        raise ValueError("Duplicate HL7 event")

    processed_events.add(event_id)

    mandatory = ["patient_id", "visit_id", "gender"]
    for field in mandatory:
        if event.get(field) is None:
            raise ValueError("Invalid HL7 message")
