from agents.CodeExecutorAgent import getCodeExecutorAgent
from agents.DataAnalyserAgent import getDataAnalyzerAgent

from autogen_agentchat.teams import RoundRobinGroupChat
from autogen_agentchat.conditions import TextMentionTermination

def AnalyzerTeam(docker, model_client):

    codeExecutor = getCodeExecutorAgent(docker)
    dataAnalyzer = getDataAnalyzerAgent(model_client=model_client)
    text_mention_termination = TextMentionTermination('STOP')

    team = RoundRobinGroupChat(
        participants=[dataAnalyzer, codeExecutor],
        description="A data analysis team that iteratively writes and executes Python code to visualize data, compute statistics, and answer queries.",
        max_turns=10,
        termination_condition=text_mention_termination
    )

    return team


