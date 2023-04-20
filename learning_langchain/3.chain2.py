from langchain.chains import SimpleSequentialChain
from langchain.chains import LLMChain
from langchain.prompts import PromptTemplate
from langchain.llms import OpenAI
import langchain


langchain.verbose = True

# Model を用意
llm = OpenAI(model_name="text-davinci-003", temperature=0)

# 1 つ目の Prompt と Chain を用意
cot_template = """
以下の質問に回答してください。

### 質問 ###
{question}
### 質問終了 ###

ステップバイステップで考えましょう。
"""
cot_prompt = PromptTemplate(
    input_variables=["question"],
    template=cot_template,
)
cot_chain = LLMChain(llm=llm, prompt=cot_prompt)

# 2 つ目の Prompt と Chain を用意
summarize_template = """
入力を結論だけ一言に要約してください。

### 入力 ###
{input}
### 入力終了 ###
"""
summarize_prompt = PromptTemplate(
    input_variables=["input"],
    template=summarize_template,
)
summarize_chain = LLMChain(llm=llm, prompt=summarize_prompt)

# 2 つの Chain を直列に繋ぐ
cot_summarize_chain = SimpleSequentialChain(
    chains=[cot_chain, summarize_chain])

# 実行
result = cot_summarize_chain(
    "私は市場に行って10個のリンゴを買いました。隣人に2つ、修理工に2つ渡しました。それから5つのリンゴを買って1つ食べました。残りは何個ですか？")
print(result['output'])
