import pandas as pd

print(pd.__version__)

# 创建 Series 和 DataFrame 数据结构
data = {
    '姓名': [3, 33, 22],
    '年龄': [5, 55, 55],
    '收入': [1, 2, 3],
    '门牌号': [3, 4, 5]
}
my_df = pd.DataFrame(data)
print(my_df)

# Jupyter 工具
# 在终端输入：pip install jupyter

