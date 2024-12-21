import json
import os
from typing import Dict, List, Optional
from models import ChatMessage, DB

DEFAULT_DB_FILE = "db.json"

def initialize_db(db_file: str = DEFAULT_DB_FILE) -> None:
    """Initialize the database file if it doesn't exist."""
    if not os.path.exists(db_file):
        empty_db = DB()
        with open(db_file, 'w') as f:
            json.dump(empty_db.model_dump(), f, indent=2)

def get_db(db_file: str = DEFAULT_DB_FILE) -> DB:
    """Get the database, initializing it if necessary."""
    initialize_db(db_file)
    try:
        with open(db_file, 'r') as f:
            data = json.load(f)
            return DB(**data)
    except (FileNotFoundError, json.JSONDecodeError):
        # If there's any issue with the file, return a fresh DB
        return DB()

def save_db(db: DB, db_file: str = DEFAULT_DB_FILE) -> None:
    """Save the database to file."""
    with open(db_file, 'w') as f:
        json.dump(db.model_dump(), f, indent=2)

def add_message(message_data: Dict) -> ChatMessage:
    """Add a new message to the database."""
    db = get_db()
    message = ChatMessage(**message_data)
    db.messages.append(message)
    save_db(db)
    return message

def get_messages() -> List[ChatMessage]:
    """Get all messages from the database."""
    db = get_db()
    return db.messages

# Initialize the database when the module is imported
initialize_db()