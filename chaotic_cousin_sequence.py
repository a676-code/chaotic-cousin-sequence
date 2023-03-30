# chaotic_cousin_sequence.py
# Andrew Lounsbury
# 29/3/23
# Purpose: Generate the chaotic cousin sequence; https://www.youtube.com/watch?v=j0o-pMIR8uk

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

def generate_chaotic_cousin(n):
    a = [1, 1, 1]
    i = 3
    while len(a) < n:
        a.append(a[a[i - 1]] + a[i - a[i - 2] - 1])

        i += 1
    return a

print(generate_chaotic_cousin(100))

# Basic Scatter Plots
n = 10
sequence = generate_chaotic_cousin(n)
df = pd.DataFrame(sequence, columns=["Number"])
df['index'] = [i for i in range(n)]
sns.scatterplot(x="index", y="Number", data=df)
plt.savefig("images/10.png")
plt.show()

n = 100
sequence = generate_chaotic_cousin(n)
df = pd.DataFrame(sequence, columns=["Number"])
df['index'] = [i for i in range(n)]
sns.scatterplot(x="index", y="Number", data=df)
plt.savefig("images/100.png")
plt.show()

n = 1000
sequence = generate_chaotic_cousin(n)
df = pd.DataFrame(sequence, columns=["Number"])
df['index'] = [i for i in range(n)]
sns.scatterplot(x="index", y="Number", data=df)
plt.savefig("images/1000.png")
plt.show()

n = 10000
sequence = generate_chaotic_cousin(n)
df = pd.DataFrame(sequence, columns=["Number"])
df['index'] = [i for i in range(n)]
sns.scatterplot(x="index", y="Number", data=df)
plt.savefig("images/10000.png")
plt.show()

n = 100000
sequence = generate_chaotic_cousin(n)
df = pd.DataFrame(sequence, columns=["Number"])
df['index'] = [i for i in range(n)]
sns.scatterplot(x="index", y="Number", data=df)
plt.savefig("images/100000.png")
plt.show()