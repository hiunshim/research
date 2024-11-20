import json

from agents.agent import Agent
from constants import INSTRUCTIONS, AgentType
from database.utils import find_order, load_orders


class OrderAgent(Agent):
    """Handles order-related queries."""

    def __init__(self, llm_client, agent_type=AgentType.ORDER):
        super().__init__(llm_client, agent_type)
        self.messages = [
            {
                "role": "system",
                "content": INSTRUCTIONS[self.agent_type],
            },
            {
                "role": "system",
                "content": f"You have access to the following order JSON data as context. JSON\n\n{load_orders()}\n\nUse it answer status related questions of the customer.",
            },
        ]

    def handle(self, user_input):
        message = self.query_llm(user_input)
        if message.function_call:
            arguments = json.loads(message.function_call.arguments)
            email = arguments.get("email")
            order_number = arguments.get("order_number")

            if email or order_number:
                order = find_order(email, order_number)
                if order:
                    self.messages.append(
                        {
                            "role": "assistant",
                            "content": f"Order found:\n{order}",
                        }
                    )
                    self.messages.append(
                        {
                            "role": "system",
                            "content": "An order has been found, so answer their inquiries about the order status and tracking link.",
                        }
                    )
                else:
                    self.messages.append(
                        {
                            "role": "assistant",
                            "content": f"No order found for OrderNumer: {order_number}",
                        }
                    )
                    self.messages.append(
                        {
                            "role": "system",
                            "content": "An order was not found. Ask if the customer can provide more details.",
                        }
                    )
            message = self.query_llm(user_input)
        self.reply(message.content, user_input)
