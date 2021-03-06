"""
Series.map(method):可实现将数据映射成想要的数据
"""
import pandas as pd

# x是一列的每个值，这里是'成绩'是int值
def grade(x):
    if x >= 90:
        return '优'
    elif 70 <= x < 90:
        return '良'
    elif 60 <= x < 70:
        return '中'
    else:
        return '差'


def main():
    data = {'姓名': ['李红', '小明', '马芳', '国志'],
            '性别': ['0', '1', '0', '1'],
            '籍贯': ['北京', '兰州', '兰州', '上海'],
            '成绩': [58, 86, 91, 78]}
    df = pd.DataFrame(data)
    print(df, end="\n\n")
    df['等级'] = df['成绩'].map(grade) #将'成绩'列每个值应用grade函数
    print(df)


if __name__ == "__main__":
    main()
