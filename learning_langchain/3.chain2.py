from langchain.chains import SimpleSequentialChain
from langchain.chains import LLMChain
from langchain.prompts import PromptTemplate
from langchain.llms import OpenAI

# Model を用意
llm = OpenAI(model_name="text-davinci-003", temperature=0)

# 1 つ目の Prompt と Chain を用意
template = """
次のコマンドの概要を説明してください。

コマンド: {command}
"""
prompt = PromptTemplate(
    input_variables=["command"],
    template=template,
)
chain = LLMChain(llm=llm, prompt=prompt)

# 2 つ目の Prompt と Chain を用意
template2 = """
入力を要約してください。

入力: {input}
"""
prompt2 = PromptTemplate(
    input_variables=["input"],
    template=template2,
)
chain2 = LLMChain(llm=llm, prompt=prompt2)

# 2 つの Chain を直列に繋ぐ
# verbose=True として、各 Chain の実行結果を表示する
overall_chain = SimpleSequentialChain(chains=[chain, chain2], verbose=True)

# 実行
result = overall_chain.run("echo")
print(result)
