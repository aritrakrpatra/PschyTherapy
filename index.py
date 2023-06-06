import random

# Define the chatbot responses
greetings = ["Hello!", "Hi there!", "Greetings!"]
positive_responses = ["That's great to hear!", "I'm glad you're feeling good!", "Keep up the positive mindset!"]
negative_responses = ["I'm sorry to hear that.", "Remember that you're not alone in this.", "Things will get better, I promise."]
farewell = ["Take care!", "Goodbye!", "Wishing you the best!"]

# Function to generate chatbot responses
def get_response(message):
    message = message.lower()

    if any(greeting in message for greeting in ["hello", "hi", "hey"]):
        return random.choice(greetings)
    elif any(keyword in message for keyword in ["good", "great", "positive"]):
        return random.choice(positive_responses)
    elif any(keyword in message for keyword in ["bad", "not good", "negative"]):
        return random.choice(negative_responses)
    elif any(keyword in message for keyword in ["bye", "goodbye", "take care"]):
        return random.choice(farewell)
    else:
        return "I'm sorry, I didn't understand. Can you please rephrase?"

# Main loop to interact with the chatbot
def chat():
    print("Welcome to the PHYTHERAPY Chatbot! How can I assist you today?")
    while True:
        user_message = input("> ")
        if user_message.lower() == "quit":
            print(random.choice(farewell))
            break
        else:
            bot_response = get_response(user_message)
            print(bot_response)

# Start the chatbot
chat()