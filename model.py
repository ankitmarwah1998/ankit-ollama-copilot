def analyze_diff(diff):
    if not diff.strip():
        return "No changes detected in the pull request."
    return f"Received diff of length {len(diff)}"

