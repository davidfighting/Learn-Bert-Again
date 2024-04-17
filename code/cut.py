import pandas as pd

# 加载CSV文件
df = pd.read_csv("data\\all_train.csv", encoding="utf-8")

# 根据标签进行筛选
label_0 = df[df['label'] == 0]
label_1 = df[df['label'] == 1]
label_2 = df[df['label'] == 2]

# 随机抽取所需数量的行，注意这里应该打乱顺序，不然训练的时候bert肯定会偷懒掉
sample_label_0 = label_0.sample(n=1200, random_state=42).sample(frac=1)
sample_label_1 = label_1.sample(n=1200, random_state=42).sample(frac=1)
sample_label_2 = label_2.sample(n=1200, random_state=42).sample(frac=1)

# 合并抽样后的数据
sampled_data = pd.concat([sample_label_0, sample_label_1, sample_label_2])

# 打乱整体顺序
sampled_data = sampled_data.sample(frac=1, random_state=42)

# 将没有被抽样到的数据行保存到新的CSV文件中
remaining_data = df[~df.index.isin(sampled_data.index)]
remaining_data.to_csv("data\\test.csv", index=False, encoding="utf-8")

# 可选择将结果保存到新的CSV文件中
sampled_data.to_csv("data\\train.csv", index=False, encoding="utf-8")
