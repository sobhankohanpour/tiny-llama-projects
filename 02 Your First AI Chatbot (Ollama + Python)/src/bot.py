from typing import Dict

from ollama import ChatResponse, chat


Message = Dict[str, str]


def get_bot_response(model_name: str, user_message: Message) -> str:
    """
    Send a message to the Ollama chat model and return the bot's response text.
    """
    response: ChatResponse = chat(
        model=model_name,
        messages=[
            {
                "role": "system",
                "content": (
                    "Answer in plain text only. "
                    "Do not use markdown, bold, italics, lists, or special formatting. "
                    "Answer very briefly in one to two sentences."
                ),
            },
            user_message,
        ],
    )
    return response["message"]["content"]


def main() -> None:
    """
    Run the interactive chatbot loop.
    """
    print("Welcome to your personal AI chatbot.")
    print("This bot has no memory. Feel free to ask any question.")
    print("Enter 'Q' or 'q' to exit the chat.")

    model_name: str = "qwen3:0.6b"

    while True:
        user_input: str = input("You: ").strip()

        if user_input.lower() == "q":
            break

        user_message: Message = {
            "role": "user",
            "content": user_input,
        }

        bot_reply: str = get_bot_response(
            model_name=model_name,
            user_message=user_message,
        )

        print(f"Robot: {bot_reply}")
    
    print("Robot: Goodbye, see you later.")


if __name__ == "__main__":
    main()
