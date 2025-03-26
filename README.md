# YouTube-Based Blog Content Generator using CrewAI

This project automates blog content creation by extracting insights from YouTube videos and transforming them into well-structured blog posts. It utilizes **CrewAI**, **LangChain**, and **OpenAI GPT-4o** to conduct video research and generate compelling content.

## Features
- **YouTube Video Research**: Retrieves relevant video content from a specified YouTube channel.
- **AI-Powered Blog Writing**: Uses GPT-4o to generate engaging blog posts.
- **Automated Workflow**: Agents collaborate to perform research and writing tasks efficiently.
- **Seamless Execution**: Supports sequential task execution with memory and caching.

## Tech Stack
- **Python**
- **CrewAI**
- **LangChain**
- **OpenAI GPT-4o**
- **YouTube API**
- **Gradio (Optional UI Component)**

## Installation

### Prerequisites
- Python 3.8+
- OpenAI API Key

### Steps

1. **Clone the repository**
   ```bash
   git clone https://github.com/PrinceGupta8/Creating-multiai-agent-with-crewai-for-real-world-usecase.git
   cd Creating-multiai-agent-with-crewai-for-real-world-usecase
   ```

2. **Create a virtual environment**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Set up environment variables**
   ```bash
   export OPENAI_API_KEY='your_openai_api_key'
   ```

5. **Run the application**
   ```bash
   python main.py
   ```

## Usage

1. **Specify a YouTube channel** in the `@Dreamai8` format.
2. **Enter a topic** for research.
3. **The AI will fetch relevant videos** and extract key points.
4. **A structured blog post will be generated** based on the extracted content.

## Project Structure
```
|-- youtube-blog-generator/
|   |-- agents.py        # Defines AI agents for research and writing
|   |-- tasks.py         # Defines tasks for the AI agents
|   |-- main.py          # Main execution script
|   |-- requirements.txt # Dependencies
|   |-- README.md        # Project documentation
```

## Example

**Input:**
```
Topic: What is Information Technology?
```

**Output:**
```
A well-structured blog post summarizing the latest trends and fundamentals of IT based on YouTube video insights.
```

## Contributing
Pull requests are welcome! Please open an issue to discuss any major changes.

---
🚀 **Transform YouTube videos into high-quality blog content effortlessly!**

