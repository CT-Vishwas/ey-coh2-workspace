from dataclasses import dataclass

security_logs = [
    {"source_ip": "192.168.1.10", "event_type": "failed_login", "attempts": 3},
    {"source_ip": "192.168.1.20", "event_type": "port_scan", "attempts": 4},
    {"source_ip": "192.168.1.30", "event_type": "malware_alert", "attempts": 2},
    {"source_ip": "192.168.1.10", "event_type": "failed_login", "attempts": 4}
]

@dataclass
class security_event:
    source_ip : str
    event_type: str
    attempts : int

# Risk weight mapping
risk_weights = {
    "failed_login": 2,
    "port_scan": 3,
    "malware_alert": 5
}

# Dictionary to store total risk score per IP
ip_risk_scores = {}

# Calculate total risk score per IP
for log in security_logs:
    # ip = log["source_ip"]
    # event = log["event_type"]
    # attempts = log["attempts"]
    security_event

    risk_score = attempts * risk_weights[event]

    if ip in ip_risk_scores:
        ip_risk_scores[ip] += risk_score
    else:
        ip_risk_scores[ip] = risk_score

# Categorize risk levels
ip_risk_category = {}

for ip, score in ip_risk_scores.items():
    if score < 10:
        category = "Low Risk"
    elif 10 <= score <= 20:
        category = "Medium Risk"
    else:
        category = "High Risk"

    ip_risk_category[ip] = {
        "Total Risk Score": score,
        "Risk Category": category
    }

# Display final report
for ip, details in ip_risk_category.items():
    print(f"IP Address: {ip}")
    print(f"Total Risk Score: {details['Total Risk Score']}")
    print(f"Risk Category: {details['Risk Category']}")
    print("-" * 40)
