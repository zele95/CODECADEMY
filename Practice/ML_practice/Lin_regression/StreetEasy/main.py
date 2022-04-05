# %%
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from sklearn import linear_model
from sklearn.model_selection import train_test_split

manhattan = pd.read_csv("https://raw.githubusercontent.com/sonnynomnom/Codecademy-Machine-Learning-Fundamentals/master/StreetEasy/manhattan.csv")
queens = pd.read_csv("https://raw.githubusercontent.com/sonnynomnom/Codecademy-Machine-Learning-Fundamentals/master/StreetEasy/queens.csv")
brooklyn = pd.read_csv("https://raw.githubusercontent.com/sonnynomnom/Codecademy-Machine-Learning-Fundamentals/master/StreetEasy/brooklyn.csv")

df = pd.DataFrame(queens)
print(df.head())

# %%
x = df[['bedrooms', 'bathrooms', 'size_sqft', 'min_to_subway', 'floor', \
'building_age_yrs', 'no_fee', 'has_roofdeck', 'has_washer_dryer', 'has_doorman',\
     'has_elevator', 'has_dishwasher', 'has_patio', 'has_gym']]
y = df['rent']

x_train, x_test, y_train, y_test = train_test_split(x.values, y.values, train_size = 0.8, test_size = 0.2, random_state=6)

mlr = linear_model.LinearRegression()
mlr.fit(x_train, y_train) 



# %%
sonny_apartment = [[1, 1, 620, 16, 1, 98, 1, 0, 1, 0, 0, 1, 1, 0]]
predict = mlr.predict(sonny_apartment)
 

print("Predicted rent: $%.2f" % predict)

# %%

y_predict=  mlr.predict(x_test)
print(mlr.coef_)

plt.scatter(y_test, y_predict, alpha=0.4)
plt.xlabel("Prices: $Y_i$")
plt.ylabel("Predicted prices: $\hat{Y}_i$")
plt.title("Actual Rent vs Predicted Rent")
plt.show()


# %%
print("Train score:")
print(mlr.score(x_train, y_train))
print("Test score:")
print(mlr.score(x_test, y_test))

residuals = y_predict - y_test
 
plt.scatter(y_predict, residuals, alpha=0.4)
plt.title('Residual Analysis')
 
plt.show()


# %%
zoe_apartment = [[1, 1, 620, 16, 1, 98, 0, 0, 1, 0, 0, 0, 1, 0]]
predict = mlr.predict(zoe_apartment)
print("Predicted rent: $%.2f" % predict)