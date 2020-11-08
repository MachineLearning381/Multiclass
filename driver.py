import numpy as np
from sklearn.model_selection import train_test_split
from LinearRegression import linear_regression as lnr
from pocket import pocket as pc

  


def regress_run(X,Y,n,T):


  wx = np.insert(X,0,1,axis=1);

  xtr,xtst,ytr,ytst = train_test_split(wx,Y,test_size=n);


  # Init W Using Linear Regresion
  b = lnr(xtr,ytr);
  
  # Linear Regression Hypothesis 
  wy = np.dot(xtr,b);
 
  # Pocket Algorithm
  g,g_mistakes =  pc(xtr,ytr,b,wy,T);

  return g, g_mistakes, T

