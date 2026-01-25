import os
import httpx
from fastapi import FastAPI, Request

DISCORD_WEBHOOK = os.environ["DISCORD_WEBHOOK"]

app = FastAPI()

@app.post("/webhook")
async def alertmanager_webhook(request: Request):
    # parse alertmanager payload
    payload = await request.json()
    status = payload.get("status", "")
    alerts = payload.get("alerts", [])

    messages = []

    for alert in alerts:
        # extract metadata from labels
        labels = alert.get("labels", {})
        alertname = labels.get("alertname", "Alert")
        instance = labels.get("instance", "unknown")
        severity = labels.get("severity", "none")

        # format alert message based on status
            # detail message when api is down
            content = (
                "🚨 FastAPI app is DOWN 🚨\n"
                f"[FIRING] {alertname} on {instance}\n"
                f"Severity: {severity}\n"
                "Summary: FastAPI is down\n"
                f"Details: service {instance} is unreachable"
            )
        elif status == "resolved":
            # short message when api is back up
            content = (
                "✅ FastAPI app is BACK UP ✅\n"
                f"[RESOLVED] {alertname} on {instance}\n"
                "Severity: low\n"
                "Summary: FastAPI is back up\n"
                f"Details: service {instance} is now reachable"
            )
        else:
            content = f"=== {status.upper()} {alertname} on {instance} ==="

        messages.append(content)

    # batch send logic
    if messages:
        async with httpx.AsyncClient() as client:
            await client.post(
                DISCORD_WEBHOOK,
                json={"content": "\n\n".join(messages)},
            )

    return {"status": "ok"}
