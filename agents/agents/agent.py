import json

from constants import AgentType, FUNCTIONS
from prompts import (
    SYSTEM_MAIN_INSTRUCTION,
    EXTRACT_INTENT_FUNCTION,
    SYSTEM_ROUTING_INSTRUCTION,
)


class Agent:
    """Base class for all agents with common routing functionality."""

    def __init__(self, llm_client, agent_type):
        self.llm_client = llm_client
        self.agent_type = agent_type
        self.used_counter = 0

    def handle(self, user_input, globa_messages):
        """To be implemented by subclasses. Processes user input."""
        raise NotImplementedError("Subclasses must implement this method.")

    def route(self):
        """Route to the appropriate agent based on user input."""
        self._increment_used_counter()
        user_input = input("\n[USER]: ").strip().lower()
        messages = [
            {
                "role": "system",
                "content": SYSTEM_ROUTING_INSTRUCTION,
            },
            {
                "role": "user",
                "content": user_input,
            },
        ]

        chat_completion = self.llm_client.chat.completions.create(
            model="gpt-4o",
            messages=messages,
            functions=[EXTRACT_INTENT_FUNCTION],
        )
        choice = chat_completion.choices[0]
        message = choice.message

        next_agent = AgentType.MAIN
        if message.function_call:
            arguments = json.loads(message.function_call.arguments)
            intent = arguments.get("intent")
            if AgentType.ORDER == intent:
                next_agent = AgentType.ORDER
            if AgentType.PRODUCT == intent:
                next_agent = AgentType.PRODUCT
            if AgentType.RECOMMEND == intent:
                next_agent = AgentType.RECOMMEND
            if AgentType.FAREWELL == intent:
                next_agent = AgentType.FAREWELL
        return next_agent, user_input

    def query_llm(
        self,
        user_input,
        functions=None,
        temperature=1,
    ):
        self.messages.append(
            {
                "role": "user",
                "content": user_input,
            },
        )
        chat_completion = self.llm_client.chat.completions.create(
            model="gpt-4o",
            messages=self.messages,
            functions=FUNCTIONS[self.agent_type] or functions,
            temperature=temperature,
        )
        choice = chat_completion.choices[0]
        message = choice.message
        if message.content:
            self.messages.append(
                {
                    "role": "assistant",
                    "content": message.content,
                }
            )
        return message

    def reply(self, content, user_input):
        print(
            f"\n[{self.agent_type} ASSISTANT]: ",
            self._handle_empty_content(content, user_input),
        )

    def _increment_used_counter(self):
        self.used_counter += 1

    def _handle_empty_content(self, content, user_input):
        if content:
            return content
        # fall back if the first query fails
        messages = [
            {
                "role": "system",
                "content": SYSTEM_MAIN_INSTRUCTION,
            },
            {
                "role": "user",
                "content": user_input,
            },
        ]
        chat_completion = self.llm_client.chat.completions.create(
            model="gpt-4o", messages=messages
        )
        # fallback. will not happen unless openai api fails
        if not (
            chat_completion
            or chat_completion.choices
            or chat_completion.choices[0]
            or chat_completion.choices[0].message
            or chat_completion.choices[0].message.content
        ):
            return "Sorry I couldn't process your message. Could you please repeat?"
        return chat_completion.choices[0].message.content

    def __repr__(self):
        return f"""
            Agent: {self.agent_type}
        """
