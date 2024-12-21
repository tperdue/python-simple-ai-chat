# Simple AI Chat with Memory (Python Version)

A lightweight, Python-based chat application that interacts with OpenAI's GPT models and maintains conversation history using a JSON database. This project demonstrates implementation of:
- Modern Python practices with type hints
- AI integration with OpenAI's GPT models
- Persistent data storage
- Clean architecture principles
- Asynchronous programming with Python
- Pydantic for data validation and serialization

## Features

- 🐍 Modern Python with type hints and async support
- 🤖 OpenAI GPT integration for intelligent responses
- 💾 Persistent chat history using JSON file storage
- 📝 Pydantic models for data validation and serialization
- 🎨 Colorful terminal interface with Colorama
- 🚀 Clean, maintainable codebase
- 🔄 Asynchronous message handling
- 📦 Minimal dependencies

## Technical Overview

### Project Structure

```
python-ai-chat/
├── .env                # Environment variables
├── requirements.txt    # Python dependencies
├── db.json            # Database storage
├── models.py          # Pydantic models and type definitions
├── memory.py          # Database operations
├── chat.py            # Chat logic and OpenAI integration
└── main.py            # Main application entry point
```

### Key Components

#### Memory Management
The application uses JSON-based storage with Python's built-in json module, featuring:
- Persistent message history
- Message metadata (UUIDs, timestamps)
- Asynchronous database operations
- Type-safe data handling with Pydantic

#### Chat System
Built with OpenAI's GPT models, implementing:
- Customizable system prompts
- Full conversation context
- Robust error handling
- Type validation with Pydantic models

#### Database Structure
Messages are stored in a structured JSON format:
```json
{
  "messages": [
    {
      "role": "user",
      "content": "Hello!",
      "id": "123e4567-e89b-12d3-a456-426614174000",
      "created_at": "2024-03-20T10:00:00.000Z"
    }
  ]
}
```

## Getting Started

### Prerequisites

- Python 3.8 or higher
- pip (Python Package Installer)
- OpenAI API key
- Virtual environment (recommended)

### Installation

1. Clone the repository:
```bash
git clone https://github.com/yourusername/python-ai-chat.git
cd python-ai-chat
```

2. Create and activate a virtual environment:
```bash
# On Windows
python -m venv venv
.\venv\Scripts\activate

# On Unix or MacOS
python -m venv venv
source venv/bin/activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Create a `.env` file in the root directory and add your OpenAI API key:
```bash
OPENAI_API_KEY=your_api_key_here
```

### Usage

Start the chat application:
```bash
python main.py
```

## Dependencies

Key dependencies include:
- `openai`: OpenAI API client
- `pydantic`: Data validation and serialization
- `python-dotenv`: Environment variable management
- `colorama`: Terminal color support

## Development Notes

### Type Hints
The project uses Python's type hints and Pydantic models for type safety:
```python
from pydantic import BaseModel
from typing import List, Literal

class ChatMessage(BaseModel):
    role: Literal["user", "assistant"]
    content: str
    id: str
    created_at: str
```

### Async Support
The application uses Python's asyncio for asynchronous operations:
```python
async def chat(user_input: str) -> Optional[str]:
    # Async chat implementation
```

## License

This project is licensed under the MIT License. Feel free to fork and modify for your own use.

## Professional Contact

I'm open to exciting opportunities and collaborations in software development, particularly in:
- Backend Web Development
- AI/ML Integration
- Python Projects
- Analytics Engineering

### Let's Connect
- 📧 Email: timaperduejr@gmail.com
- 💼 LinkedIn: [Tim Perdue](https://www.linkedin.com/in/tperdue/)

If you're interested in discussing potential opportunities or would like to learn more about my work, feel free to reach out through any of the channels above.