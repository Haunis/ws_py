"""
sns.distplot()已经deperacated
"""
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

sns.set(palette="muted", color_codes=True)
rs = np.random.RandomState(10)
# data = rs.normal(size=100)
data = np.random.normal(size=100)
f, axes = plt.subplots(2, 2, figsize=(7, 7), sharex=True)
sns.distplot(data, kde=False, color="r", ax=axes[0, 0])
sns.distplot(data, hist=False, rug=True, color="g", ax=axes[0, 1])
sns.distplot(data, hist=False, color="b", kde_kws={"shade": True}, ax=axes[1, 0])
sns.distplot(data, color="k", ax=axes[1, 1])

sns.histplot(data, color='r', ax=axes[0, 0])
sns.kdeplot(data, color="g", ax=axes[0, 1])

plt.show()
