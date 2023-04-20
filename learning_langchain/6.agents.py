from langchain.agents import load_tools
from langchain.agents import initialize_agent
from langchain.llms import OpenAI
import langchain


langchain.verbose = True

llm = OpenAI(model_name="text-davinci-003", temperature=0)
tools = load_tools(["terminal"], llm=llm)
agent_executor = initialize_agent(
    tools, llm, agent="zero-shot-react-description")

result = agent_executor.run("現在のディレクトリにあるファイルの一覧を教えてください。")
print(result)
