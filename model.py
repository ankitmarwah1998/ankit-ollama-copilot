import subprocess

def analyze_diff(diff: str) -> str:
    if not diff.strip():
        return "⚠️ No meaningful changes detected in the pull request."

    prompt = f"""
You are an AI DevOps and FinOps assistant.

Your job is to analyze the following git diff and:
1. 🧾 Provide a summary of changes
2. 🚀 Suggest an appropriate deployment strategy (blue/green, rolling, canary, etc.)
3. ✅ Recommend testing and rollback strategy
4. ⚠️ Identify risky or anti-pattern changes (e.g., hardcoded secrets, DB schema changes)
5. 💰 Estimate infrastructure cost impact due to this change
   - Include EC2, RDS, EBS, S3, egress, Lambda, etc.
   - Give qualitative and rough quantitative cost increase (like +$10/month)
6. Format everything nicely in GitHub Markdown with emojis and tables where needed.

Git Diff:
{diff}
"""

    try:
        # Use Ollama to generate the AI response
        result = subprocess.run(
            ["ollama", "run", "gemma:2b"],
            input=prompt.encode("utf-8"),
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            timeout=120,
        )

        if result.returncode != 0:
            return f"❌ AI suggestion failed: {result.stderr.decode('utf-8')}"

        return result.stdout.decode("utf-8").strip()

    except Exception as e:
        return f"❌ AI suggestion failed: {str(e)}"

