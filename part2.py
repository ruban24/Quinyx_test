import pandas as pd

df = pd.read_excel("data.xlsx")
x=pd.to_datetime('2022-01-01 10:04:00')
df['time']=pd.to_datetime(df['time'])
df2 = df.resample('15T', on='time').agg({'sales': 'sum','time': 'count'})
df2 = df2.rename(columns = {'time' : 'transactions' })
data = df2.index.map(str)
df2.insert(0,'time',data)
df2['time'] = pd.to_datetime(df2.time)
df2['time']=df2['time'].dt.strftime("%Y-%m-%dT%H:%M:%S.%fZ")
df2.reset_index(drop=True, inplace=True)
print(df2)
df2.to_csv('new.csv',index=False)