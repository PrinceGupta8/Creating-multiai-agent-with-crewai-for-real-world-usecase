from crewai import Agent
from Tools import yt_tool
import os
from langchain_openai import ChatOpenAI

os.environ['openai_api_key']=os.getenv('openai_api_key')
llm=ChatOpenAI(model_name='gpt-4o',temperature=0.7)

#create a senior blog content researcher
blog_researcher=Agent(
    role='blog researcher from youtube video',
    goal='get the relevant video content for the topic from youtube channel',
    verbose=True,
    memory=True,
    backstory=(
        'Expert in understanding youtube video on Data science and Artificial Intelligence'
    ),
    llm= llm,
    tools=[yt_tool],
    allow_delegation=True
    )

#create a senior blog content writer
blog_writer=Agent(
    role='blog writer from youtube video',
    goal='Write engaging blog posts based on YouTube video content.',
    verbose=True,
    memory=True,
    backstory=(
        '''with a flair of simplyfying topics, 
           you craft engaging narratives that captivate and educate,
           bringing new discoveries to light in an accessible manner
          '''
    ),
    llm=llm,
    tools=[yt_tool],
    allow_delegation=False
    )