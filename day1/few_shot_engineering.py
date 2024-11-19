import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))


# 1. 영어를 한국어로 번역하는 5-shot prompt 를 작성하고 "dog"를 번역해보세요.
def few_shot_prompt1():
    completion = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": "You are a translator who translates English to Korean."},
            {
                "role": "user",
                "content": "바나나"
            },
            {
                "role": "assistant",
                "content": "banana"
            },
            {
                "role": "user",
                "content": "파인애플"
            },
            {
                "role": "assistant",
                "content": "pineapple"
            },
            {
                "role": "user",
                "content": "사과"
            }
        ]
    )

    print(completion.choices[0].message.content)


# 2. 영화 리뷰에 대한 sentiment (positive or negative) 를 결정하는 5-shot prompt 를 작성하고 "The storyline was dull and uninspiring." 에 대한 결과를 확인해보세요.
def few_shot_prompt2():
    completion = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": "You are a translator who translates English to Korean."},
            {
                "role": "user",
                "content": "This movie is shit."
            },
            {
                "role": "assistant",
                "content": "negative"
            },
            {
                "role": "user",
                "content": "The performances were outstanding and brought the characters to life."
            },
            {
                "role": "assistant",
                "content": "positive"
            }, {
                "role": "user",
                "content": "The film was overly long and dragged in certain parts."
            },
            {
                "role": "assistant",
                "content": "negative"
            }, {
                "role": "user",
                "content": "The soundtrack was exceptional and perfectly complemented the scenes."
            },
            {
                "role": "assistant",
                "content": "positive"
            }, {
                "role": "user",
                "content": "The movie's camera angle is so simple."
            },
            {
                "role": "assistant",
                "content": "negative"
            },
            {
                "role": "user",
                "content": "The storyline was dull and uninspiring."
            }
        ]
    )

    print(completion.choices[0].message.content)


def few_shot_prompt3():
    completion = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": "You are a DBA"},
            {
                "role": "user",
                "content": """
                    Convert the following natural language requests into SQL queries:
                    1. "급여가 50000 초과인 직원": SELECT * FROM employees WHERE salary > 50000;
                    2. "stock이 0인 products": SELECT * FROM products WHERE stock = 0;
                    3. "수학 점수가 90 초과인 학생들의 이름": SELECT name FROM students WHERE math_score > 90;
                    4. "30일 간의 주문 내역": SELECT * FROM orders WHERE order_date >= DATE_SUB(CURDATE(), INTERVAL 30 DAY);
                    5. "customers 테이블에서 각 도시에 있는 고객의 수": SELECT city, COUNT(*) FROM customers GROUP BY city;

                    Request: "Find the average salary of employees in the marketing department."
                    SQL Query:
                """
            }
        ]
    )

    print(completion.choices[0].message.content)


if __name__ == '__main__':
    few_shot_prompt1()
    few_shot_prompt2()
    few_shot_prompt3()
