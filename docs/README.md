# AI Coding Assistant

This project is an AI-powered chat interface designed to assist software engineers in rapidly building cross-platform applications. It uses the Flet framework for the UI and the Neurum AI for generating responses.

## Features

- Interactive chat interface
- AI-powered responses for software engineering queries
- Cross-platform compatibility

## Prerequisites

- Python 3.7 or higher
- pip (Python package installer)

## Installation

1. Clone the repository:
   ```
   git clone https://github.com/yourusername/ai_coding_assistant.git
   cd ai_coding_assistant
   ```

2. (Optional) Create and activate a virtual environment:
   ```
   python -m venv venv
   source venv/bin/activate  # On Windows, use: venv\Scripts\activate
   ```

3. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```

## Usage

To run the application, execute the following command in the project directory:
```
python src/main.py
```

This will launch the chat interface. You can then type your software engineering questions or requests, and the AI will provide responses to assist you.

## Project Structure

- `src/main.py`: The entry point of the application
- `src/ui/chat_interface.py`: Contains the UI components and layout
- `src/logic/chat_handler.py`: Handles the chat logic and interaction with the AI service
- `src/utils/ai_service.py`: Manages the interaction with the Neurum AI
- `tests/`: Contains unit tests for the application
- `docs/`: Contains project documentation

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.