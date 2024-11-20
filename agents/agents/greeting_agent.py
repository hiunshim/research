from agents.agent import Agent
from constants import INSTRUCTIONS, AgentType


class GreetingAgent(Agent):
    """Handles greetings and routing to other agents."""

    def __init__(self, llm_client, agent_type=AgentType.GREETING):
        super().__init__(
            llm_client,
            agent_type,
        )
        self.messages = [
            {
                "role": "system",
                "content": INSTRUCTIONS[self.agent_type],
            }
        ]

    def handle(self, user_input):
        message = self.query_llm(user_input)
        self.reply(message.content, user_input)