from langchain.chat_models import ChatOpenAI
from langchain.schema import (
    HumanMessage,
)
 
API_KEY = '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'


MODEL = "gpt-3.5-turbo-0301"

open

from langchain.callbacks.base import CallbackManager
from langchain.callbacks.streaming_stdout import StreamingStdOutCallbackHandler

chat = ChatOpenAI(streaming=True, callback_manager=CallbackManager([StreamingStdOutCallbackHandler()]), verbose=True, temperature=0, openai_api_key=API_KEY)
for resp in chat([HumanMessage(content="Write me a song about sparkling water.")]):
    print(resp)