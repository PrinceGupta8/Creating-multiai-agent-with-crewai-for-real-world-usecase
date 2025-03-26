from crewai import Task
from Tools import yt_tool
from agents import blog_researcher,blog_writer

#Research Task
research_task=Task(
    description=('''Indentify the video {topic}
    Get detailed information about the video from the channel'''),
    expected_output= 'A comprehensive 3 paragraphs long report based on the {topic} of video content',
    tools=[yt_tool],
    agent=blog_researcher
)

#Blog writting Task
blog_writing_task=Task(
    description=('''Get the information from youtube on the {topic}'''),
    expected_output= 'summarize the information from youtube channel video on the topic {topic} and create the content for the blog',
    tools=[yt_tool],
    async_execution=False,
    agent=blog_writer,
    output_file='new-blog-post-md'
)