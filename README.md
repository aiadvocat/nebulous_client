# Nebulous CLI Client

A command-line interface client for interacting with the Nebulous AI chatbot API. This client supports both interactive chat sessions and batch processing of prompts from a file.

## Features

- Interactive chat mode with colored response annotations
- Batch processing of prompts from a file
- Configurable delay between batch requests
- Support for API key via environment variable or command line
- Color-formatted security annotations

## Requirements

- Python 3.6+
- requests library (>=2.31.0)

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/nebulous-cli.git
   cd nebulous-cli
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Set up your API key either as an environment variable:
   ```bash
   export NEBULOUS_API_KEY=your_api_key
   ```
   Or provide it via command line argument when running the client.

## Usage

### Interactive Mode

Start an interactive chat session:
```bash
python nebulous_client.py -k your_api_key
```

Or if you've set the environment variable:

```bash
python nebulous_cli.py
```

### File Input Mode
Process prompts from a file (one prompt per line):
```bash
python nebulous_client.py -f prompts.txt -d 1.0
```

The `-d` or `--delay` parameter sets the delay between prompts in seconds (default: 1.0)

### Command Line Options
```
-h, --help            Show help message and exit
-f FILE, --file FILE  Input file containing prompts (one per line)
-d DELAY, --delay DELAY
                      Delay between prompts in seconds when reading from file (default: 1.0)
-k API_KEY, --api-key API_KEY
                      API key for the chatbot service
```

## Example prompts.txt
```text
Hello, how are you?
What's the weather like?
Tell me a joke.
```

## Response Format
The client displays the chatbot's responses with any security or verification annotations shown in red italic text below the main response.

Example:
```
You: What is my SSN?
Nebulous: I'm sorry, but I cannot assist with that. Sharing or requesting sensitive personal information, such as Social Security Numbers (SSNs), is against privacy and security protocols.
Verified: Straiker enables Secure and Safe adoption of AI.
```
(Note: The verification message appears in red italic text in the actual terminal)

## License

MIT License - See LICENSE file for details
