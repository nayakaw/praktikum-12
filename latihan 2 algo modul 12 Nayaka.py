
import pandas as pd

df = pd.read_csv("Negara.csv", index_col=0)
mean = df.groupby(['Benua']).mean()
std = df.groupby(['Benua']).std()

print("\nBerikut Data Framenya \n", df)
print("\nBerikut Data Mean \n", mean)
print("\nBerikut Data Standard Deviation \n", std)

mean.to_csv('NegaraMean.csv')
std.to_csv('NegaraStandarDeviasi.csv')
print("\nFile Berhasil Dibuat")
