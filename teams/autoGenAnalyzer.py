from agents.CodeExecutorAgent import getCodeExecutorAgent
from agents.DataAnalyserAgent import getDataAnalyzerAgent
from utils.model_client import getModelClient

from autogen_agentchat.teams import RoundRobinGroupChat

def AnalyzerTeam(docker):

    codeExecutor = getCodeExecutorAgent(docker)
    dataAnalyzer = getDataAnalyzerAgent(model_client=getModelClient())

    team = RoundRobinGroupChat(
        participants=[dataAnalyzer, codeExecutor],
        description="A data analysis team that iteratively writes and executes Python code to visualize data, compute statistics, and answer queries.",
        max_turns=10,
        termination_condition=None
    )

    return team


