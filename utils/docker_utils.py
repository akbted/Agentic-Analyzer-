from autogen_ext.code_executors.docker import DockerCommandLineCodeExecutor
from config.settings import DOCKER_WORKING_DIR
import logging

logger = logging.getLogger(__file__)

def getDockerClient():
    docker = DockerCommandLineCodeExecutor(
        work_dir=DOCKER_WORKING_DIR,
        timeout=120
    )
    return docker

async def startDocker(docker):
    logger.info("Starting Docker Container")
    await docker.start()

async def stopDocker(docker):
    logger.info("Starting Docker Container")
    await docker.stop()