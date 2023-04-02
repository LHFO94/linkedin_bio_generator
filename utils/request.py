import os
from langchain import LLMChain
from langchain.chat_models import ChatOpenAI
from langchain.prompts.chat import (
    HumanMessage,
    ChatPromptTemplate,
    SystemMessagePromptTemplate,
    HumanMessagePromptTemplate,
)
from langchain.callbacks.base import CallbackManager
from langchain.callbacks.streaming_stdout import StreamingStdOutCallbackHandler


MODEL = "gpt-3.5-turbo-0301"


def generate_prompt(prompt_template: str, human_template: str) -> ChatPromptTemplate:
    """Generates a prompt template to which document texts can be inserted later"""
    system_message_prompt = SystemMessagePromptTemplate.from_template(prompt_template)
    human_message_prompt = HumanMessagePromptTemplate.from_template(human_template)
    chat_prompt = ChatPromptTemplate.from_messages(
        [system_message_prompt, human_message_prompt]
    )
    return chat_prompt



system_prompt = """
                You are a skilled writer well versed in all languages and specially good at corporate lingo.
                You will be given information about a particular person and are expected to write a fitting bio for their LinkedIn page
                """

human_prompt = """
               You are a skilled writer well versed in all languages and specially good at corporate lingo.
               You will be given information about a particular person and are expected to write a fitting bio for their LinkedIn page
               The person has the following name: {first_name}, {last_name} and lives in {location}. This person has {years_of_experience} years of experience in the field of {industry}.    
               This person has a {degree_type} in {field_of_study}         
               """

def generate_bio(first_name: str, last_name: str, location: str, 
                 years_of_experience: str, industry: str, 
                 degree_type: str, field_of_study: 
                 str, temperature: int=0):
    
    
    chat = ChatOpenAI(openai_api_key=os.getenv('$OPENAI_API_KEY'),
                      model_name=MODEL, temperature=temperature, 
                      verbose=True)

    promt = generate_prompt(system_prompt, human_prompt)
    chain = LLMChain(llm=chat, prompt=promt)
    response = chain.run(
        **{
            "first_name": first_name,
            "last_name": last_name,
            "location": location,
            "years_of_experience": years_of_experience,
            "industry": industry,
            "degree_type": degree_type,
            "field_of_study": field_of_study,
        }
    )

    return response.replace('\n', '<br>')

if __name__ == "__main__":
    generate_bio('papi','chulo','Amsterdam','2', 'IT', 'Masters', 'Data Science')