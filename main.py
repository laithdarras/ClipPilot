import pyperclip
import time
import sys


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
                
                # Update content
                previous_content = current_content
            
            time.sleep(1)
            
    except KeyboardInterrupt:
        print("\nClipboard monitoring stopped.")
        sys.exit(0)
    except Exception as e:
        print(f"Error: {e}")
        sys.exit(1)

if __name__ == "__main__":
    monitor_clipboard()
