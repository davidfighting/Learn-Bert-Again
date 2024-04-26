import pandas as pd

# 读取 CSV 文件
df = pd.read_csv("O:\成长记\HKU RA\Learn-Bert-Again\data\sub.csv", encoding="utf-8")

# 比较三列的最大值，并将最大值对应的列索引添加到新列 predict_result 中
df['predict_result'] = df[['label_0', 'label_1', 'label_2']].idxmax(axis=1).str[-1]

# 将 DataFrame 写入到新的 CSV 文件中
df.to_csv("O:\成长记\HKU RA\Learn-Bert-Again\data\\test_result.csv", index=False, encoding="utf-8")
