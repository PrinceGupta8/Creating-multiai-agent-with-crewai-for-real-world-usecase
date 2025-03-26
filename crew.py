from crewai import Crew,Process
from agents import blog_researcher,blog_writer
from tasks import research_task,blog_writing_task

#create crew
crew=Crew(
    agents=[blog_researcher,blog_writer],
    tasks=[research_task,blog_writing_task],
    process=Process.sequential,
    memory=True,
    cache=True,
    ma0x_rpm=100,
    share_crew=True,    
)

#start the task execution process with enhanced feedback
result=crew.kickoff(inputs={'topic':'What is Information Technology?'})
print(result)