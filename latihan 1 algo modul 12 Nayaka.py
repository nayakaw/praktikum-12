import pandas as pd

data = pd.read_csv("Negara.csv")

df = pd.DataFrame(data)
mean = df.groupby(['Benua']).mean()
std = df.groupby(['Benua']).std()

print("\nBerikut Data Framenya: \n", df)
print("\nBerikut Data Mean: \n", mean)
print("\nBerikut Data Standard Deviation: \n", std)