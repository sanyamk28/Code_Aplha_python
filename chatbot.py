import nltk
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer

# Initialize the lemmatizer
lemmatizer = WordNetLemmatizer()

# Define a dictionary of responses
responses = {
    "hello": "Hi! How can I help you today?",
    "hi": "Hello! What's on your mind?",
    "how are you": "I'm doing well, thanks! How about you?",
    "what is your name": "I'm Chatty, your friendly chatbot!",
    "goodbye": "See you later! Have a great day!",
    "bye": "Goodbye! Come back soon!"
}

# Define a function to process user input
def process_input(input_text):
    # Tokenize the input text
    tokens = word_tokenize(input_text.lower())

    # Lemmatize the tokens
    lemmas = [lemmatizer.lemmatize(token) for token in tokens]

    # Join the lemmas back into a string
    input_text = " ".join(lemmas)

    # Check if the input matches a response
    if input_text in responses:
        return responses[input_text]
    else:
        return "I didn't understand that. Can you please rephrase?"

# Create a chatbot loop
while True:
    # Get user input
    user_input = input("You: ")

    # Process the input and get a response
    response = process_input(user_input)

    # Print the response
    print("Chatty:", response)

    # Check if the user wants to quit
    if user_input.lower() in ["quit", "exit", "goodbye", "bye"]:
        break
