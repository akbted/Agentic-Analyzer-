from teams.autoGenAnalyzer import AnalyzerTeam
from utils.model_client import getModelClient, close_model_client
from utils.docker_utils import getDockerClient, startDocker, stopDocker
import logging
import asyncio

logger = logging.getLogger(__file__)

async def main():
    logger.info("Starting MultiAgent Analyzer")

    docker = getDockerClient()
    model_client = getModelClient()

    try:
        await startDocker(docker)
        multi_agent_team = AnalyzerTeam(docker, model_client)
        stream = multi_agent_team.run_stream(task="How many files are there in temp folder? If there are any pdf files tell me what is it about ?", )
        
        async for message in stream:
            print(message)
        
    
    except Exception as e:
        print(f"Error - {e}")

    finally:
        await stopDocker(docker)


if __name__ == "__main__":
    asyncio.run(main())
