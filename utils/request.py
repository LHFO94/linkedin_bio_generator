import os
import json
from linkedin_api import Linkedin
from langchain import LLMChain
from langchain.chat_models import ChatOpenAI
from langchain.prompts.chat import (
    HumanMessage,
    ChatPromptTemplate,
    SystemMessagePromptTemplate,
    HumanMessagePromptTemplate,
)


MODEL = "gpt-3.5-turbo-0301"

def scrape_profile(profile_url: str) -> dict:
    """Scrapes a Linkedin profile based on URL"""
    api = Linkedin('luuk_hofman1994@hotmail.com', os.getenv('Linkedpwd'))
    profile_uri = profile_url.split('/')[4]
    profile = api.get_profile(profile_uri)

    header = {'first_name': profile['firstName'], 
              'last_name': profile['lastName'],
              'location': profile['geoLocationName'],
              'current_job': profile['headline']}
                
    experiences, eduction = [], []
    for experience in profile['experience']:
        job_details = {}
        for key in ['companyName', 'title', 'timePeriod', 'description']:
            try:
                job_details[key] = experience[key]
            except KeyError:
                pass
        experiences.append(job_details)

    for study in profile['education']:
        study_details = {}
        for key in ['fieldOfStufy', 'degreeName', 'schoolName']:
            try:
                study_details[key] = study[key]
            except KeyError:
                pass
        eduction.append(study_details)

    profile_out = {}
    profile_out['header'] = header
    profile_out['work_experience'] = experiences
    profile_out['education'] = eduction

    return profile_out        


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
                You will be given information about a particular person and are expected to write a fitting bio for their LinkedIn page. 
                Make sure you do not just cite a persons work experience and education but use this information to write a compelling and personalised biography.
                """

human_prompt = """
               ---------------
               Header info: 
               {header}
               ---------------
               Work experience: 
               {work_experience}
               ---------------
               Education: 
               {education}
               ---------------
               """

def generate_bio(profile: dict, temperature: int=0.7):
    
    chat = ChatOpenAI(openai_api_key=os.getenv('$OPENAI_API_KEY'),
                      model_name=MODEL, temperature=temperature, 
                      verbose=True)

    promt = generate_prompt(system_prompt, human_prompt)
    chain = LLMChain(llm=chat, prompt=promt)

    response = chain.run(
        **{
            "header": str(profile['header']),
            "work_experience": str(profile['work_experience']),
            "education": str(profile['education'])
        }
    )

    response = response.replace('\n', '<br>')
    return response

