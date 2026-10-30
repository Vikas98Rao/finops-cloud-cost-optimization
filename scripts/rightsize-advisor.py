#!/usr/bin/env python3
"""
Azure VM Rightsizing Advisor
Author: Vikas Rao | Senior DevOps Engineer
Queries Azure Advisor recommendations and generates a rightsizing report.
"""

import os
import json
from datetime import datetime
from azure.identity import DefaultAzureCredential
from azure.mgmt.advisor import AdvisorManagementClient

SUBSCRIPTION_ID = os.environ['AZURE_SUBSCRIPTION_ID']
credential = DefaultAzureCredential()

def get_rightsizing_recommendations():
    advisor = AdvisorManagementClient(credential, SUBSCRIPTION_ID)
    recs = advisor.recommendations.list(filter="Category eq 'Cost'")
    results = []
    for rec in recs:
        if rec.short_description and 'right-size' in rec.short_description.problem.lower():
            results.append({
                'resource': rec.resource_metadata.resource_id.split('/')[-1],
                'current_sku': rec.extended_properties.get('currentSku', 'unknown'),
                'recommended_sku': rec.extended_properties.get('targetSku', 'unknown'),
                'estimated_annual_saving': rec.extended_properties.get('annualSavingsAmount', 0),
                'impact': rec.impact,
            })
    return results

def generate_report(recommendations):
    total_saving = sum(float(r['estimated_annual_saving']) for r in recommendations)
    report = {
        'generated_at': datetime.utcnow().isoformat(),
        'subscription_id': SUBSCRIPTION_ID,
        'total_recommendations': len(recommendations),
        'total_annual_saving_usd': round(total_saving, 2),
        'recommendations': sorted(recommendations, key=lambda x: float(x['estimated_annual_saving']), reverse=True)
    }
    filename = f"rightsizing-report-{datetime.utcnow().strftime('%Y%m%d')}.json"
    with open(filename, 'w') as f:
        json.dump(report, f, indent=2)
    print(f'Report saved: {filename}')
    print(f'Total recommendations: {len(recommendations)}')
    print(f'Total annual savings: USD {total_saving:,.2f}')
    return report

if __name__ == '__main__':
    print('Fetching Azure Advisor rightsizing recommendations...')
    recs = get_rightsizing_recommendations()
    generate_report(recs)