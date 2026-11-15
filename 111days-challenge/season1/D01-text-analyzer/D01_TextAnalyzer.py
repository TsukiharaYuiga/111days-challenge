
def main():
    lines = []
    while(1):
    # 1. 利用者から文章を繰り返し受け取る
        lines = input()
    # 2. 空行が入力されたら繰り返しを終了する
        if lines == '':
            break
    # 3. 文章を改行文字で結合する
        else:
            # x = lines.join()
    # 4. 文字数と行数を計算する
            y = len(lines)
    # 5. 結果を表示する
            print(f'文字数：{y}\n行数：{y}')

if __name__ == "__main__":
    main()
