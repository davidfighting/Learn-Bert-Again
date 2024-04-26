import pandas as pd
from sklearn.metrics import accuracy_score, f1_score

# 读取合并后的 CSV 文件
merged_df = pd.read_csv("O:\成长记\HKU RA\Learn-Bert-Again\data\\test_merged_file.csv", encoding="utf-8")

# 删除包含缺失值的行
merged_df = merged_df.dropna(subset=['label', 'predict_result'])

# 计算准确率
accuracy = accuracy_score(merged_df['label'], merged_df['predict_result'])

# 计算 F1 值
f1 = f1_score(merged_df['label'], merged_df['predict_result'], average='weighted')  #F1 score以weight计算

with open("O:\成长记\HKU RA\Learn-Bert-Again\data\\result.txt", "a") as f:
    f.write("Accuracy Rate: {}\n".format(accuracy))
    f.write("F1 Score: {}\n".format(f1))

print("Accuracy Rate:", accuracy)
print("F1 Score:", f1)
