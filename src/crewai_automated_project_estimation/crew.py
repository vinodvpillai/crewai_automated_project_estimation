from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task
from crewai import LLM # type: ignore
import os
from os.path import join, dirname
from dotenv import load_dotenv
from .outputs.output_model import ProjectPlan

# Load environment variables
dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)

@CrewBase
class CrewaiAutomatedProjectEstimation():
	"""CrewaiAutomatedProjectEstimation crew"""

	agents_config = 'config/agents.yaml'
	tasks_config = 'config/tasks.yaml'
 
	# LLM
	llm = LLM(model=os.getenv('GEMINI_MODEL'),api_key=os.getenv('GEMINI_API_KEY'))

	@agent
	def project_planning_agent(self) -> Agent:
		return Agent(
			llm=self.llm,
			config=self.agents_config['project_planning_agent'], # type: ignore
			# tools=[MyCustomTool()], # Example of custom tool, loaded on the beginning of file
			verbose=True
		)
  
	@agent
	def estimation_agent(self) -> Agent:
		return Agent(
			llm=self.llm,
			config=self.agents_config['estimation_agent'], # type: ignore
			# tools=[MyCustomTool()], # Example of custom tool, loaded on the beginning of file
			verbose=True
		)

	@agent
	def resource_allocation_agent(self) -> Agent:
		return Agent(
			llm=self.llm,
			config=self.agents_config['resource_allocation_agent'], # type: ignore
			verbose=True
		)

	@task
	def task_breakdown(self) -> Task:
		return Task(
			config=self.tasks_config['task_breakdown'], # type: ignore
		)

	@task
	def time_resource_estimation(self) -> Task:
		return Task(
			config=self.tasks_config['time_resource_estimation'], # type: ignore
		)
  
	@task
	def resource_allocation(self) -> Task:
		return Task(
			config=self.tasks_config['resource_allocation'], # type: ignore
			output_pydantic=ProjectPlan,
			output_file='resource_allocation.md'
		)

	@crew
	def crew(self) -> Crew:
		"""Creates the CrewaiAutomatedProjectEstimation crew"""
		return Crew(
			agents=self.agents, # Automatically created by the @agent decorator # type: ignore
			tasks=self.tasks, # Automatically created by the @task decorator # type: ignore
			process=Process.sequential,
			verbose=True,
			# process=Process.hierarchical, # In case you wanna use that instead https://docs.crewai.com/how-to/Hierarchical/
		)
