import datums as data
#import OneVsOne as OvO
import matplotlib.pyplot as plt



dX = data.digits.data;
dY = data.digits.target;


# Transform Feature Space to order 1,5,10, and 20
degree_1 = PolynomialFeatures(degree=1)
degree_5 = PolynomialFeatures(degree=5)
degree_10 = PolynomialFeatures(degree=10)
degree_20 = PolynomialFeatures(degree=20)

X1 = degree_1.fit_transform( dx.copy() )
X5 = degree_5.fit_transform( dx.copy() )
X10 = degree_10.fit_transform( dx.copy() )
X20 = degree_20.fit_transform( dx.copy() )




#print("running")







# CURRENT PROBLEMS IN OneVSOne



# lines 32-37
# need to figure out how to slice the data so we only get the two classes' X and Y vectors

# could just set the other values to zero
# ignore zero vals

#lines 61-68
# how to differentiate the votes



# how to store the votes 

# array[10] 
# ++ index for vote