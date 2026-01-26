# FastAPI Monitoring Stack

Production-grade monitoring and alerting for FastAPI applications using Prometheus, Grafana, and Alertmanager.

## Features

- **Metrics**: Request count, latency histograms, error rates
- **Dashboards**: Real-time Grafana visualizations
- **Alerts**: Discord notifications on high error rate or latency

## Tech Stack

- Python (FastAPI)
- Prometheus
- Grafana
- Alertmanager
- Docker Compose

## Setup

1. Clone the repository
2. Create `.env` file:

DISCORD_WBHOOK_URL=https://discord.com/api/weboooks/YOUR_WEBHOOK_URL

3. Run the stack:
```bash
docker compose up --build
```

Access
- App: http://localhost:8000
- Prometheus: http://localhost:9090
- Grafana: http://localhost:3000 (admin/admin)
- Alertmanager: http://localhost:9093

Metrics Endpoints
- /health - Health check
- /simulate_work - Simulated workload
- /metrics - Prometheus metrics
