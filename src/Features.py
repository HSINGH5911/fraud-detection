from sklearn.preprocessing import StandardScaler

def scale_amount(df):
    scaler = StandardScaler()
    df["Amount"] = scaler.fit_transform(df[["Amount"]])
    return df

def drop_time(df):
    df = df.drop("Time", axis=1)
    return df

def engineer_features(df):
    df = scale_amount(df)
    df = drop_time(df)

    return df
