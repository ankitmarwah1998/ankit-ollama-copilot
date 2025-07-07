def analyze_diff(diff):
    if not diff.strip():
        return "No meaningful changes detected."

    if "print" in diff:
        return "⚠️ Detected use of print statements. Consider using logging."

    return f"✅ Analyzed diff of {len(diff)} characters. No issues found."

