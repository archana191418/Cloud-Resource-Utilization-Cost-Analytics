import pandas as pd
df=pd.read_csv("data/raw/Cloud_Dataset.csv")
#1.inspect the data 

print(df.head())
print(df.info())
print(df.describe())
print(df.shape)

#2.remove duplicate

df=df.drop_duplicates()

#3.handlig missing values
print(df.isnull().sum())

##remove rows with missing values
df=df.dropna()

#4. convert data types

df["timestamp"]=pd.to_datetime(df["timestamp"])
df["cpu_usage"]=pd.to_numeric(df["cpu_usage"])
df["memory_usage"]=pd.to_numeric(df["memory_usage"])
df["net_io"]=pd.to_numeric(df["net_io"])
df["disk_io"]=pd.to_numeric(df["disk_io"])
df["vCPU"]=pd.to_numeric(df["vCPU"])
df["RAM_GB"]=pd.to_numeric(df["RAM_GB"])
df["price_per_hour"]=pd.to_numeric(df["price_per_hour"])
df["latency_ms"]=pd.to_numeric(df["latency_ms"])
df["throughput"]=pd.to_numeric(df["throughput"])
df["cost"]=pd.to_numeric(df["cost"])
df["utilization"]=pd.to_numeric(df["utilization"])


#5.standarize text column 
df["cloud_provider"]=df["cloud_provider"].str.strip().str.upper()
df["region"]=df["region"].str.strip()
df["vm_type"]=df["vm_type"].str.strip()

# 6.remove invalid values
#cpu and memory usage should be in between 0-100
df=df[(df["cpu_usage"]>=0)& (df["cpu_usage"]<=100)]
df=df[(df["memory_usage"]>=0)& (df["memory_usage"]<=100)]

#utilization between 0 and 100
df=df[(df["utilization"]>=0)& (df["utilization"]<=100)]

#remove negative values
df=df[df["net_io"]>=0]
df=df[df["price_per_hour"]>=0]
df=df[df["disk_io"]>=0]
df=df[df["throughput"]>=0]
df=df[df["latency_ms"]>=0]
df=df[df["vCPU"]>=0]
df=df[df["RAM_GB"]>=0]


# 7.feature engineering
df["cost_per_vCPU"]=df["cost"] / df["vCPU"]
df["cost_per_RAM"]=df["cost"] / df["RAM_GB"]
df["High_cpu"]=df["cpu_usage"]>80
df["high_memory"]=df["memory_usage"]>80
df["underutilized"]=df["utilization"]<30

##### 8.save cleaned data
df.to_csv("data/processed/cloud_dataset__cleaned.csv",index=False)

print("data cleaned successfully")
print(df.head())
