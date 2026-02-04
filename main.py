# Library imports
import os
import argparse
from dotenv import load_dotenv
from google import genai
from google.genai import types
load_dotenv()

# Global constants
api_key = os.environ.get("GEMINI_API_KEY")
if api_key == None:
    raise RuntimeError('API key needed')

# Create new instance of Gemini client
client = genai.Client(api_key=api_key)

def main():
    # Create parser object
    parser = argparse.ArgumentParser(description = "Prompt for Gemini AI Agent")
    # Define arguments for the parser to accept
    parser.add_argument("user_prompt", type=str, help="The user should enter a prompt that goes to Google Gemini")
    parser.add_argument("--verbose", action = "store_true", help="Enable verbose output")
    args = parser.parse_args()

    messages = [types.Content(role="user", parts=[types.Part(text=args.user_prompt)])]

    response = client.models.generate_content(
        model='gemini-2.5-flash', contents= messages
    )

    # Print Response and token usage
    if (args.verbose):
        print(f'User prompt: {args.user_prompt}')
        print(f'Prompt tokens: {response.usage_metadata.prompt_token_count}')
    print(response.text)  
    if (args.verbose):      
        print(f'Response tokens: {response.usage_metadata.candidates_token_count}')

if __name__ == "__main__":
    main()
