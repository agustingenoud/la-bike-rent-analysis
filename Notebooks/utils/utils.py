import sys
import pandas as pd

def obj_size_fmt(num):
    if num<10**3:
        return "{:.2f}{}".format(num,"B")
    elif ((num>=10**3)&(num<10**6)):
        return "{:.2f}{}".format(num/(1.024*10**3),"KB")
    elif ((num>=10**6)&(num<10**9)):
        return "{:.2f}{}".format(num/(1.024*10**6),"MB")
    else:
        return "{:.2f}{}".format(num/(1.024*10**9),"GB")


def memory_usage():
    memory_usage_by_variable=pd.DataFrame({k:sys.getsizeof(v)\
        for (k,v) in globals().items()},index=['Size'])
    memory_usage_by_variable=memory_usage_by_variable.T
    memory_usage_by_variable=memory_usage_by_variable\
        .sort_values(by='Size',ascending=False).head(10)
    memory_usage_by_variable['Size']=memory_usage_by_variable['Size']\
        .apply(lambda x: obj_size_fmt(x))
    
    return memory_usage_by_variable

def find_null(df):
    #Find null values
    na_sum=df.isna().sum()
    na_percent=(((df.isna().sum()) / (len(df))) *100).round(2)
    null_sum=df.isnull().sum()
    null_percent=(((df.isnull().sum()) / (len(df))) *100).round(2)
    null_sum.name='NULL_sum'
    null_percent.name='NULL_%(0./100.)'
    na_sum.name='NAL_sum'
    na_percent.name='NA_%(0./100.)'

    return pd.concat([null_sum,null_percent, na_sum, na_percent], axis=1)