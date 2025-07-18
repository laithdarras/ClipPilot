# ClipboardAI

A real-time clipboard monitoring tool that automatically summarizes copied text using OpenAI's GPT-3.5-turbo. Perfect for devs and others who want to stay focused while working with long-form content.

![Demo](demo.gif)

## Features

- **Real-time monitoring**: Automatically detects new clipboard content
- **AI-powered summarization**: Uses OpenAI GPT-3.5-turbo for text summarization
- **Clean terminal UI**: Formatted output with clear separation between content and summaries
- **Error handling**: Robust error handling for API rate limits, timeouts, and network issues
- **Cross-platform**: Works on Windows, macOS, and Linux
- **Lightweight**: Minimal dependencies and fast performance

## Installation

### Prerequisites

- Python 3.7 or higher
- pip package manager
- OpenAI API key

### Setup

1. **Clone the repository**

   ```bash
   git clone <repository-url>
   cd clipboardai
   ```

2. **Install dependencies**

   ```bash
   pip install -r requirements.txt
   ```

3. **Configure OpenAI API**

   Create a `.env` file in the project root:

   ```bash
   # .env
   OPENAI_API_KEY=your_openai_api_key_here
   ```

   Get your API key from [OpenAI Platform](https://platform.openai.com/api-keys)

## Usage

1. **Start the clipboard monitor**

   ```bash
   python main.py
   ```

2. **Copy text to clipboard**

   - The tool will automatically detect new content
   - AI summaries will be displayed in the terminal

3. **Stop monitoring**
   - Press `Ctrl+C` to exit

### Example Output

```
Clipboard Monitor Started...
Press Ctrl+C to stop monitoring
========================================
New clipboard content detected:
Length: 1250 characters
Content: [Your copied text here]
========================================
AI Summary:
--------------------
• Key point 1 about the content
• Key point 2 about the content
• Key point 3 about the content
========================================
```

## Dependencies

- **pyperclip**: Cross-platform clipboard access
- **openai**: OpenAI API client
- **python-dotenv**: Environment variable management

## Configuration

### Environment Variables

| Variable         | Description         | Required |
| ---------------- | ------------------- | -------- |
| `OPENAI_API_KEY` | Your OpenAI API key | Yes      |

### API Settings

The tool uses the following OpenAI API settings:

- **Model**: `gpt-3.5-turbo`
- **Max tokens**: 150 (for concise summaries)
- **Temperature**: 0.5 (balanced creativity and focus)

## Troubleshooting

### Common Issues

**"OPENAI_API_KEY not found"**

- Ensure your `.env` file exists and contains the API key
- Check that the key is valid and has sufficient credits

**"Rate limit exceeded"**

- Wait a moment before copying new content
- Consider upgrading your OpenAI plan if needed

**"Request timed out"**

- Check your internet connection
- Try again in a few moments

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## Support

If you encounter any issues or have questions, please open an issue on GitHub.