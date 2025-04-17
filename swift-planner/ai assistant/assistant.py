# utils/ai_assistant.py

def get_ai_response(user_input):
    user_input = user_input.lower()

    if "add guest" in user_input or "guest list" in user_input:
        return "To add guests, go to your event, then click 'Manage Guests'."

    elif "reminder" in user_input or "invite" in user_input:
        return "Don't forget to send invitations a week before the event!"

    elif "best time" in user_input:
        return "The best time to host an event is usually on weekends after 3PM."

    elif "help" in user_input:
        return "You can ask me about adding events, managing guests, or sending invites."

    else:
        return "Sorry, I’m not sure how to help with that. Try asking something else!"
