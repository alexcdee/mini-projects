from fastapi import FastAPI
import random
import time

from prometheus_client import Counter, Histogram, generate_latest, CONTENT_TYPE_LATEST
from fastapi.responses import Response

app = FastAPI()

# prometheus metrics
REQUEST_COUNT = Counter(
    "app_requests_total",
    "Total HTTP requests",
    ["endpoint", "status"]
)

REQUEST_LATENCY = Histogram(
    "app_request_latency_seconds",
    "Request latency",
    ["endpoint"]
)



# health check
@app.get("/health")
def health():
    return {"status": "ok"}

# endpoint to simulate load and errors
@app.get("/simulate_work")
def simulate_work():
    start = time.time()

    # simulate variable latency
    sleep_time = (random.uniform(0.05, 0.8))
    time.sleep(sleep_time)

    if random.random() < 0.2:
        REQUEST_COUNT.labels(endpoint="/simulate_work", status="error").inc()
        REQUEST_LATENCY.labels(endpoint="/simulate_work").observe(time.time() - start)
        return {"status": "error"}

    REQUEST_COUNT.labels(endpoint="/simulate_work", status="success").inc()
    REQUEST_LATENCY.labels(endpoint="/simulate_work").observe(time.time() - start)
    
    return {"status": "success", "latency": sleep_time}

# exposition endpoint for prometheus
@app.get("/metrics")
def metrics():
    data = generate_latest()
    return Response(content=data, media_type=CONTENT_TYPE_LATEST)
