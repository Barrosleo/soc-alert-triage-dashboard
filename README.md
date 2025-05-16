# SOC Alert Triage Dashboard

A lightweight incident triage tool built for SOC Analyst Level 1 professionals. This project simulates core SOC tasks by ingesting sample security alerts, performing basic prioritization, and delivering an interactive dashboard view. It demonstrates the fundamentals of alert triage, investigation, and reporting using Python, Node.js, and JavaScript.

## Table of Contents

- [Overview](#overview)
- [Key Features](#key-features)
- [Architecture](#architecture)
- [Installation & Setup](#installation--setup)
- [Usage](#usage)
- [Project Structure](#project-structure)
- [Future Enhancements](#future-enhancements)
- [License](#license)
- [Contact](#contact)

## Overview

Level 1 SOC Analysts need to quickly review incoming alerts and determine if further investigation is required. This tool ingests sample alert data, evaluates each alert by assigning a priority based on severity, and displays all alerts in an interactive dashboard for quick triage.

## Key Features

- **Alert Ingestion:** Reads sample security alerts from a JSON file.
- **Basic Triage:** Evaluates alerts and assigns a priority (Low, Medium, or High) based on the severity score.
- **Interactive Dashboard:** Visualizes alert timelines and priorities for analysts via a clean web interface.
- **Easy to Extend:** Designed as a proof-of-concept that can be expanded to integrate real SIEM data.

## Architecture

For detailed explanations of the system components and data flow, please see the [docs/architecture.md](docs/architecture.md) file.

## Installation & Setup

### Prerequisites

- Python 3.6+ and pip  
- Node.js (v12+)

### Steps

1. **Clone the Repository:**

   ```bash
   git clone https://github.com/yourusername/soc-alert-triage-dashboard.git
   cd soc-alert-triage-dashboard
   ```
2.  **Setup the Python Module:**
```
bash
cd python-module
pip install -r requirements.txt
python ingest_alerts.py
```
This script reads alerts.json, processes the alerts, and writes the results to processed_alerts.json.

3.  **Setup the Node.js API & Dashboard:**
```
bash
cd ../nodejs-api
npm install
node server.js
```
4.  **Access the Dashboard:**

Open your browser and navigate to http://localhost:3000/dashboard

### Usage

Data Ingestion: The Python script ingest_alerts.py loads and processes sample alerts from python-module/sample_data/alerts.json.

Alert Evaluation: A simple prioritization algorithm assigns a priority based on the alert’s severity.

Dashboard: The Node.js API serves the processed alert data to the front-end dashboard, which visualizes alerts in an interactive table/timeline.

### Project Structure
```
soc-alert-triage-dashboard/
├── README.md
├── docs/
│   └── architecture.md
├── python-module/
│   ├── ingest_alerts.py
│   ├── requirements.txt
│   └── sample_data/
│         ├── alerts.json
│         └── processed_alerts.json
├── nodejs-api/
│   ├── server.js
│   ├── package.json
│   └── views/
│         └── dashboard.html
```
### Future Enhancements

Integrate with live SIEM data sources.

Add better alert correlation and automated escalation.

Improve visualizations with detailed incident timelines.

Introduce a lightweight user authentication mechanism.

### License

This project is licensed under the MIT License.
