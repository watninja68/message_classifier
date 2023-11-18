from langchain.llms import CTransformers
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
from get_email import *
from spreadsheet_write import *
arr = getEmails('Aa')
print(arr)
model_path : str = "llama-2-7b.bin"

llm = CTransformers(
            model=model_path, 
            model_type='llama', 
        )

prompt = PromptTemplate(
        input_variables=["product"],
        template="What is the money which was debited or credited from the message {product}? Give the answer in the given format The amount no other text.",
    )
prompt2 = PromptTemplate(
        input_variables=["product"],
        template="Was it debited or credited from the message {product}? Give the answer in the given format credited/debited no other text.",
    )
llmchain = LLMChain(llm=llm, prompt=prompt)
llmchain2 = LLMChain(llm=llm, prompt=prompt2)

# for msg in arr:
#     print(llmchain.run(msg))
bb = llmchain2.run(arr)
print(bb)
aa = llmchain.run(arr)
val = ''.join(filter(str.isdigit, aa))
val = int(val)
print(val/100)
spreadsheets(val,'debited')
