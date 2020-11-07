import numpy as np

# psuedo-inverse = (X^TX)^-1 * X^T
# multiplys psuedo-inverse of X by Y

def linear_regression_ex(x,y):

  b = np.linalg.solve(np.dot(np.transpose(x),x),np.dot(np.transpose(x),y));
  
  return b;