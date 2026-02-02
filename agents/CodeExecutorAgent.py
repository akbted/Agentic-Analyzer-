from autogen_agentchat.agents import CodeExecutorAgent
from autogen_agentchat.messages import TextMessage
from utils.docker_utils import getDockerClient, startDocker, stopDocker
from autogen_core import CancellationToken
import asyncio

def getCodeExecutorAgent(codeExecutor):

    codeExecutor = CodeExecutorAgent(
        name="CodeExecutorAgent",
        description="Agent to Execute Python Code in Docker Container",
        code_executor=codeExecutor,
    )

    return codeExecutor

# Testing Code Executor
async def main():

    # Start the docker container
    try:
        docker = getDockerClient()
        await startDocker(docker)

        codeexecutor = getCodeExecutorAgent(docker)

        task = TextMessage(content='''Here is some code
```python
print('Hello world')
```
''', source= "user")
        
        response = await codeexecutor.on_messages([task], cancellation_token=CancellationToken())
        print(response)

    except Exception as e:
        print(f"Error - {e}")

    finally:
        await stopDocker(docker)

if __name__ == "__main__":
    asyncio.run(main())