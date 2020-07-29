import pandas as pd

import seaborn as sns
import matplotlib.pyplot as plt

def import_data():

    OD_2014 = pd.read_csv('data/OD_2014.csv')
    OD_2015 = pd.read_csv('data/OD_2015.csv')
    OD_2016 = pd.read_csv('data/OD_2016.csv')
    OD_2017 = pd.read_csv('data/OD_2017.csv')

    df = pd.concat([OD_2014, OD_2015, OD_2016, OD_2017])
    df.reset_index(drop=True, inplace=True)

    return df


def import_station():
    df = pd.read_csv('data/Stations_2017.csv')

    return df


df = import_data()
fig, axs = plt.subplots(nrows=3)
sns.countplot(x="start_station_code",
              data=df,
              order=df.start_station_code.value_counts().iloc[:10].index,
              ax=axs[0])
sns.countplot(x="end_station_code",
              data=df,
              order=df.end_station_code.value_counts().iloc[:10].index,
              ax=axs[1])

sns.countplot(x="start_station_code",
              data=df,
              order=df.start_station_code.value_counts().iloc[:10].index,
              ax=axs[2])




