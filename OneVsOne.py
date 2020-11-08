import driver as d
import numpy as np
from itertools import combinations

# X = transformed feature vecotor 
# Y = classification vector



def OvO(X,Y,n,T):

  y_vals = [0,1,2,3,4,5,6,7,8,9] 
  combos = []
  votes = [0,0,0,0,0,0,0,0,0,0]

  Y_c = Y.copy()
  
  g = []
  g_mistakes = []
  T_vals = []

  # Y vector computed from Tournament Champions
  g_Y_multi = []
  # mistkaes made by the multiclassifier
  g_mistakes_multi = 0


 
  for combo in combinations(y_vals, 2): 

    # keep track of the combos for voting
    # first g corresponds to first combo ... etc
    combos.append(combo)

    # relabel the Y vector of the classes 
    # we are going to compare to +1, -1
    for i in range(Y_c.size):
      if( Y_c[i] == combo[0] ):
        Y_c[i] = 1
      elif( Y_c[i] == combo[1] ): 
        Y_c[i] = -1
      else:
        Y_c[i] = 0

   

    # find g for each comparision
    g_n, g_mistakes_n, T_n = d.regress_run(X,Y_c,.8,300);


    # store data to arrays
    g.append(g_n.copy)
    g_mistakes.append(g_mistakes_n)
    T_vals.append(T_n)


    # reset Y_c for the next comparison
    Y_c = Y.copy()
    



  # Find Tournament Champion
  for i in range(X.size):

    for j in range(g.size):
      
      # get vote from every comparision
      classification = g[j] * X[i]

      # calculate vote for x 
      if( np.sign(classification) == 1 ):
        votes[ combo[j][0] ] += 1
      else:
        votes[ combo[j][1] ] += 1


    # classify x
    max = 0 
    for v in range(votes.size):
      if( votes[ v ] > max):
        max = votes[v]
        g_Y_multi[i] = v
    
    #reset vote array
    votes = [0,0,0,0,0,0,0,0,0,0]    


    
  # calculate number of errors made by
  # multiclassifier  g
  for i in range(Y.size):

    if( g_Y_multi[i] != Y[i] ):
      g_mistakes_multi += 1 

  
  

  return  g_mistakes_multi 






