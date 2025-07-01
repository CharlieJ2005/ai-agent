import os
import sys
from dotenv import load_dotenv
from google import genai
from google.genai import types
from functions.call_function import call_function, available_functions
from prompts import system_prompt


def get_api_key():
    load_dotenv()
    api_key = os.environ.get("GEMINI_API_KEY")
    if not api_key:
        print("Error: GEMINI_API_KEY not set in environment.")
        sys.exit(1)
    return api_key


def get_client(api_key):
    return genai.Client(api_key=api_key)


def main():
    
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <prompt> [--verbose]")
        sys.exit(1)

    args = sys.argv[1:]
    prompt_words = []
    flags = []

    for arg in args:
        if arg.startswith("--"):
            flags.append(arg)
        else:
            prompt_words.append(arg)

    user_prompt = " ".join(prompt_words)
    verbose = "--verbose" in flags

    api_key = get_api_key()
    client = get_client(api_key)

    messages = [
        types.Content(role="user", parts=[types.Part(text=user_prompt)]),
    ]

    try:
        response = client.models.generate_content(
            model="gemini-2.0-flash-001",
            contents=messages,
            config=types.GenerateContentConfig(
                tools=[available_functions],
                system_instruction=system_prompt
            )
        )
        if not response.function_calls:
            return response.text
        
        prompt_tokens = response.usage_metadata.prompt_token_count
        response_tokens = response.usage_metadata.candidates_token_count
        if verbose:
            print(f"User prompt: {user_prompt}")
            print(f"Prompt tokens: {prompt_tokens}")
            print(f"Response tokens: {response_tokens}")
        
        function_responses = []
        for function_call_part in response.function_calls:
            function_call_result = call_function(function_call_part, verbose)
            if (
                not function_call_result.parts
                or not function_call_result.parts[0].function_response
            ):
                raise Exception("empty result")
            if verbose:
                print(f"-> {function_call_result.parts[0].function_response.response}")
            function_responses.append(function_call_result.parts[0])
        
        if not function_responses:
            raise Exception("no function responses generated")
            
    except Exception as e:
        print(f"Error during API call: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()
