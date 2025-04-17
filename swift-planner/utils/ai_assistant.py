# utils/ai_assistant.py

def get_ai_response(user_input):
    prompt = f"""
You are Sia, a friendly and intelligent virtual assistant in the Swift Planner application.
Your job is to help event planners manage and optimize their events.

Capabilities:
- Explain how Swift Planner features work.
- Remind the user of upcoming events.
- Suggest venues in a given city for a specific number of guests.
- Offer useful event planning tips.

Respond clearly, in a friendly and helpful tone.

User: {user_input}
Sia:
"""
    # Simulate a response — we'll replace this with a real AI model or logic later
    if "how do I create an event" in user_input.lower():
        return "To create an event, go to the Dashboard > Create Event. Fill in the name, date, location, and description."
    elif "remind me" in user_input.lower() or "upcoming event" in user_input.lower():
        return "You have an event called 'Launch Party' on April 20 at The Grand Hall."
    elif "venue" in user_input.lower():
        return "Based on your location and number of guests, I suggest: 'Skyline Venue', 'Lakeside Gardens', or 'Urban Loft'."
    else:
        return "I'm here to help! You can ask me anything about managing events with Swift Planner."
