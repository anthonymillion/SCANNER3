def combine_signals(econ, cot, options):
    all_keys = set(econ) | set(cot) | set(options)
    combined = []
    for key in sorted(all_keys):
        row = {
            "Symbol": key,
            "Economic": econ.get(key, {}).get("sentiment", ""),
            "Econ Reason": econ.get(key, {}).get("reason", ""),
            "COT": cot.get(key, {}).get("sentiment", ""),
            "COT Reason": cot.get(key, {}).get("reason", ""),
            "Options": options.get(key, {}).get("sentiment", ""),
            "Options Reason": options.get(key, {}).get("reason", "")
        }
        combined.append(row)
    return combined