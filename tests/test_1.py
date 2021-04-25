import csv
import opensmile
import pandas as pd

smile = opensmile.Smile(
    #feature_set=opensmile.FeatureSet.ComParE_2016,
    feature_set=opensmile.FeatureSet.IS09_emotion,
    feature_level=opensmile.FeatureLevel.Functionals,
)
#print(smile.feature_names)
y = smile.process_file('/home/liuyuanqing/new_data/emotion/L债务/1926194_232_2.wav')

# print(y.shape)
# y.to_csv('features.csv')

# reader = csv.reader(open('features.csv','r'))
# print(y.iloc[0])


#reader = csv.reader(open('/home/liuyuanqing/learn/emotion/ser/features/3-category/1926194_232_2.csv','r'))
rows = [row for row in reader]
last_line = rows[-1]

print(len(last_line[3:]))

