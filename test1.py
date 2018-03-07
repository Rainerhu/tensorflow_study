# -*- coding: utf-8 -*-
import math
from IPython import display
from matplotlib import cm
from matplotlib import gridspec
from matplotlib import pyplot as plt
import numpy as np
import pandas as pd
from sklearn import metrics
import tensorflow as tf
from tensorflow.python.data import Dataset

tf.logging.set_verbosity(tf.logging.ERROR)
pd.options.display.max_rows=10
pd.options.display.float_format='{:.1f}'.format
Location=r'D:\study\python\tensorflow\california_housing_train.csv'
california_housing_dataframe = pd.read_csv(Location, sep=",")
california_housing_dataframe=california_housing_dataframe.reindex(np.random.permutation(california_housing_dataframe.index))
california_housing_dataframe["median_house_value"]/=1000.0
#print(california_housing_dataframe)
#print(california_housing_dataframe.describe())
