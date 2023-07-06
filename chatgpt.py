import openai

openai.api_key = "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"


completion = openai.Completion.create(engine="text-davinci-003", prompt="Hazme una solicitud http de tipo get en javascript")

print(completion.choices[0].text)