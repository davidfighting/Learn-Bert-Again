import pandas as pd

# 读取第一个 CSV 文件
df1 = pd.read_csv("O:\成长记\HKU RA\Learn-Bert-Again\data\\test_result.csv", encoding="utf-8")

# 读取第二个 CSV 文件
df2 = pd.read_csv("O:\成长记\HKU RA\Learn-Bert-Again\data\\test_checkresult.csv", encoding="utf-8")

# 根据 id 列进行匹配，并将两个 DataFrame 合并起来
merged_df = pd.merge(df1, df2, on='id', how='inner')

# 显示合并后的 DataFrame
print(merged_df)

# 将合并后的 DataFrame 写入到新的 CSV 文件中
merged_df.to_csv("O:\成长记\HKU RA\Learn-Bert-Again\data\\test_merged_file.csv", index=False, encoding="utf-8")
