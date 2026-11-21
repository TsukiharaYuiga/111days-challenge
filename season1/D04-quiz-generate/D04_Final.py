import json
import random

with open("questions.json", "r", encoding="utf-8") as file:
    questions = json.load(file)

print('===Pythonクイズ===')

question_num = 0
correct_count = 0

while True:
    try:
        Q = int(input("問題数を決めてください："))
        if 1 <= Q <= len(questions):
            break
        print(f"1〜{len(questions)}問で指定してください。")
    except ValueError:
        print("整数を入力してください。")

R = random.sample(range(0, len(questions)), Q)

for i in R:
    question_num += 1
    print(f'第{question_num}問：{questions[i]["question"]}')

    for num, choice in enumerate(questions[i]["choices"], 1):
        print(f'{num}:{choice}')

    while True:
        answer = input("回答：")

        try:
            answer_num = int(answer)
        except ValueError:
            print("1〜4の数字を入力してください。")
            continue

        if not 1 <= answer_num <= len(questions[i]["choices"]):
            print("選択肢の番号で答えてください。")
            continue

        if answer_num - 1 == questions[i]["correct_index"]:
            print("正解！")
            correct_count += 1
        else:
            print("残念！")
            print(f'正解は{questions[i]["correct_index"] + 1}でした。')

        break

print(f'結果：{Q}問中、{correct_count}問正解')
print(f'正答率{correct_count / Q * 100 :.1f}%')
