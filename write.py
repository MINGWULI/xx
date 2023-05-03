>> import os
>>> os.chdir('D:/source/dataset')
>>> os.listdir()
['drinksbycountry.csv', 'IMDB-Movie-Data.csv', 'movietweetings', 'test.csv', 'titanic_eda_data.csv', 'titanic_train_data.csv', 'train.csv']
# 读文件
>>> with open('drinksbycountry.csv',mode='r',encoding='utf-8') as f:
      o = f.read()
      print(o)
      
