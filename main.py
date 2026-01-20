import os
from dotenv import load_dotenv
from google import genai

load_dotenv()
api_key = os.environ.get("GEMINI_API_KEY")
if api_key == None:
    raise RuntimeError(f"api-key == None")
    
client = genai.Client(api_key=api_key)

def main():
    
    print("Hello from ai-agent!")

    contents = "Why is Boot.dev such a great place to learn backend development? Use one paragraph maximum."

    response = client.models.generate_content(model='gemini-2.5-flash', contents=contents)
    
    usage_metadata = response.usage_metadata
    if usage_metadata == None:
        raise RuntimeError("usage_metadata == None / Failed API Request")
    
    prompt_token_count = usage_metadata.prompt_token_count
    canidates_token_count = usage_metadata.candidates_token_count

    print(f"User Prompt: {contents}")

    print(f"Prompt tokens: {prompt_token_count}")
    print(f"Response tokens: {canidates_token_count}")

    print(f"Response:\n{response.text}")



if __name__ == "__main__":
    main()
