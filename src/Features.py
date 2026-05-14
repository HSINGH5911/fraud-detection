from sklearn.preprocessing import StandardScaler

def scale_amount(df):
    scaler = StandardScaler()
    df["Amount"] = scaler.fit_transform(df["Amount"])
    return df

def drop_time(df):
    df = df.drop("time", axis=1)
    return df