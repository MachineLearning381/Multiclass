import numpy as np
from sklearn.model_selection import train_test_split
from LinearRegression import linear_regression_ex as lnr
from pocket import pocket as pc

  

def test_run(b,X,Y,T):

  # Perceptron Hypothesis
  wy = np.dot(X,b);
 
  # Pocket Algorithm
  g,g_mistakes =  pc(X,Y,b,wy,T);

  return T, g_mistakes

  

def regress_run(X,Y,T):

  # Init W Using Linear Regresion
  b = lnr(X,Y);
  
  # Linear Regression Hypothesis 
  wy = np.dot(X,b);
 
  # Pocket Algorithm
  g,g_mistakes =  pc(X,Y,b,wy,T);

  return T,g_mistakes


def full_run(X,Y,n,T):
  
  wx = np.insert(X,0,1,axis=1);
  xtr,xtst,ytr,ytst = train_test_split(wx,Y,test_size=n);
  T1,G1_mistakes = test_run(wx[0],xtr,ytr,T);
  T2,G2_mistakes = regress_run(xtr,ytr,T);

  return T1,G1_mistakes,T2,G2_mistakes