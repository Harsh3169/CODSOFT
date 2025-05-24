# Task 1: Chatbot with Rule-Based Responses

## Overview
This is a simple rule-based chatbot developed as part of the CodSoft Artificial Intelligence Internship. The chatbot uses predefined responses and basic pattern matching (via regular expressions) to simulate conversation with a user.

## Features
- Responds to greetings and common queries like name, age, weather, etc.
- Uses `re.search` for basic keyword matching
- Gracefully handles unknown inputs
- Exits when the user types "bye"

## Technologies Used
- Python 3
- `re` module for pattern matching

## How It Works
The chatbot continuously takes user input in a loop and matches it against a predefined set of response patterns using regular expressions. If a pattern is matched, a response is returned. Otherwise, a default message is shown.

## How to Run
1. Clone the repository or download the `aichatbot.py` file.
2. Open a terminal and navigate to the directory.
3. Run the chatbot with:
   ```bash
   python aichatbot.py
