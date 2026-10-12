
from datetime import datetime, timezone

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware


app = FastAPI(title="Security Awareness Training API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["https://test-site-phish-front.vercel.app"],
    allow_methods=["GET", "POST"],
    allow_headers=["Content-Type"],
)

class TrainingEvent(BaseModel):
    event: str



@app.get("/")
def health_check():
    return {"status": "API is running"}


@app.post("/api/training-event")
def record_training_event(data: TrainingEvent):
    if data.event != "training_form_submitted":
        raise HTTPException(
            status_code=400,
            detail="Invalid training event"
        )

    result = {
        "event": data.event,
        "timestamp": datetime.now(timezone.utc).isoformat(),
    }

    # Records the event in the server's console logs.
    print("Training event received:", result)

    return {
        "success": True,
        "message": "Training event recorded",
        "result": result,
    }