# FinOps Cloud Cost Optimization Toolkit

> Azure cost optimization toolkit that delivered 28% reduction in cloud spend across enterprise subscriptions.
> Combines automated rightsizing, Reserved Instance recommendations, budget governance, and tagging enforcement.

---

## Results Achieved

| Metric | Before | After | Saving |
|---|---|---|---|
| Monthly Compute Spend | 145,000 USD | 104,400 USD | 28% (40,600/mo) |
| Untagged Resources | 34% | 2% | 94% compliance |
| RI Coverage | 18% | 67% | 49% increase |
| Idle Resources | 23% of VMs | 3% | 18,000/mo saved |

## Toolkit Components

| Script | Purpose |
|---|---|
| scripts/rightsize-advisor.py | VM rightsizing recommendations via Azure Advisor API |
| scripts/ri-coverage-report.py | RI coverage gaps and savings opportunities |
| scripts/idle-resource-hunter.py | Detect and report idle VMs, disks, public IPs |
| terraform/budget-alerts/ | Terraform for budget alerts and action groups |
| terraform/tagging-policy/ | Azure Policy for mandatory tag enforcement |
| dashboards/grafana-finops.json | Grafana FinOps dashboard |

## Tagging Standard

Required Tags:
  Environment  : dev, uat, prod
  Owner        : team-email@company.com
  CostCenter   : CC-1234
  Project      : project-code
  ManagedBy    : terraform or manual

---
Senior DevOps Engineer - Vikas Rao | FinOps Specialist