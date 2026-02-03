# Library imports
import os
import argparse
from dotenv import load_dotenv
from google import genai
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
    args = parser.parse_args()

    response = client.models.generate_content(
        model='gemini-2.5-flash', contents= args.user_prompt
    )
    print(f'Prompt tokens: {response.usage_metadata.prompt_token_count}')
    print(response.text)        
    print(f'Response tokens: {response.usage_metadata.candidates_token_count}')

if __name__ == "__main__":
    main()
