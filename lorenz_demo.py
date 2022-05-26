import math

c = 299792458

def lorenz_factor( velocity ):
  return 1 / math.sqrt(1 - ( velocity**2 / c**2))

def beta( velocity ):
  return velocity / c

#if __name__ == "__main__":
  #for i in range( 290000000, c, 100):
    #print( lorenz_factor(i), beta(i), -beta(i)*lorenz_factor(i) )

v = 0.98*c
lorenz_mat = [ [ lorenz_factor(v), -beta(v)*lorenz_factor(v), 0, 0],
               [ -beta(v)*lorenz_factor(v), lorenz_factor(v), 0, 0],
               [0, 0, 1, 0],
               [0, 0, 0, 1] ]

print("\n\n")
for i in lorenz_mat:
  for j in i:
    print(j, end=" ")
  print("")
print("\n\n")

print( 10 * lorenz_factor(v) * (-beta(v)*lorenz_factor(v)))