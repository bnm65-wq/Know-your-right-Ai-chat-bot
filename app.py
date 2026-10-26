import os
from dotenv import load_dotenv
from google import genai
from google.genai import types

# Load API key from .env file
load_dotenv()
api_key = os.getenv("GEMINI_API_KEY")

if not api_key:
    raise ValueError("GEMINI_API_KEY not found. Please set it in your .env file.")

client = genai.Client(api_key=api_key)

# The System Prompt defines the bot's behavior
SYSTEM_INSTRUCTION = """
You are a chatbot that provides users with clear, actionable information on their rights.
Your focus areas are:
1. Human Rights
2. Consumer Rights
3. Legal/Constitutional Rights
4. Housing Rights
5. Education Rights

Guidelines:
- Tailor answers based on the user's location (country, state/province, city).
- If the user hasn't provided a location, ask for it before giving jurisdiction-specific advice.
- Cite relevant statutes, agencies, or standard legal timelines when applicable.
- Maintain a helpful, objective tone and include an educational disclaimer (not formal legal advice).
"""

def start_chat():
    print("==================================================")
    print(" Rights Information Assistant Initialized ")
    print(" (Type 'exit' or 'quit' to end the session) ")
    print("==================================================\n")

    # Create a persistent chat session
    chat = client.chats.create(
        model="gemini-2.5-flash",
        config=types.GenerateContentConfig(
            system_instruction=SYSTEM_INSTRUCTION,
            temperature=0.3, # Lower temperature for more factual, precise answers
        )
    )

    while True:
        try:
            user_input = input("You: ")
            if user_input.strip().lower() in ["exit", "quit"]:
                print("Goodbye!")
                break
            
            if not user_input.strip():
                continue

            response = chat.send_message(user_input)
            print(f"\nAssistant:\n{response.text}\n")
            print("-" * 50)

        except KeyboardInterrupt:
            print("\nExiting...")
            break
        except Exception as e:
            print(f"Error: {e}")

if __name__ == "__main__":
    start_chat()