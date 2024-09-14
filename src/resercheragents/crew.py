from logging import config
from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task
from crewai_tools import PDFSearchTool, FileReadTool, DirectoryReadTool
from langchain_groq import ChatGroq
from dotenv import load_dotenv
import os
# Uncomment the following line to use an example of a custom tool
# from resercheragents.tools.custom_tool import MyCustomTool

# Check our tools documentations for more information on how to use them
# from crewai_tools import SerperDevTool
""" Tool instantiate """
load_dotenv()
llm = ChatGroq(api_key=os.getenv('GROQ_API_KEY'),
               model='mixtral-8x7b-32768')
file_read_tool = FileReadTool()
pdf_rag_too = PDFSearchTool(
        config=dict(
            llm=dict(provider="groq", 
                     config=dict(model = "mixtral-8x7b-32768",
                                 api_key= os.getenv('GROQ_API_KEY'),
            					 stream= True
                                 )
                     ),
            embedder=dict(provider="huggingface",
                          config=dict(model = "sentence-transformers/all-mpnet-base-v2"),
                          )
        )
        )
directory_read_tool =  DirectoryReadTool(os.getenv('DIRECTORY_PATH'))
"""LLM Model"""
@CrewBase
class ResercheragentsCrew():
	"""Resercheragents crew"""
	agents_config = 'config/agents.yaml'
	tasks_config = 'config/tasks.yaml'
 
	@agent
	def researcher(self) -> Agent:
		return Agent(
			config=self.agents_config['researcher'],
			tools=[file_read_tool,pdf_rag_too,directory_read_tool], # Example of custom tool, loaded on the beginning of file
			verbose=True,
			llm = llm,
   			allow_delegation = False,
		)

	@agent
	def writer(self) -> Agent:
		return Agent(
			config=self.agents_config['writer'],
			verbose=True,
			llm = llm,
			allow_delegation = False,
		)

	@task
	def research_task(self) -> Task:
		return Task(
			config=self.tasks_config['research_task']
		)

	@task
	def writing_task(self) -> Task:
		return Task(
			config=self.tasks_config['writing_task'],
			output_file='report.doc'
		)

	@crew
	def crew(self) -> Crew:
		"""Creates the Resercheragents crew"""
		return Crew(
			agents=self.agents, # Automatically created by the @agent decorator
			tasks=self.tasks, # Automatically created by the @task decorator
			process=Process.sequential,
			verbose=True,
		)
  #