from twilio.rest import Client
account_sid = 'AC243413a7b35a7602db007e4469f5f1ab'
auth_token = '10083eb942e2ac7d687a467e68ea87aa'
client = Client(account_sid, auth_token)
import os
import openai
openai.organization = "org-8fdsinS9S3Og37JhjC7djL71"
openai.api_key = "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"
openai.Model.list()
# message = client.messages.create(
#   from_='+13157906318',
#   body='ihifdgvbdklzf',
#   to='+919910977193'
# )

# print(message.sid)
def get_completion(prompt, model="ada"):

    messages = [{"role": "user", "content": prompt}]

    response = openai.ChatCompletion.create(

    model=model,

    messages=messages,

    temperature=0,

    )
    return response.choices[0].message["content"]
prompt = "Test chat"

response = get_completion(prompt)

print(response)
for sms in client.messages.list():
  print(sms.to)
  print(sms.body)