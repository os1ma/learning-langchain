from langchain.chains import LLMChain
from langchain.prompts import PromptTemplate
from langchain.llms import OpenAI

# Model を用意
llm = OpenAI(model_name="text-davinci-003", temperature=0)

# Prompt を用意
template = """
次のコマンドの概要を説明してください。

コマンド: {command}
"""
prompt = PromptTemplate(
    input_variables=["command"],
    template=template,
)

# Chain を作成
chain = LLMChain(llm=llm, prompt=prompt)

# 実行
result = chain.run("echo")
print(result)
