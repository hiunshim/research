from prompts import (
    SYSTEM_FAREWELL_INSTRUCTION,
    SYSTEM_FIND_ORDER_INSTRUCTION,
    SYSTEM_GREETING_INSTRUCTION,
    SYSTEM_MAIN_INSTRUCTION,
    SYSTEM_PRODUCT_INSTRUCTION,
    SYSTEM_RECOMMEND_INSTRUCTION,
    FIND_ORDER_FUNCTION,
    # FIND_PRODUCT_FUNCTION,
    # RECOMMEND_PRODUCT_FUNCTION,
)


class AgentType:
    MAIN = "MAIN"
    GREETING = "GREETING"
    ORDER = "ORDER"
    PRODUCT = "PRODUCT"
    FAREWELL = "FAREWELL"
    RECOMMEND = "RECOMMEND"


INSTRUCTIONS = {
    AgentType.MAIN: SYSTEM_MAIN_INSTRUCTION,
    AgentType.GREETING: SYSTEM_GREETING_INSTRUCTION,
    AgentType.ORDER: SYSTEM_FIND_ORDER_INSTRUCTION,
    AgentType.PRODUCT: SYSTEM_PRODUCT_INSTRUCTION,
    AgentType.RECOMMEND: SYSTEM_RECOMMEND_INSTRUCTION,
    AgentType.FAREWELL: SYSTEM_FAREWELL_INSTRUCTION,
}


FUNCTIONS = {
    AgentType.MAIN: [],
    AgentType.GREETING: [],
    AgentType.ORDER: [FIND_ORDER_FUNCTION],
    AgentType.PRODUCT: [],
    AgentType.RECOMMEND: [],
    # AgentType.PRODUCT: [FIND_PRODUCT_FUNCTION],
    # AgentType.RECOMMEND: [RECOMMEND_PRODUCT_FUNCTION],
    AgentType.FAREWELL: [],
}
