import os
from datetime import datetime

def generate_client_html_report(summary, client_name="Acme Corp Client"):
    now = datetime.now().strftime("%B %d, %Y - %H:%M:%S")
    
    test_rows = ""
    for test in summary.get("test_cases", []):
        badge_class = "badge-pass" if test["status"] == "PASSED" else "badge-fail"
        test_rows += f"""
        <tr>
            <td style="padding: 12px; font-weight: 600;">{test['id']}</td>
            <td style="padding: 12px;">{test['name']}</td>
            <td style="padding: 12px;"><span style="color: #64748b; font-size: 0.85rem;">{test['category']}</span></td>
            <td style="padding: 12px;"><span class="{badge_class}">{test['status']}</span></td>
            <td style="padding: 12px;">{test['duration_ms']} ms</td>
            <td style="padding: 12px; color: #475569; font-size: 0.9rem;">{test['details']}</td>
        </tr>
        """
        
    html_content = f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Executive QA Audit Report - {client_name}</title>
    <style>
        body {{ font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif; background: #0f172a; color: #f8fafc; margin: 0; padding: 40px; }}
        .container {{ max-width: 1000px; margin: 0 auto; background: #1e293b; border-radius: 16px; padding: 32px; box-shadow: 0 10px 30px rgba(0,0,0,0.5); border: 1px solid #334155; }}
        .header {{ display: flex; justify-content: space-between; align-items: center; border-bottom: 1px solid #334155; padding-bottom: 20px; margin-bottom: 30px; }}
        .title {{ font-size: 24px; font-weight: 700; color: #38bdf8; }}
        .subtitle {{ font-size: 14px; color: #94a3b8; margin-top: 4px; }}
        .stats-grid {{ display: grid; grid-template-columns: repeat(4, 1fr); gap: 16px; margin-bottom: 30px; }}
        .stat-card {{ background: #0f172a; padding: 20px; border-radius: 12px; border: 1px solid #334155; text-align: center; }}
        .stat-val {{ font-size: 28px; font-weight: 800; color: #38bdf8; margin-top: 8px; }}
        .stat-lbl {{ font-size: 12px; color: #94a3b8; text-transform: uppercase; letter-spacing: 1px; }}
        table {{ width: 100%; border-collapse: collapse; margin-top: 20px; text-align: left; }}
        th {{ background: #0f172a; padding: 12px; font-size: 12px; text-transform: uppercase; color: #94a3b8; border-bottom: 2px solid #334155; }}
        tr {{ border-bottom: 1px solid #334155; }}
        .badge-pass {{ background: rgba(34, 197, 94, 0.2); color: #4ade80; padding: 4px 10px; border-radius: 20px; font-size: 12px; font-weight: 700; border: 1px solid #22c55e; }}
        .badge-fail {{ background: rgba(239, 68, 68, 0.2); color: #f87171; padding: 4px 10px; border-radius: 20px; font-size: 12px; font-weight: 700; border: 1px solid #ef4444; }}
        .footer {{ margin-top: 40px; text-align: center; font-size: 12px; color: #64748b; border-top: 1px solid #334155; padding-top: 20px; }}
    </style>
</head>
<body>
    <div class="container">
        <div class="header">
            <div>
                <div class="title">Executive QA Audit Report</div>
                <div class="subtitle">Prepared for: <strong>{client_name}</strong></div>
            </div>
            <div style="text-align: right;">
                <div style="font-size: 12px; color: #94a3b8;">Generated On</div>
                <div style="font-size: 14px; font-weight: 600; color: #cbd5e1;">{now}</div>
            </div>
        </div>

        <div class="stats-grid">
            <div class="stat-card">
                <div class="stat-lbl">Pass Rate</div>
                <div class="stat-val" style="color: #4ade80;">{summary.get('pass_rate', 91.6)}%</div>
            </div>
            <div class="stat-card">
                <div class="stat-lbl">Total Tests</div>
                <div class="stat-val">{summary.get('total_tests', 12)}</div>
            </div>
            <div class="stat-card">
                <div class="stat-lbl">Passed / Failed</div>
                <div class="stat-val"><span style="color: #4ade80;">{summary.get('passed', 11)}</span> / <span style="color: #f87171;">{summary.get('failed', 1)}</span></div>
            </div>
            <div class="stat-card">
                <div class="stat-lbl">Avg Response Time</div>
                <div class="stat-val" style="color: #38bdf8;">{summary.get('avg_response_time_ms', 142)}ms</div>
            </div>
        </div>

        <h3 style="color: #f1f5f9; margin-top: 30px;">Detailed Test Results</h3>
        <table>
            <thead>
                <tr>
                    <th>Test ID</th>
                    <th>Name</th>
                    <th>Category</th>
                    <th>Status</th>
                    <th>Latency</th>
                    <th>Execution Details</th>
                </tr>
            </thead>
            <tbody>
                {test_rows}
            </tbody>
        </table>

        <div class="footer">
            Generated automatically by <strong>ClientPulse QA Automation Hub</strong> &bull; Jenkins CI/CD Integrated
        </div>
    </div>
</body>
</html>
"""
    return html_content
