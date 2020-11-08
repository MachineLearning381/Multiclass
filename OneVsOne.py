import driver as d
from itertools import combinations

# X = transformed feature vecotor 
# Y = classification vector





def OvO(X,Y,n,T):

  y_vals = [0,1,2,3,4,5,6,7,8,9] 
  
  Y_c = Y.copy
  X_c = X.copy

  g = []
  g_mistakes = []
  T_vals = []

  # Y vector computed from Tournament Champions
  g_Y_multi = []
  # mistkaes made by the multiclassifier
  g_mistakes_multi = 0


 
  for combo in combinations(y_vals, 2): 

    # need to slice the data to get only
    # y[index] = i or y[index] = j
    # also need to slice X accordingly

    #X_c = 
    #Y_c = 

    # relabel the Y vector of the classes 
    # we are going to compare to +1, -1
    for l in Y_c.size:
      if( Y_c[l] == combo[0] ):
        Y_c[l] = 1
      else: 
        Y_c[l] = -1
      
    
    # find g for each comparision
    g_n, g_mistakes_n, T_n = d.regress_run(X,Y,.8,300);

    # store data to arrays
    g.append(g_n.copy)
    g_mistakes.append(g_mistakes_n)
    T_vals.append(T_n)

    # reset Y_c/X_c for the next comparison
    Y_c = Y.copy 
    X_c = X.copy



  # Find Tournament Champion
  for i in X:

    for j in g.size:

      # calculate vote for x 

  # classify x
  #



  # calculate number of errors made by
  # multiclassifier  g
  for i in Y.size:

    if( g_Y_multi[i] != Y[i] ):
      g_mistakes_multi += 1 

  
  

  return  g_mistakes_multi 






