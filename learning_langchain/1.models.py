from langchain.llms import OpenAI


llm = OpenAI(model_name="text-davinci-003", temperature=0)
result = llm("GPTとして自己紹介してください。日本語で2文程度でお願いします。")
print(result)
