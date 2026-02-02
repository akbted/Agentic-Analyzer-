from autogen_agentchat.agents import AssistantAgent
from prompts.DataAnalyzerPrompt import DATA_ANALYZER_MSG

def getDataAnalyzerAgent(model_client):
    
    agentAnalyzer = AssistantAgent(
        name="AnalyzingAgent",
        model_client=model_client,
        description="Agent Responsible in Produce the Python Script and giving it to Code Executor and validating the result",
        system_message=DATA_ANALYZER_MSG
    )

    return agentAnalyzer

