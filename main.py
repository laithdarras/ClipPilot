import pyperclip    # for accessing clipboard content
import time    # for timing
import sys    # for system operations
import os    # for operating system operations
from dotenv import load_dotenv   # for loading environment variables from env file
from openai import OpenAI    # for interacting with openai api
from openai._exceptions import APIError, RateLimitError, APITimeoutError    # for handling errors

load_dotenv()

# global
client = None

# initialize openai client with api key
def load_openai_config():
    global client
    
    api_key = os.getenv('OPENAI_API_KEY')
    
    if not api_key:
        print("Warning: OPENAI_API_KEY not found in .env file")
        return False
    
    try:
        # initialize client
        client = OpenAI()
        return True
    except Exception as error:
        print(f"Error initializing OpenAI client: {error}")
        return False


# monitor clipboard for new content
def monitor_clipboard():
    print("Clipboard Monitor Started...")
    print("Press Ctrl+C to stop monitoring")
    print("=" * 40)
    
    # store content
    previous_content = ""
    
    try:
        while True:
            # reading
            current_content = pyperclip.paste()
            
            # This checks if content has changed and ignores program's own output
            if (current_content != previous_content and 
                current_content.strip() and 
                "Clipboard Monitor Started" not in current_content and
                "New clipboard content detected" not in current_content):
                print("New clipboard content detected:")
                print(f"Length: {len(current_content)} characters")
                print(f"Content: {current_content}")
                print("=" * 40)
                
                # AI summary
                summary = summarize_content(current_content)
                print("AI Summary:")
                print("-" * 20)
                print(summary)
                print("=" * 40)
                
                # update
                previous_content = current_content
            
            time.sleep(1)
            
    except KeyboardInterrupt:
        print("\nClipboard monitoring stopped. Goodbye!")
        sys.exit(0)
    except Exception as error:
        print(f"Error: {error}")
        sys.exit(1)

# summarize text using api
def summarize_content(text):
    global client
    
    try:
        if client is None:
            return "Error: OpenAI API not configured."
        
        # prompting the model
        system_message = "Summarize the user's copied content in 2–3 short, clear bullet points."
        
        # send request to OpenAI
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": system_message},
                {"role": "user", "content": text}
            ],
            max_tokens=150,    # 150 tokens for short bullet points
            temperature=0.5    # chose for a good balance of focused and creative responses
        )
        
        # extract and return the summarized content
        summary = response.choices[0].message.content.strip()
        return summary
        
    except RateLimitError:
        return "Error: Rate limit exceeded. Please wait a moment before trying again."
    except APITimeoutError:
        return "Error: Request timed out. Please check your internet connection."
    except APIError as e:
        return f"Error: OpenAI API error - {str(e)}"
    except Exception as e:
        return f"Error: Failed to summarize content - {str(e)}"

if __name__ == "__main__":
    openai_configured = load_openai_config()

    monitor_clipboard()