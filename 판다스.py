import pandas as pd

exam_data = {'수학': [90,80,70], '영어':[98,89,95], '음악':[85,95,100], '체육':[100,90,90]}
df = pd.DataFrame(exam_data, index=['서준', '우현', '인아'])
print(df)
print('\n')
df2=df[:]
df2.drop('우현', inplace=True)
print(df2)
print('\n')
df3=df[:]
df3.drop(['우현', '인아'],axis=0, inplace=True)
print(df3)
df4=df[:]
df4.drop('수학', axis=1, inplace=True)
print(df4)
print('\n')
df5=df[:]
df5.drop(['영어', '음악'], axis=1, inplace=True)
print(df5)
print('\n')