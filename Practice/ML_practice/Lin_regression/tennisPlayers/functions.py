from sre_compile import isstring
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

def plot_all_features(df,outcome):
    fig, ax = plt.subplots(sharey = True, figsize = (20,30), constrained_layout=True)
    for i in range(1,len(df.columns)-4):
        plt.subplot(len(df.columns)-4,1,i)
        if df.columns[i] not in ['Wins','Winnings','Losses', 'Ranking']:
            column = df.columns[i]
        plt.scatter(df[column],df[outcome],alpha = 0.5)
        plt.xlabel(column)
    fig.suptitle(outcome +' against different features',fontsize=16)
    fig.supylabel(outcome)

def linReg(df,xval,yval):
    # set parameters
    X = df[xval].values
    if isstring(xval):
        X = X.reshape(-1, 1)
    y = df[yval]

    # train and test data
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

    # perform lin. regression
    lr = LinearRegression()
    lr.fit(X_train,y_train)
    print(xval, 'vs.', yval )
    print(f'coefficients: {lr.coef_}')
    print(f'intercept: {lr.intercept_}')
    print(f'score: {lr.score(X_test,y_test)}')
    # compute predicted values
    y_predict = lr.predict(X_test)

    # plot predicted and all data
    
    plt.figure()
    if isstring(xval):
        plt.scatter(df[xval],df[yval],alpha = 0.5)
        plt.plot(X_test,y_predict,color='orange')
        plt.xlabel(xval)
        plt.ylabel(yval)       
    else:
        plt.scatter(y_test,y_predict,alpha = 0.5)
        plt.xlabel(yval)
        plt.ylabel(yval + ' predicted' )
    plt.show() 
