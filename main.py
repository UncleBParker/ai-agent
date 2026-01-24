import os
import argparse
from dotenv import load_dotenv
from google import genai
from google.genai import types


load_dotenv()
api_key = os.environ.get("GEMINI_API_KEY")
if not api_key:
    raise RuntimeError(
        "GEMINI_API_KEY environment variable not set. "
        ".env file or GEMINI_API_KEY object missing"
    )
client = genai.Client(api_key=api_key)


def parse_args():
    parser = argparse.ArgumentParser(description="Bootdev Chatbot")
    parser.add_argument("user_prompt", type=str, help="Prompt to send to Gemini")
    parser.add_argument("--verbose", action="store_true", help="Enable verbose output")
    return parser.parse_args()


def main():
    
    print("\nRunning ai-agent!")

    args = parse_args()
    contents = args.user_prompt
    messages = [types.Content(role="user", parts=[types.Part(text=args.user_prompt)])]

    print(f"User Prompt: {contents}\n")

    try:
        response = client.models.generate_content(
            model="gemini-2.5-flash", contents=messages
        )
    except Exception as e:
        raise RuntimeError(f"Gemini API request failed: {e}") from e
    
    usage_metadata = response.usage_metadata
    
    prompt_token_count = usage_metadata.prompt_token_count
    canidates_token_count = usage_metadata.candidates_token_count

    print(f"Prompt tokens: {prompt_token_count}")
    print(f"Response tokens: {canidates_token_count}")
    print(f"Response:\n{response.text}\n")



if __name__ == "__main__":
    main()
