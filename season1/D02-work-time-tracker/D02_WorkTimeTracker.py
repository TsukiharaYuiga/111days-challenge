def main():
    records = []
    print('作業名と作業時間を入力してください。終了と入力すると記録します')
    total_time = 0

    while True:
        # 1. 作業名を入力する
        task_name = input('作業名：')
        # 2. 「終了」が入力されたらループを抜ける
        if task_name == '終了':
            break
        # 3. 作業時間を入力する
        task_min = int(input('作業時間（分）：'))
        total_time += task_min
        # 4. 作業名と作業時間を辞書にまとめる
        record = {task_name,task_min}
        # 5. 辞書をrecordsに追加する
        records.append(record)
    # 6. 保存した作業を一覧表示する
    print("---本日の作業記録---")
    print(records)
    # 7. 合計作業時間を計算して表示する
    print(f'合計：{total_time}')

if __name__ == "__main__":
    main()
