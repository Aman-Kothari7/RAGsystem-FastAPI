#Neccesary imports 
from dotenv import load_dotenv
from save_notes import note_engine
from llama_index.core.tools import QueryEngineTool, ToolMetadata
from llama_index.core.agent import ReActAgent
from llama_index.llms.openai import OpenAI
from create_index import rbi_query_engine_service_context
from pandas_query_engine import rbi_notifications_query_engine

#Loading .env file for openAI API key
load_dotenv()
#Defining context for our agent 
context = "Purpose: This primary role of this agent is to provide RBI notifications related information to the user"

#Defining tools avaiable for the agent 
tools = [
    #Note engine to save notes 
    note_engine,
    
    #Query engine for questions related to any information provided in the notifications 
    QueryEngineTool(
        query_engine=rbi_query_engine_service_context,
        metadata=ToolMetadata(
            name="rbi_notification_data",
            description="This has data on different notifications sent by RBI",
        ),
    ),
    
    #Pandas query engine to search the notification dataset 
    QueryEngineTool(
        query_engine=rbi_notifications_query_engine,
        metadata=ToolMetadata(
            name="rbi_all_notification_records",
            description="These are records of various RBI notifications with their titles and text",
        ),
    ),
]

#Defining model to be used by the agent, could also pick open source, local models 
llm = OpenAI(model="gpt-3.5-turbo-0613")
#Using react agent to allow the agent to pick the correct tool/agent for given user query 
agent = ReActAgent.from_tools(tools, llm=llm, verbose=True, context=context)