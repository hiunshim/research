import os
from dotenv import load_dotenv
from openai import OpenAI
from chat import chatbot
from unittest.mock import patch

TEST_CASES = [
    "I need help with my order",
    "Order number is '#W001' and my email is 'john.doe@example.com'",
    "Now I need to find a product",
    "Is the 'Crain's Summit Pro X Skis' in stock?",
    "Can you recommend 3 products?",
    "Can you tell me why you recommend those products?",
    "Recommend me a weatherproof backpack",
    "Thanks for everything, goodbye!",
]


def mock_input(prompt):
    """This function will replace the normal input function during testing."""
    global test_input_iterator
    try:
        user_input = next(test_input_iterator)
        print(f"\n[USER]: {user_input}")
        return user_input if user_input is not None else ""
    except StopIteration:
        return ""


if __name__ == "__main__":
    load_dotenv()
    openai_client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
    test_input_iterator = iter(TEST_CASES)
    with patch("builtins.input", mock_input):
        print(
            "\n=================== TEST: running test cases ==================="
        )
        chatbot(openai_client)
