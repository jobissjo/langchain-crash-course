# Chat Model Documents: https://python.langchain.com/v0.2/docs/integrations/chat/
# OpenAI Chat Model Documents: https://python.langchain.com/v0.2/docs/integrations/chat/openai/

from dotenv import load_dotenv
from langchain_groq import ChatGroq

# Load environment variables from .env
load_dotenv()

# Create a ChatGroq model
model = ChatGroq(model="qwen/qwen3-32b", temperature=0)

# Invoke the model with a message
result = model.invoke("What is 81 divided by 9?")
# print("Full result:")
# print(result)
print("Content only:")
print(result.content)
