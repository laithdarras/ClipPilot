import pyperclip
import time
import sys
import os
from dotenv import load_dotenv
from openai import OpenAI
from openai._exceptions import APIError, RateLimitError, APITimeoutError

# Load environment variables from .env file
load_dotenv()

# Global client variable
client = None

def load_openai_config():
    """
    Load OpenAI API key from .env file and initialize the OpenAI client.
    """
    global client
    
    # Get API key from environment
    api_key = os.getenv('OPENAI_API_KEY')
    
    if not api_key:
        print("Warning: OPENAI_API_KEY not found in .env file")
        return False
    
    try:
        # Initialize OpenAI client
        client = OpenAI()
        print("OpenAI API configured successfully")
        return True
    except Exception as e:
        print(f"Error initializing OpenAI client: {e}")
        return False


# This function monitors the clipboard for new content and prints it when detected
def monitor_clipboard():
    print("Clipboard Monitor Started...")
    print("Press Ctrl+C to stop monitoring")
    print("=" * 40)
    
    # Store clipboard content
    previous_content = ""
    
    try:
        while True:
            # Read the clipboard content
            current_content = pyperclip.paste()
            
            # Check if content has changed and ignore program's own output
            if (current_content != previous_content and 
                current_content.strip() and 
                "Clipboard Monitor Started" not in current_content and
                "New clipboard content detected" not in current_content):
                print("New clipboard content detected:")
                print(f"Length: {len(current_content)} characters")
                print(f"Content: {current_content}")
                print("=" * 40)
                
                # Get AI summary of the clipboard content
                summary = summarize_content(current_content)
                print("AI Summary:")
                print("-" * 20)
                print(summary)
                print("=" * 40)
                
                # Update content
                previous_content = current_content
            
            time.sleep(1)
            
    except KeyboardInterrupt:
        print("\nClipboard monitoring stopped.")
        sys.exit(0)
    except Exception as e:
        print(f"Error: {e}")
        sys.exit(1)

def summarize_content(text):
    """
    Send clipboard text to GPT-3.5-turbo for summarization.
    Returns a summarized version in 2-3 bullet points.
    """
    global client
    
    try:
        # Check if OpenAI client is configured
        if client is None:
            return "Error: OpenAI API not configured. Please check your .env file."
        
        # Create the system message
        system_message = "Summarize the user's copied content in 2–3 short, clear bullet points."
        
        # Send request to OpenAI
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": system_message},
                {"role": "user", "content": text}
            ],
            max_tokens=150,
            temperature=0.5
        )
        
        # Extract and return the summarized content
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
    # Load OpenAI configuration
    openai_configured = load_openai_config()
    
    # Start clipboard monitoring
    monitor_clipboard()
