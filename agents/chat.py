import os

from dotenv import load_dotenv
from openai import OpenAI

from agents import (
    GreetingAgent,
    OrderAgent,
    MainAgent,
    ProductAgent,
    RecommendAgent,
    FarewellAgent,
)
from constants import AgentType


def chatbot(llm_client):
    """Main chatbot interface."""
    agents = {
        AgentType.GREETING: GreetingAgent(llm_client),
        AgentType.ORDER: OrderAgent(llm_client),
        AgentType.MAIN: MainAgent(llm_client),
        AgentType.PRODUCT: ProductAgent(llm_client),
        AgentType.RECOMMEND: RecommendAgent(llm_client),
        AgentType.FAREWELL: FarewellAgent(llm_client),
    }

    # Remove if users should initiate chat first
    agents[AgentType.GREETING].handle(
        "I love outdoors so greet me in the most extravagant way possible, as if you will fulfill my dreams"
    )
    next_agent_name = AgentType.MAIN
    while next_agent_name != AgentType.FAREWELL:
        agent = agents[next_agent_name]
        next_agent_name, user_input = agent.route()
        agents[next_agent_name].handle(user_input)


if __name__ == "__main__":
    load_dotenv()
    openai_client = OpenAI(
        api_key=os.getenv("OPENAI_API_KEY"),
    )
    chatbot(openai_client)
