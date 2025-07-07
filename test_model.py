from model import analyze_diff, estimate_cost

diff = "diff --git a/app.py b/app.py\n+ print('Hello')"
print("🔍 Diff Analysis Result:\n")
print(analyze_diff(diff))

with open("infra.yaml", "r") as f:
    infra_content = f.read()
    print("\n💰 Infra Cost Estimation:\n")
    print(estimate_cost(infra_content))

