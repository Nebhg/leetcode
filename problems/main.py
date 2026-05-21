

raw = [
    {"event_id": "a1", "event_time": "2026-05-01 10:00","value": "1,234"},
    {"event_id": "a1", "event_time": "01/05/2026 10:00:00","value": "1.234"},   # duplicate id, different formats
    {"event_id": "b2", "event_time": "2026-05-02T12:00:00Z","value": "2.0"},
    {"event_id": "c3", "event_time": "bad-date","value": "3.0"},
    {"event_id": "d4", "event_time": "2026-05-03 09:30","value": None},
]

def normalize_events(raw):
    """
    Returns (clean_events, errors)
    clean_events: list of dicts, sorted by event_time
    errors: list of dicts containing event_id, reason, raw
    """
    # normalise dates first 
    # then check for each value if its valid
    # if invalid store in the hasmap under the id 
    clean = []
    errors = []
    seen = set()

    for event in raw:
        eid = event.get('event_id')
        raw_time = event.get('event_time')
        raw_value = event.get('value')

        if eid in seen:
            errors.append({"event_id": eid, "reason": "duplicate id", "raw": event   })
            continue
        seen.add(eid)
        

    
normalize_events(raw)