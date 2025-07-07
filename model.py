import ollama

def analyze_diff(diff):
    if not diff.strip():
        return "No meaningful changes detected."

    try:
        response = ollama.chat(model='gemma:2b', messages=[
            {"role": "system", "content": "You are a DevOps assistant that analyzes code diffs and suggests deployment strategies, flags risky changes, and recommends improvements."},
            {"role": "user", "content": f"Analyze this code diff:\n{diff}"}
        ])
        return response['message']['content']
    except Exception as e:
        return f"AI suggestion failed: {str(e)}"

