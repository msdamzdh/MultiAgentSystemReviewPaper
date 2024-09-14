# Resercheragents Crew

Welcome to the Resercheragents Crew project, powered by [crewAI](https://crewai.com). This project is designed to help you set up a multi-agent AI system with ease, for writing review papers based on PDFs located in your system. 

## Installation

Ensure you have Python >=3.10 <=3.13 installed on your system. This project uses [Poetry](https://python-poetry.org/) for dependency management and package handling, offering a seamless setup and execution experience.

First, if you haven't already, install Poetry:

```bash
pip install poetry
```

Next, navigate to your project directory and install the dependencies:

1. First lock the dependencies and then install them:
```bash
poetry lock
```
```bash
poetry install
```
<span style="color:blue">Make sure all needed packages are installed, otherwise check and install them manually. for example for me, pypika did not installed that make me intall it manually.<span> 
### Customizing

## LLM Models
Here for agents, <b>mixtral-8x7b-32768</b> by using an api key from Groq for chat and local embeder model from huggingface for embedding PDFs are used. User must set it's variable envirnment in <b>.env</b> file.

## Running the Project

To kickstart your crew of AI agents and begin task execution, run this from the root folder of your project:

```bash
$ crewai run
```
or
```bash
poetry run resercheragents
```

This command initializes the ResercherAgents Crew, assembling the agents and assigning them tasks as defined in your configuration.

## Understanding Your Crew

The ResercherAgents Crew is composed of multiple AI agents, each with unique roles, goals, and tools. These agents collaborate on a series of tasks, defined in `config/tasks.yaml`, leveraging their collective skills to achieve complex objectives. The `config/agents.yaml` file outlines the capabilities and configurations of each agent in your crew.

## Support

For support, questions, or feedback regarding the Resercheragents Crew or crewAI.
- Visit our [documentation](https://docs.crewai.com)
- Reach out to us through our [GitHub repository](https://github.com/joaomdmoura/crewai)
- [Join our Discord](https://discord.com/invite/X4JWnZnxPb)
- [Chat with our docs](https://chatg.pt/DWjSBZn)

Let's create wonders together with the power and simplicity of crewAI.
