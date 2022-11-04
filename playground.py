import openai
import os
from dotenv import load_dotenv
load_dotenv(".env")


openai.api_key = os.environ.get("OPEN_AI_KEY")
prompt = "Can you please add the following numbers together 13 and 25. minus 10 from the result"
operations = ['add', 'addition', 'plus', 'sum', '+', 'subtract', 'subtraction', 'minus', '-', 'multiply', 'product', 'multiplication', '*', 'divide', 'division', '/']
operationsDict = {
    'addition': ['add', 'addition', 'plus', 'sum', '+'],
    'subtraction': ['subtract', 'subtraction', 'minus', '-'],
    'multiplication': ['multiply', 'product', 'multiplication', '*'],
    'division': ['divide', 'division', '/']
}

def gptFunc(prompt=prompt, operations=operations):
    operationsList = []
    response = openai.Completion.create(engine="text-davinci-002", prompt=prompt,
                temperature=0,
                top_p=1,
                max_tokens=20,
                frequency_penalty=0,
                presence_penalty=0
            )

    for ope in operations:
        if ope in prompt:
            for operand in operationsDict:
                for x in range(len(operationsDict[operand])):
                    if ope == operationsDict[operand][x]:
                        operationsList.append(operand)
                        break

    computed = response.choices[0].text.replace("\n", "=").replace(" ", "=").split("=")[-1]
    return (",".join(set(operationsList)), int(float(computed)))

# opeList, result = gptFunc(prompt="24 multiply by 3")