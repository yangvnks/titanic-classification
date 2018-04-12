import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from pandas import Series, DataFrame

train_path ="../Data/train.csv"

df=pd.read_csv(train_path)
print(df.head())