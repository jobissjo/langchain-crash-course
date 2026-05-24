from dotenv import load_dotenv
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableLambda
from langchain_groq import ChatGroq

# Load environment variables from .env
load_dotenv()

# Create a ChatOpenAI model
model = ChatGroq(model="llama-3.1-8b-instant", temperature=0.7, max_tokens=500)

# Define prompt templates
prompt_template = ChatPromptTemplate.from_messages(
    [
        ("system", "You are a comedian who tells jokes about {topic}."),
        ("human", "Tell me {joke_count} jokes."),
    ]
)

# Define additional processing steps using RunnableLambda
uppercase_output = RunnableLambda(lambda x: x.upper())
count_words = RunnableLambda(lambda x: f"Word count: {len(x.split())}\n{x}")

# Create the combined chain using LangChain Expression Language (LCEL)
chain = prompt_template | model | StrOutputParser() | uppercase_output | count_words

# Run the chain
result = chain.invoke({"topic": "lawyers", "joke_count": 3})

# Output
# print(result)

lowercase_output = RunnableLambda(lambda x: x.lower())

chain2 = prompt_template | model | StrOutputParser() | lowercase_output

result2 = chain2.invoke({"topic": "lawyers", "joke_count": 3})

print(result2)

