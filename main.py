from teams.autoGenAnalyzer import AnalyzerTeam
from models.model_client import getModelClient, close_model_client
from utils.docker_utils import getDockerClient, startDocker, stopDocker
import logging
import asyncio
from autogen_agentchat.messages import TextMessage
from autogen_agentchat.base import TaskResult

logger = logging.getLogger(__file__)

async def main():
    logger.info("Starting MultiAgent Analyzer")

    docker = getDockerClient()
    model_client = getModelClient()

    try:
        await startDocker(docker)
        multi_agent_team = AnalyzerTeam(docker, model_client)
        stream = multi_agent_team.run_stream(task="Analyse the teams training and tell me the topics each person has done.", )
        
        async for message in stream:
            if isinstance(message, TextMessage):
                print(message.source, ":", message.content)
            if isinstance(message, TaskResult):
                print("Stop Reason :" , message.stop_reason)
        
    except Exception as e:
        print(f"Error - {e}")

    finally:
        await stopDocker(docker)
        await close_model_client(model_client)


if __name__ == "__main__":
    asyncio.run(main())
