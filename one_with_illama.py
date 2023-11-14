from langchain.llms import CTransformers
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
from get_email import *
from spreadsheet_write import *
arr = getEmails('Bankkkk')

model_path : str = "llama-2-7b.bin"

llm = CTransformers(
            model=model_path, 
            model_type='llama', 
        )

prompt = PromptTemplate(
        input_variables=["product"],
        template="What is the money which was debited or credited from the message {product}? Answer only the number.",
    )

llmchain = LLMChain(llm=llm, prompt=prompt)
# for msg in arr:
#     print(llmchain.run(msg))
print(llmchain.run(arr))

