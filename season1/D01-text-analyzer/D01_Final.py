
def main():
    lines = []
    print("文章を入力してください（空行で終了）")
    while True:
    # 1. 利用者から文章を繰り返し受け取る
        text = input()
    # 2. 空行が入力されたら繰り返しを終了する
        if text == '':
            break
    # 3. 文章を改行文字で結合する
        lines.append(text)
    full_text = "\n".join(lines)
    # 4. 文字数と行数を計算する
    count_ch = len(full_text)
    count_line = len(lines)
    # 5. 結果を表示する
    print(f"文字数：{count_ch}\n行数：{count_line}")

if __name__ == "__main__":
    main()
