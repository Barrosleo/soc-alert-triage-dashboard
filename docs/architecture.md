
---

### docs/architecture.md


# Architecture Overview

## System Components

1. **Python Module:**
   - **ingest_alerts.py:**  
     Reads sample alert data from `sample_data/alerts.json` and processes each alert to assign a priority based on its severity.
   - **Sample Data:**  
     `alerts.json` contains raw alert entries. The processed results are saved as `processed_alerts.json`.

2. **Node.js API:**
   - **server.js:**  
     Uses Express to serve an API endpoint `/api/alerts` that returns the processed alert data. It also serves the static dashboard from the `views/` directory.

3. **Dashboard:**
   - **dashboard.html:**  
     A simple interface using HTML and JavaScript (with Plotly.js) that visualizes alerts and their priorities.

## Data Flow

1. The Python script reads raw alert data.
2. Alerts are processed with basic triage rules and saved to `processed_alerts.json`.
3. The Node.js API exposes this processed data via an endpoint.
4. The dashboard fetches the data and displays it interactively.

## Design Principles

- **Simplicity:**  
  Focused on core SOC Level 1 tasks: alert triage and initial evaluation.

- **Modularity:**  
  Clear separation between data processing (Python) and data presentation (Node.js/JavaScript).

- **Extensibility:**  
  Easy to integrate with real-time SIEM data and to add more complex triage logic in the future.
