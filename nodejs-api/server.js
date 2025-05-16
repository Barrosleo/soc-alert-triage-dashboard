const express = require('express');
const path = require('path');
const app = express();
const PORT = 3000;

// Serve static files from the dashboard directory.
app.use(express.static(path.join(__dirname, 'views')));

// API endpoint to retrieve processed alert data.
app.get('/api/alerts', (req, res) => {
  try {
    const alerts = require('../python-module/sample_data/processed_alerts.json');
    res.json(alerts);
  } catch (err) {
    console.error("Error fetching alerts:", err);
    res.status(500).json({ error: "Failed to retrieve alerts." });
  }
});

app.listen(PORT, () => {
  console.log(`Server running at http://localhost:${PORT}`);
});
