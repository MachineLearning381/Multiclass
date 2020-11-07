
import numpy as np
import random

# x = test feature vectors
# y = test data classifications
# w = weight vector 
# w_y = data classifications predicted from W*X
# N = size of the y vectors
# T = number of iterations

def pocket(x , y, w, w_y, T ):

  N = w_y.size

  # List of random numbers
  indcs = random.sample(range(N),N);

  # Changed the y values to +1, -1
  for i in range(N):
    if y[i] == 0:
      y[i] = -1

  t = 0
  mistakes_g = 99999
  mistakes = 0


  while t < T :

    # Look for a random mistake and correct it
    for i in indcs:
      if np.sign( w_y[i] ) != y[i] :
        w += y[i]*x[i]
        break
       

    # Calculate new Y vector using the "corrected" W
    w_y = np.dot( x, w )
   

    # Calculate number of mistakes using "corrected" W
    for i in range(N):
      if np.sign( w_y[i] ) !=  y[i] :
        mistakes += 1
     

    # If the new W makes less mistakes set g = W
    if mistakes < mistakes_g:
      mistakes_g = mistakes
      g = w.copy()
     


    #print("number of mistakes: " + str(mistakes))
    mistakes = 0
    t += 1


  

  return g, mistakes_g






  # place at the end to see stats

  #print("Least number of mistakes: " + str(mistakes_g))
  #print("g = ")
  #print(g)
  #print(y)
  #print( np.sign( np.dot( x, g )) )