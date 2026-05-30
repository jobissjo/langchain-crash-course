# from dotenv import load_dotenv
# from langchain_classic import hub
# from langchain_classic.agents import AgentExecutor
# from langchain_core import load
# from langchain.agents import (
    
#     create_agent,
# )

# from langchain_core.tools import Tool
# # from langchain_openai import ChatOpenAI
# from langchain_groq import ChatGroq
# # Load environment variables from .env file
# load_dotenv()
# from langgraph.prebuilt import create_react_agent

# from langgraph.prebuilt import create_react_agent
# # Define a very simple tool function that returns the current time
# def get_current_time(*args, **kwargs):
#     """Returns the current time in H:MM AM/PM format."""
#     import datetime  # Import datetime module to get current time

#     now = datetime.datetime.now()  # Get current time
#     return now.strftime("%I:%M %p")  # Format time in H:MM AM/PM format


# # List of tools available to the agent
# tools = [
#     Tool(
#         name="Time",  # Name of the tool
#         func=get_current_time,  # Function that the tool will execute
#         # Description of the tool
#         description="Useful for when you need to know the current time",
#     ),
# ]

# # Pull the prompt template from the hub
# # ReAct = Reason and Action
# # https://smith.langchain.com/hub/hwchase17/react
# prompt = load.load("hwchase17/react")

# # Initialize a ChatOpenAI model
# # llm = ChatOpenAI(
# #     model="gpt-4o", temperature=0
# # )
# llm = ChatGroq(model="llama-3.1-8b-instant", temperature=0)

# # Create the ReAct agent using the create_react_agent function
# # agent = create_agent(
# #     model=llm,
# #     tools=tools,
# #     system_prompt=prompt
# # )
# agent_executor = create_react_agent(model=llm, tools=tools)

# # Create an agent executor from the agent and tools
# # agent_executor = AgentExecutor.from_agent_and_tools(
# #     agent=agent,
# #     tools=tools,
# #     verbose=True,
# # )

# # Run the agent with a test query
# response = agent_executor.invoke({"input": "What time is it?"})

# # Print the response from the agent
# print("response:", response)


import datetime
from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langchain_core.tools import Tool
from langgraph.prebuilt import create_react_agent

# 1. Load environment variables from your .env file
load_dotenv()

# 2. Define your tool function
def get_current_time(*args, **kwargs):
    """Returns the current time in H:MM AM/PM format."""
    now = datetime.datetime.now()
    return now.strftime("%I:%M %p")

# 3. Explicitly package it into a LangChain Tool
tools = [
    Tool(
        name="Time",
        func=get_current_time,
        description="Useful for when you need to know the current time. Input should be an empty string.",
    ),
]

# 4. Initialize the Groq model
llm = ChatGroq(model="llama-3.1-8b-instant", temperature=0)

# 5. Compile the agent graph 
# This automatically constructs the optimal ReAct system prompt using ONLY your tools.
agent_executor = create_react_agent(model=llm, tools=tools)

# 6. Invoke the agent using the correct State schema ('messages')
response = agent_executor.invoke({
    "messages": [("user", "What time is it?")]
})

# 7. Extract and print the final model response cleanly
final_message = response["messages"][-1].content
print("\n--- Agent Response ---")
print(final_message)

for res in response["messages"]:
    print("\n--- Intermediate Step ---")
    print(res.content)