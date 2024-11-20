from agents.agent import Agent
from constants import AgentType, INSTRUCTIONS


class FarewellAgent(Agent):
    """Handles end of conversation."""

    def __init__(self, llm_client, agent_type=AgentType.FAREWELL):
        super().__init__(llm_client, agent_type)
        self.messages = [
            {
                "role": "system",
                "content": INSTRUCTIONS[self.agent_type],
            }
        ]

    def handle(self, user_input):
        message = self.query_llm(user_input)
        self.reply(message.content, user_input)
