import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))


def simple1():
    completion = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {
                "role": "user",
                "content": """
                    Solve the following problem step-by-step: 23 + 47
    
                    Step-by-step solution:
                    1. Write your Prompt
                    2. Write your Prompt
                    3. Write your Prompt
                    4. Write your Prompt
                    
                    Answer: 70
                """
            }
        ]
    )

    print(completion.choices[0].message.content)


def simple2():
    completion = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {
                "role": "user",
                "content": """
                    Solve the following problem step-by-step: 123 - 58
                    
                    Step-by-step solution:
                    1. Write your Prompt
                    2. Write your Prompt
                    3. Write your Prompt
                    4. Write your Prompt
                    
                    Answer: 65
                """
            }
        ]
    )

    print(completion.choices[0].message.content)


def simple3():
    completion = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {
                "role": "user",
                "content": """
                    Solve the following problem step-by-step: 345 + 678 - 123
                    
                    Step-by-step solution:
                    1. Check the response
                    2. Check the response
                    3. Check the response
                    
                    Answer: 900
                """
            }
        ]
    )

    print(completion.choices[0].message.content)


def intermediate1():
    completion = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {
                "role": "user",
                "content": """
                    Solve the following logic puzzle step-by-step:
                    Three friends, Alice, Bob, and Carol, have different favorite colors: red, blue, and green. We know that:
                    1. Alice does not like red.
                    2. Bob does not like blue.
                    3. Carol likes green.
                    
                    Determine the favorite color of each friend.
                    
                    Step-by-step solution:
                    Write your Prompt
                    
                    Answer:
                    - Alice: blue
                    - Bob: red
                    - Carol: green
                """
            }
        ]
    )

    print(completion.choices[0].message.content)


def intermediate2():
    completion = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {
                "role": "user",
                "content": """
                    Solve the following logic puzzle step-by-step:
                    Four people (A, B, C, D) are sitting in a row. We know that:
                    1. A is not next to B.
                    2. B is next to C.
                    3. C is not next to D.
                    
                    Determine the possible seating arrangements.
                    
                    Step-by-step solution:
                    Write your Prompt
                    
                    Answer:
                    - Possible arrangements: BCAD, CABD
                """
            }
        ]
    )

    print(completion.choices[0].message.content)


if __name__ == '__main__':
    simple1()
    simple2()
    simple3()
    intermediate1()
    intermediate2()
