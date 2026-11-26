import csv

list_score = []
member = 0
total = 0

try:
    with open("scores.csv", "r", encoding="utf-8", newline="") as file:
        reader = csv.DictReader(file)

        for row in reader:
            # print(row["name"], row["score"])
            score = int(row["score"])

            if not 0 <= score <= 100:
                raise ValueError("点数が0~100の範囲外です。")

            member += 1
            total += score
            list_score.append(score)    
    print("====CSV成績分析ツール===\n")
    print("読み込みファイル：scores.csv")

    print(f"読み込み成功：{member}件\n")
    print(f"受験者数：{member}人")
    # print(f"合計点：{total}点")

    if member >= 1:
        average = total / member
        print(f"平均点：{average:.1f}点")
        point_max = max(list_score)
        print(f"最高点：{point_max}点")
        point_min = min(list_score)
        print(f"最低点：{point_min}点")

        print("\n分析が完了しました。")

    else:
        print("\n受験者はいません")

except FileNotFoundError:
    print("CSVファイルが見つかりません。")

except (ValueError, KeyError, TypeError):
    print("CSVデータの形式または点数が不正です。")