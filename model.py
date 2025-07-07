import yaml

def estimate_cost_from_infra(filepath="infra.yaml"):
    try:
        with open(filepath, 'r') as f:
            infra = yaml.safe_load(f)
    except Exception as e:
        return f"❌ Failed to read infra file: {e}"

    report = ["## 💰 Infrastructure Cost Estimation:\n"]

    # EC2 Instances
    ec2s = infra.get('ec2_instances', [])
    count = len(ec2s)
    gpu_instances = [i for i in ec2s if any(g in i['type'] for g in ['g4dn', 'p2', 'p3', 'a10g'])]
    if count:
        report.append(f"- 💻 {count} EC2 instances defined.")
    if gpu_instances:
        report.append(f"- ⚡ {len(gpu_instances)} GPU EC2 instance(s) found — higher cost.")

    # RDS
    rds = infra.get('rds_instances', [])
    if rds:
        report.append(f"- 🗄️ {len(rds)} RDS instance(s) configured (e.g., {rds[0]['engine']}).")

    # S3 Buckets
    s3s = infra.get('s3_buckets', [])
    if s3s:
        report.append(f"- 📦 {len(s3s)} S3 buckets listed — storage cost applies.")

    # K8s Replicas
    replicas = infra.get('k8s', {}).get('replicas', {})
    if replicas:
        total_replicas = sum(replicas.values())
        report.append(f"- 📈 {total_replicas} total Kubernetes replicas defined.")

    # Monitoring
    monitoring = infra.get('monitoring', {}).get('tools', [])
    if monitoring:
        report.append(f"- 📊 Monitoring tools: {', '.join(monitoring)} — may add data ingestion/storage costs.")

    report.append("\n_This is an AI-estimated cost based on declared infra. Actual billing may vary._")

    return "\n".join(report)

