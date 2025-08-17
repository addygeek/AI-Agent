from langchain.llms import OpenAI
from langchain.agents import initialize_agent, AgentType
from langchain.tools import Tool

# Define a simple tool
def add_numbers(a: int, b: int) -> int:
    return a + b

add_tool = Tool(
    name="AddNumbers",
    func=lambda x: str(add_numbers(*map(int, x.split()))),
    description="Adds two numbers. Input format: 'num1 num2'"
)

# Initialize the agent
llm = OpenAI(temperature=0)
agent = initialize_agent(
    tools=[add_tool],
    llm=llm,
    agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
    verbose=True
)

# Example usage
if __name__ == "__main__":
    result = agent.run("Add 5 and 7")
    print(result)