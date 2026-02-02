from autogen_ext.models.anthropic import AnthropicChatCompletionClient
import logging

logger = logging.getLogger(__file__)

def getModelClient():
    anthropic_client = AnthropicChatCompletionClient(model="claude-3-7-sonnet-20250219")
    return anthropic_client

async def close_model_cleint(model_client):
    logger.info("Closing the Model Client!")
    await model_client.close()
    


