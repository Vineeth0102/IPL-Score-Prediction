# -*- coding: utf-8 -*-
"""test_pro1.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/14Qct-0DyizLr6tFikEgyDGiFAdHVeWFF
"""

import numpy as np
import pandas as pd

test = pd.read_csv(r"/content/ipl.csv")  #Enter the path of the csv file

print(test['mid'].unique())

remove_list = ['mid','venue','batsman','bowler','striker','non-striker']
print("Before removing unwanted columns {}".format(test.shape))
test.drop(remove_list,axis = 1,inplace = True)
print("After removing unwanted columns {}".format(test.shape))
test

test['bat_team'].unique()
test['bowl_team'].unique()

consistent_teams = ['Royal Challengers Bangalore', 'Kings XI Punjab',
       'Delhi Daredevils', 'Kolkata Knight Riders', 'Rajasthan Royals',
       'Mumbai Indians', 'Chennai Super Kings',
       'Sunrisers Hyderabad']

df = test[(test['bat_team'].isin(consistent_teams)) & (test['bowl_team'].isin(consistent_teams))]
print(df)

df = df[df['overs']>=5]
df

from datetime import datetime
import pandas as pd
x = df['date']
df['date'] = df['date'].apply(lambda x: datetime.strptime(x, '%Y-%m-%d'))
df.info()

import pandas as pd
encoded_df = pd.get_dummies(data = df, columns =['bat_team','bowl_team'])
encoded_df

encoded_df.columns

encoded_df = encoded_df[['date', 'bat_team_Chennai Super Kings', 'bat_team_Delhi Daredevils',
       'bat_team_Kings XI Punjab', 'bat_team_Kolkata Knight Riders',
       'bat_team_Mumbai Indians', 'bat_team_Rajasthan Royals',
       'bat_team_Royal Challengers Bangalore', 'bat_team_Sunrisers Hyderabad',
       'bowl_team_Chennai Super Kings', 'bowl_team_Delhi Daredevils',
       'bowl_team_Kings XI Punjab', 'bowl_team_Kolkata Knight Riders',
       'bowl_team_Mumbai Indians', 'bowl_team_Rajasthan Royals',
       'bowl_team_Royal Challengers Bangalore',
       'bowl_team_Sunrisers Hyderabad','overs', 'runs', 'wickets', 'runs_last_5', 'wickets_last_5',
       'total']]
encoded_df

import pandas as pd
x_train = encoded_df.drop(labels = 'total',axis = 1 )[encoded_df['date'].dt.year <= 2016]
x_test = encoded_df.drop(labels = 'total',axis = 1 )[encoded_df['date'].dt.year >= 2017]

y_train = encoded_df[encoded_df['date'].dt.year <= 2016]['total'].values
y_test = encoded_df[encoded_df['date'].dt.year >= 2017]['total'].values

x_train.drop(labels = 'date',axis = True , inplace = True)
x_test.drop(labels = 'date',axis = True , inplace = True)

print(x_test)
print(x_train)
np.shape(y_train)

!pip  install scikit-learn
from sklearn.linear_model import LinearRegression

linear_regressor = LinearRegression()
linear_regressor.fit(x_train,y_train)

y_pred_lr = linear_regressor.predict(x_test)
y_pred_lr

from sklearn.metrics import mean_absolute_error as mae , mean_squared_error as mse

print("----------Linear Reggression- Model Evaluvation-----------")
print("Mean Absolute Error (MAE) : {}".format(mae(y_test,y_pred_lr)))
print("Mean Squared Error (MSE) : {}".format(mse(y_test,y_pred_lr)))
print("Root MeanSquared Error (RMSE) : {}".format(np.sqrt(mse(y_test,y_pred_lr))))

print(linear_regressor.score(x_test,y_test))
print(linear_regressor.score(x_train,y_train))

from sklearn.tree import DecisionTreeRegressor
Decision_Regressor = DecisionTreeRegressor()
Decision_Regressor.fit(x_train,y_train)

y_pred_dr = Decision_Regressor.predict(x_test)
y_pred_dr

print(Decision_Regressor.score(x_test,y_test))
print(Decision_Regressor.score(x_train,y_train))

print("----------Linear Reggression- Model Evaluvation-----------")
print("Mean Absolute Error (MAE) : {}".format(mae(y_test,y_pred_dr)))
print("Mean Squared Error (MSE) : {}".format(mse(y_test,y_pred_dr)))
print("Root MeanSquared Error (RMSE) : {}".format(np.sqrt(mse(y_test,y_pred_dr))))

from sklearn.ensemble import RandomForestRegressor
Random_Regressor = RandomForestRegressor()
Random_Regressor.fit(x_train,y_train)

