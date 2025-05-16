import json
import os
from datetime import datetime, timedelta

def load_alerts():
    with open(os.path.join("sample_data", "alerts.json"), "r") as f:
        return json.load(f)

def evaluate_alert(alert):
    """
    Assigns a priority based on the severity:
      - High if severity >= 7
      - Medium if severity between 4 and 6
      - Low if severity <= 3
    """
    severity = alert.get("severity", 0)
    if severity >= 7:
        priority = "High"
    elif severity >= 4:
        priority = "Medium"
    else:
        priority = "Low"
    alert["priority"] = priority
    return alert

def process_alerts(alerts):
    processed = [evaluate_alert(alert) for alert in alerts]
    return processed

def save_processed_alerts(alerts):
    with open(os.path.join("sample_data", "processed_alerts.json"), "w") as f:
        json.dump(alerts, f, indent=2)

if __name__ == "__main__":
    alerts = load_alerts()
    processed_alerts = process_alerts(alerts)
    save_processed_alerts(processed_alerts)
    print("Processed Alerts:")
    print(json.dumps(processed_alerts, indent=2))
