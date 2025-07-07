import subprocess

def analyze_diff(diff: str) -> str:
    if not diff.strip():
        return "⚠️ No meaningful changes detected in the pull request."

    prompt = f"""
You are an expert AI DevOps + FinOps assistant.

Analyze the following `git diff` and provide a GitHub Markdown comment with:

---

**🧾 Code Summary:**  
Summarize what was changed.

**🚀 Deployment Strategy:**  
What deployment strategy should be used (rolling, blue-green, canary, etc.)?

**🔧 Infra/Config Changes:**  
Any infrastructure or config changes detected?

**✅ Testing Plan:**  
What tests should be added or verified?

**⚠️ Red Flags or Anti-Patterns:**  
Any risky code or practices?

**💰 Infra Cost Estimate:**  
Rough estimate of cloud resource cost impact (monthly/daily if applicable) based on changes. Format this in a table like:

| Resource | Description | Est. Monthly Cost |
|----------|-------------|-------------------|
| EC2 | Added instance for worker | ~$12.00 |
| S3 | Logging added | ~$0.10 |
| **Total** |             | **~$12.10** |

---

Now analyze this git diff:

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