y_pred_rr = Decision_Regressor.predict(x_test)
y_pred_rr

print(Random_Regressor.score(x_test,y_test))
print(Random_Regressor.score(x_train,y_train))

print("----------Linear Reggression- Model Evaluvation-----------")
print("Mean Absolute Error (MAE) : {}".format(mae(y_test,y_pred_rr)))
print("Mean Squared Error (MSE) : {}".format(mse(y_test,y_pred_rr)))
print("Root MeanSquared Error (RMSE) : {}".format(np.sqrt(mse(y_test,y_pred_rr))))

from sklearn.ensemble import AdaBoostRegressor

Ada_Regressor =AdaBoostRegressor(base_estimator=linear_regressor, n_estimators=100, learning_rate=25)

Ada_Regressor.fit(x_train,y_train)

y_pred_ad = Ada_Regressor.predict(x_test)
y_pred_ad

print(Ada_Regressor.score(x_test,y_test))
print(Ada_Regressor.score(x_train,y_train))

print("----------Linear Reggression- Model Evaluvation-----------")
print("Mean Absolute Error (MAE) : {}".format(mae(y_test,y_pred_ad)))
print("Mean Squared Error (MSE) : {}".format(mse(y_test,y_pred_ad)))
print("Root MeanSquared Error (RMSE) : {}".format(np.sqrt(mse(y_test,y_pred_ad))))

def predict_score(batting_team = "Chennai Super Kings", bowling_team = "Mumbai Indians",overs =5.1, runs =50  , wickets = 0, runs_last_5 = 0, wickets_last_5 = 0):
  temp_array = list()
  if batting_team == 'Chennai Super Kings':
    temp_array = temp_array + [1,0,0,0,0,0,0,0]
  elif batting_team == 'Delhi Daredevils':
    temp_array = temp_array + [0,1,0,0,0,0,0,0]
  elif batting_team == 'Kings XI Punjab':
    temp_array = temp_array + [0,0,1,0,0,0,0,0]
  elif batting_team == 'Kolkata Knight Riders':
    temp_array = temp_array + [0,0,0,1,0,0,0,0]
  elif batting_team == 'Mumbai Indians':
    temp_array = temp_array + [0,0,0,0,1,0,0,0]
  elif batting_team == 'Rajasthan Royals':
    temp_array = temp_array + [0,0,0,0,0,1,0,0]
  elif batting_team == 'Royal Challengers Bangalore':
    temp_array = temp_array + [0,0,0,0,0,0,1,0]
  elif batting_team == 'Sunrisers Hyderabad':
    temp_array = temp_array + [0,0,0,0,0,0,0,1]

  if bowling_team == 'Chennai Super Kings':
    temp_array = temp_array + [1,0,0,0,0,0,0,0]
  elif bowling_team == 'Delhi Daredevils':
    temp_array = temp_array + [0,1,0,0,0,0,0,0]
  elif bowling_team == 'Kings XI Punjab':
    temp_array = temp_array + [0,0,1,0,0,0,0,0]
  elif bowling_team == 'Kolkata Knight Riders':
    temp_array = temp_array + [0,0,0,1,0,0,0,0]
  elif bowling_team == 'Mumbai Indians':
    temp_array = temp_array + [0,0,0,0,1,0,0,0]
  elif bowling_team == 'Rajasthan Royals':
    temp_array = temp_array + [0,0,0,0,0,1,0,0]
  elif bowling_team == 'Royal Challengers Bangalore':
    temp_array = temp_array + [0,0,0,0,0,0,1,0]
  elif bowling_team == 'Sunrisers Hyderabad':
    temp_array = temp_array + [0,0,0,0,0,0,0,1]

  temp_array = temp_array +[overs, runs , wickets, runs_last_5, wickets_last_5]

  temp_array = np.array([temp_array])
  print(temp_array)

  return int(linear_regressor.predict(temp_array))

final_score = predict_score( batting_team = 'Kolkata Knight Riders', bowling_team = 'Delhi Daredevils',overs = 7, runs = 2, wickets = 2, runs_last_5 = 23, wickets_last_5 = 2 )
print("The final predicted score (range): {}-{}".format(final_score - 10, final_score + 10))

final_score = predict_score( batting_team = 'Mumbai Indians', bowling_team = 'Chennai Super Kings',overs = 17, runs = 28, wickets = 5, runs_last_5 = 23, wickets_last_5 = 0 )
print("The final predicted score (range): {}-{}".format(final_score - 10, final_score + 10))

import pickle
with open('ipl-score-predictor.pkl', 'wb') as file:
    pickle.dump(linear_regressor, file)


