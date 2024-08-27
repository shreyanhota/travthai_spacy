import spacy

# Load the small English model
nlp = spacy.load('en_core_web_sm')

def get_response(user_input):
    # Process the input text
    doc = nlp(user_input)

    # Initialize an empty response
    response = "I'm here to help with your travel plans! Ask me about destinations, tips, and more."

    # Simple logic based on entities recognized by spaCy
    for ent in doc.ents:
        if ent.label_ == "GPE":  # GPE = Geopolitical Entity (like countries, cities, etc.)
            response = f"Planning a trip to {ent.text}? I can help you find the best places to visit!"
        elif ent.label_ == "DATE":
            response = f"Looking for travel options around {ent.text}? I can suggest some great destinations!"

    return response

# Test the chatbot
if __name__ == "__main__":
    while True:
        user_input = input("You: ")
        response = get_response(user_input)
        print("Bot:", response)
