from langchain.prompts import PromptTemplate


template = """
次のコマンドの概要を説明してください。

コマンド: {command}
"""

prompt = PromptTemplate(
    input_variables=["command"],
    template=template,
)

result = prompt.format(command="echo")
print(result)
