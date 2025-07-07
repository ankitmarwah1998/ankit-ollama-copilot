import subprocess

def analyze_diff(diff: str) -> str:
    if not diff.strip():
        return "⚠️ No meaningful changes detected in the pull request."

    prompt = f"""
You are an expert AI DevOps + FinOps assistant.

Your job is to analyze the following git diff and return a GitHub Markdown comment with:

1. 🧾 Summary of code changes
2. 🚀 Suggested deployment strategy
3. ✅ Testing recommendations
4. ⚠️ Risks or anti-patterns
5. 💰 Infra cost impact (with dollar estimate)
6. 🎨 Use emojis, markdown tables, and include these visual elements:
    - GitHub Copilot logo: ![logo](https://github.githubassets.com/images/modules/logos_page/GitHub-Mark.png)
    - Optional relevant GIF (like rocket or warning)
    - Tables for cost estimate
    - Bullet points for clarity

Here is the code diff:
{diff}
"""

    try:
        result = subprocess.run(
            ["ollama", "run", "gemma:2b"],
            input=prompt.encode("utf-8"),
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            timeout=180,
        )

        if result.returncode != 0:
            return f"❌ AI suggestion failed: {result.stderr.decode('utf-8')}"

        return result.stdout.decode("utf-8").strip()

    except Exception as e:
        return f"❌ AI suggestion failed: {str(e)}"

