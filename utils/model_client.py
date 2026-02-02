from autogen_ext.models.anthropic import AnthropicChatCompletionClient
import logging
from dotenv import load_dotenv
import os

load_dotenv()

logger = logging.getLogger(__file__)

MODEL_API_KEY = os.getenv("CLAUDE_API_KEY")

if MODEL_API_KEY is None:
    logger.info("API KEY NOT CREATED OR UPDATED IN .ENV")

def getModelClient():
    anthropic_client = AnthropicChatCompletionClient(model="claude-3-7-sonnet-20250219", api_key=MODEL_API_KEY)
    return anthropic_client

async def close_model_cleint(model_client):
    logger.info("Closing the Model Client!")
    await model_client.close()



