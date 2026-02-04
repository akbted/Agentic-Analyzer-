from autogen_ext.models.anthropic import AnthropicChatCompletionClient
from autogen_ext.models.ollama import OllamaChatCompletionClient
from autogen_ext.models.openai import OpenAIChatCompletionClient
import logging
from dotenv import load_dotenv
import os

load_dotenv()

logger = logging.getLogger(__file__)

MODEL_API_KEY = os.getenv("CLAUDE_API_KEY")
OPEN_AI_MODEL_KEY = os.getenv("OPENAI_API_KEY")

if MODEL_API_KEY is None:
    logger.info("API KEY NOT CREATED OR UPDATED IN .ENV")

# def getModelClient():
#     anthropic_client = AnthropicChatCompletionClient(model="claude-3-7-sonnet-20250219", api_key=MODEL_API_KEY)
#     return anthropic_client

# def getModelClient():
#     ollama_model_client = OllamaChatCompletionClient(model="qwen2.5:7b")
#     return ollama_model_client


def getModelClient():
    openai_model_client = OpenAIChatCompletionClient(
    model="gpt-4o-2024-08-06",
    api_key=OPEN_AI_MODEL_KEY, 
)
    return openai_model_client



async def close_model_client(model_client):
    logger.info("Closing the Model Client!")
    await model_client.close()



