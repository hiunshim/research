from agents.agent import Agent
from constants import (
    INSTRUCTIONS,
    AgentType,
)
from database.utils import (
    product_descriptions,
    load_products,
)


class RecommendAgent(Agent):
    """Handles recommendation-related queries."""

    def __init__(self, llm_client, agent_type=AgentType.RECOMMEND):
        super().__init__(llm_client, agent_type)
        self.messages = [
            {
                "role": "system",
                "content": INSTRUCTIONS[self.agent_type],
            },
            {
                "role": "system",
                "content": f"You have access to the following product JSON data as context. JSON\n{load_products()}\nUse it to recommend a product to the customer.",
            },
            {
                "role": "system",
                "content": f"This is the list of available products and descriptions to recommend: {product_descriptions()}\nOnly recommend from the list of products above. Do not recommend a product not in the list.",
            },
        ]

    def handle(self, user_input):
        message = self.query_llm(user_input, temperature=0.5)
        self.reply(message.content, user_input)
