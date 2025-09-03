# model.py
import requests
import json

def analyze_diff(diff_text: str) -> str:
    prompt = f"""
You are an AI DevOps assistant.
Analyze the following code diff and provide a detailed response with:

1. **Summary of the intent of the change**  
2. **Recommended deployment strategy**  
3. **Infrastructure components impacted**  
4. **Tests to run before deploying**  
5. **Additional notes or risks**

Diff:
{diff_text}
"""

    response = requests.post(
        "http://localhost:11434/api/generate",
        json={"model": "gemma:2b", "prompt": prompt},
        stream=False
    )

    data = response.json()
    return data.get("response", "No analysis generated.")

