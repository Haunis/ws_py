"""

"""
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

sns.set(palette="muted", color_codes=True)
rs = np.random.RandomState(10)
d = rs.normal(size=100)
f, axes = plt.subplots(2, 2, figsize=(7, 7), sharex=True)
sns.distplot(d, kde=False, color="r", ax=axes[0, 0])
sns.distplot(d, hist=False, rug=True, color="g", ax=axes[0, 1])
sns.distplot(d, hist=False, color="b", kde_kws={"shade": True}, ax=axes[1, 0])
sns.distplot(d, color="k", ax=axes[1, 1])
plt.show()
