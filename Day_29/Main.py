from fastapi import FastAPI, HTTPException
from model import UserRegistration
import File_handler

app = FastAPI(title= "EVENT REGISTRATION APP! 🗓️✨",
    description="A FastAPI backend to view available events and register for them.",
    version="0.115.13"
)

@app.get("/events")
def get_events():           #  Return a list of all available events.
    return File_handler.load_events()


@app.post("/register")
def register_user(user: UserRegistration):      #  Register a user for a specific event if slots are available.
    events = File_handler.load_events()

    matching_event = next((event for event in events if event["event_id"] == user.event), None)

    if not matching_event:
        raise HTTPException(status_code=404, detail="Event does not exist.")

    if matching_event["available_slots"] == 0:
        raise HTTPException(status_code=400, detail="Event is full.")

    File_handler.reduce_event_slot(user.event)
    File_handler.save_registration(user.name, user.email_id, user.age, user.event)

    return {"message": "Registration successful!"}


@app.get("/registrations")
def view_registrations():           #  Return a list of all user registrations.
    return File_handler.get_all_registrations()