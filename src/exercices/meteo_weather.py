import pandas as pd

df = pd.read_csv('data/meteo.csv')

df.describe()

df['fecha'] = pd.to_datetime(df['fecha'])

df['tmed'] = df['tmed'].str.replace(",", ".", regex = False)
df['tmed'] = df['tmed'].astype(float)

df['tmin'] = df['tmin'].str.replace(",", ".", regex = False)
df['tmin'] = df['tmin'].astype(float)

df['tmax'] = df['tmax'].str.replace(",", ".", regex = False)
df['tmax'] = df['tmax'].astype(float)


df = df.dropna()

print(df[['fecha', 'tmed', 'tmin', 'tmax']].head())

df['año'] = df['fecha'].dt.year

df_grouped = df.groupby('año')[['tmin', 'tmax']].agg(['min', 'max'])

print(df_grouped)

def plot_temperature(date: pd.Series, temperatures: pd.Series):
    import matplotlib.pyplot as plt
    import numpy as np
    years = date.dt.year
    day = date.dt.dayofyear
    plt.scatter(day, temperatures, c=years, marker=".")
    plt.colorbar(label="Year")
    plt.xlabel("Day of Year")
    plt.ylabel("Temperature (°C)")
    plt.show()

plot_temperature(df['fecha'], df['tmed'])