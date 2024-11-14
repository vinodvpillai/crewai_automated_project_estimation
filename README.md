# Project Analyst, Estimation, and Resource Allocation Agentic Automation

This application is built using the **CrewAI** framework and is designed to automate the process of project analysis, task estimation, and resource allocation. The goal is to support project managers and teams in breaking down complex projects, estimating timelines and resources, and optimizing task assignments for efficient project execution.

## Features
- **Detailed Project Task Breakdown**: Analyzes project requirements to create detailed task lists with dependencies and timelines.
- **Time and Resource Estimation**: Estimates the effort, time, and resources needed for each task, considering historical data and task complexity.
- **Strategic Resource Allocation**: Allocates tasks to team members based on skills, availability, and workload for balanced project execution.

![](https://github.com/vinodvpillai/crewai_automated_project_estimation/blob/master/resources/output.gif)
## Project Structure

The repository consists of the following key files:

```bash
crewai-report-generation-app
├── .gitignore Specifies files and directories to ignore in Git
├── pyproject.toml   Project configuration and dependencies
├── README.md  Project documentation
├── .env Environment variables
└── src/ Source code directory
    └── my_project/  Main application package
        ├── __init__.py Marks the directory as a Python package
        ├── main.py  Main application script
        ├── crew.py  Crew-related functionalities
        ├── tools/   Custom tools directory
        │ ├── custom_tool.py  Custom tool implementation
        │ └── __init__.py  Marks tools directory as a package
        └── config/  Configuration files directory
            ├── agents.yaml   Agent configurations
            └── tasks.yaml Task configurations
```
### 1. `crew.py`
Defines the `CrewaiAutomatedProjectEstimation` class, integrating various CrewAI tools and defining agents and tasks:
- **Agents**:
  - `project_planning_agent`: Plans the project, breaking it down into actionable tasks.
  - `estimation_agent`: Estimates time and resources for tasks.
  - `resource_allocation_agent`: Allocates resources and optimizes team workload.
- **Tasks**:
  - `task_breakdown`: Breaks down project requirements into detailed tasks.
  - `time_resource_estimation`: Provides time and resource estimates for tasks.
  - `resource_allocation`: Assigns tasks to team members and generates an allocation report.

### 2. `main.py`
The entry point to run and test the application locally, with functions to:
- **Run**: Execute the crew's processes with example project inputs.
- **Train**: Train the agents with specified iterations.
- **Replay**: Replay a task from a specific checkpoint.
- **Test**: Test the crew's execution and review results.

### 3. Configuration Files
- **`tasks.yaml`**: Configures tasks, including their descriptions, expected outputs, and agent assignments.
- **`agents.yaml`**: Defines agents, their roles, goals, and backstories.

## Installation

Ensure you have Python >=3.10 <=3.13 installed on your system. This project uses [UV](https://docs.astral.sh/uv/) for dependency management and package handling, offering a seamless setup and execution experience.

First, if you haven't already, install uv:

```bash
pip install uv
```

Next, navigate to your project directory and install the dependencies:

(Optional) Lock the dependencies and install them by using the CLI command:
```bash
crewai install
```

> **Note**: Make sure to include `CrewAI` and any other required libraries in `requirements.txt`.

### Customizing

**Add your `GEMINI_API_KEY` into the `.env` file**

## How to Use

1. **Setup Configuration**:
   - Customize `agents.yaml` to define agent roles, goals, and backgrounds.
   - Update `tasks.yaml` for specifying task descriptions, tools, and expected outputs.

2. **Run the Application**:
   To kickstart your crew of AI agents and begin task execution, run this from the root folder of your project:

   ```bash
   crewai run
   ```

3. **Review the Output**:
   The generated report will be displayed in the console or saved to a specified output file as defined in the `crew.py` logic.
   This example, unmodified, will run the create a `resource_allocation.md` file with the output of a research on LLMs in the root folder.

## Contributing

Contributions are welcome! If you have ideas for improvements or new features, feel free to submit a pull request.

## License

This project is licensed under the MIT License. See `LICENSE` for more details.
