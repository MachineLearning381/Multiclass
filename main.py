import datums as data
import OneVsOne as multiClassifier
from sklearn.preprocessing import PolynomialFeatures
#import matplotlib.pyplot as plt



dX = data.digits.data;
dY = data.digits.target;


# Transform Feature Space to order 1,5,10, and 20
degree_1 = PolynomialFeatures(degree=1)
#degree_5 = PolynomialFeatures(degree=5)
#degree_10 = PolynomialFeatures(degree=10)
#degree_20 = PolynomialFeatures(degree=20)

X1 = degree_1.fit_transform( dX.copy() )
#X5 = degree_5.fit_transform( dX.copy() )
#X10 = degree_10.fit_transform( dX.copy() )
#X20 = degree_20.fit_transform( dX.copy() )


#print(X1)

g_mistakes = multiClassifier.OvO(X1,dY,.80,300)

print(g_mistakes)

print("terminated")







# CURRENT PROBLEMS IN OneVSOne



#lines 61-68
# how to differentiate the votes



# how to store the votes 

# array[10] 
# ++ index for vote