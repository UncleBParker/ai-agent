# main.py

import os
import argparse
import config
from dotenv import load_dotenv
from google import genai
from google.genai import types
from prompts import system_prompt
from call_function import available_functions, call_function


load_dotenv()
api_key = os.environ.get("GEMINI_API_KEY" if config.KEY == 0 else "ALT_GEMINI_API_KEY")
if not api_key:
    raise RuntimeError(
        "GEMINI_API_KEY environment variable not set. "
        ".env file or GEMINI_API_KEY object missing"
    )
client = genai.Client(api_key=api_key)
model_name = "gemini-2.5-flash"


def parse_args():
    parser = argparse.ArgumentParser(description="Bootdev Chatbot")
    parser.add_argument("user_prompt", type=str, help="Prompt to send to Gemini")
    parser.add_argument("--verbose", action="store_true", help="Enable verbose output")
    return parser.parse_args()


def main():
    
    print("\nRunning ai-agent!")

    args = parse_args()
    user_prompt = args.user_prompt
    messages = [types.Content(role="user", parts=[types.Part(text=user_prompt)])]


    try:
        response = client.models.generate_content(
            model=model_name,
            contents=messages,
            config=types.GenerateContentConfig(system_instruction=system_prompt, temperature=config.TEMP, tools=[available_functions]),
        )
    except Exception as e:
        raise RuntimeError(f"Gemini API request failed: {e}") from e
    
    usage_metadata = response.usage_metadata
    func_calls = response.function_calls

    prompt_token_count = usage_metadata.prompt_token_count
    canidates_token_count = usage_metadata.candidates_token_count

    if func_calls:
        function_results = []
        for call in func_calls:
            function_call_result = call_function(call, verbose=args.verbose)

            if function_call_result.parts == []:
                raise Exception(f'in function_call_result for "{call.name}": types.Content.parts is an empty list')
            if function_call_result.parts[0].function_response == None:
                raise Exception(f'in function_call_result for "{call.name}": FunctionResponse object is "None"')
            if function_call_result.parts[0].function_response.response == None:
                raise Exception(f'in function_call_result for "{call.name}": RunctionsResponse.response object is "None"')
            function_results.append(function_call_result.parts[0])
            
            if args.verbose:
                print(f"-> {function_call_result.parts[0].function_response.response}")
    else:
        if args.verbose:
            print(f"\nUser prompt: {user_prompt}\n")   
            print(f"Prompt tokens: {prompt_token_count}")
            print(f"Response tokens: {canidates_token_count}\n")
        print(f"Response:\n{response.text}\n")



if __name__ == "__main__":
    main()
