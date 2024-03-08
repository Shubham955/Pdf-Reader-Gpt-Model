import sys
import openai

# get keys from .env file
import os
from dotenv import load_dotenv
load_dotenv()
os.environ['OPENAI_API_KEY']='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'

openai.api_key = os.getenv('OPENAI_API_KEY')

if len(sys.argv) != 2:
    print("Usage: python3 app_cmd.py 'your question'")
    sys.exit(1)

param = sys.argv[1]

from llama_index.core import StorageContext, load_index_from_storage
storage_context = StorageContext.from_defaults(persist_dir='./storage')
index = load_index_from_storage(storage_context)

# query_engine = index.as_query_engine()
# response = query_engine.query(param)

from llama_index.core.memory import ChatMemoryBuffer

memory = ChatMemoryBuffer.from_defaults()
q1=q2=q3=q4=q5=""

q5=q4
q4=q3
q3=q2
q2=q1
q1=param
chat_engine = index.as_chat_engine(
    chat_mode="context",
    memory=memory,
    system_prompt=(
        "you are chatbot, maintain context upto 5 consecutive questions"
        # "context should be according to "+q1+" and "+q2+" and "+q3+" and "+q4+" and "+q5
    ),
)

# response = chat_engine.chat("answer this question "+param+" and context should be according to "+q1+" and "+q2+" and "+q3+" and "+q4+" and "+q5)
response = chat_engine.chat(param)

print(" ")
print(response)
print(" ") 