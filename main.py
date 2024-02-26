from dotenv import load_dotenv
from save_notes import note_engine
from llama_index.core.tools import QueryEngineTool, ToolMetadata
from llama_index.core.agent import ReActAgent
from llama_index.llms.openai import OpenAI
from create_index import rbi_query_engine_service_context

load_dotenv()
context = "Purpose: This primary role of this agent is to provide RBI notifications relation information to the user"

tools = [
    note_engine,
    QueryEngineTool(
        query_engine=rbi_query_engine_service_context,
        metadata=ToolMetadata(
            name="rbi_notification_data",
            description="This has data on different notifications sent by RBI",
        ),
    ),
]

llm = OpenAI(model="gpt-3.5-turbo-0613")
agent = ReActAgent.from_tools(tools, llm=llm, verbose=True, context=context)
