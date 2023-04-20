from langchain.chains import ConversationChain
from langchain.llms import OpenAI
from langchain.memory import ConversationBufferMemory
import langchain


langchain.verbose = True

llm = OpenAI(model_name="text-davinci-003", temperature=0)
conversation = ConversationChain(
    llm=llm,
    memory=ConversationBufferMemory()
)

while True:
    user_message = input("You: ")
    ai_message = conversation.predict(input=user_message)
    print(f"AI: {ai_message}")
