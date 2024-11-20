from agents.agent import Agent
from constants import (
    INSTRUCTIONS,
    AgentType,
)
from database.utils import (
    product_inventory,
    load_products,
)


class ProductAgent(Agent):
    """Handles product-related queries."""

    def __init__(self, llm_client, agent_type=AgentType.PRODUCT):
        super().__init__(llm_client, agent_type)
        self.messages = [
            {
                "role": "system",
                "content": INSTRUCTIONS[self.agent_type],
            },
            {
                "role": "system",
                "content": f"You have access to the following product JSON data as context. JSON\n{load_products()}\nUse it to find a product and the inventory.",
            },
            {
                "role": "system",
                "content": f"These are the items in stock: {product_inventory()}",
            },
        ]

    def handle(self, user_input):
        """Processes user input and calls the appropriate function."""
        message = self.query_llm(user_input, temperature=0.5)
        self.reply(message.content, user_input)
