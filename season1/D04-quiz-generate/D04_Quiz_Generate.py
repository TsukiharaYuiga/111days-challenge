import json
import random

with open("questions.json", "r", encoding="utf-8") as file:
    questions = json.load(file)

print('===Pythonクイズ===')

quetion_num = 0
correct_count = 0

try:
    Q = int(input('問題数を決めてください'))
except:
    print('数字を入力してください。')

if 0 <= Q <= len(questions):
    R = random.sample(range(0, len(questions)), Q)

    for i in R:
        quetion_num += 1
        print(f'第{quetion_num}問：{questions[i]["question"]}')

        for num, choice in enumerate(questions[i]["choices"], 1):
            print(f'{num}:{choice}')


        while True:
            answer = input()
            if 1 <= int(answer) <= len(questions[i]["choices"]):
                print('回答：'+ answer)
                if (int(answer) -1) == questions[i]["correct_index"]:
                    print('正解！')
                    correct_count += 1
                    break
                else:
                    print('残念！')
                    print(f'正解は{questions[i]["correct_index"] + 1}でした。')
                break
            else:
                print('選択肢で答えてください。')

    print(f'結果：{Q}問中、{correct_count}問正解')
    print(f'正答率{correct_count / Q * 100 :.1f}%')

else:
    print(f'問題数は最大で{len(questions)}です')
