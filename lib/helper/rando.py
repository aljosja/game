import random


def rando():
  '''
  returns: random number between 0 and 1
  '''
  
  return random.random()

def randoSeed(seed):
  '''
  input: seed
  returns: the same random result between 0 and 1 based on seed

  '''
  if seed == None:
    return 0

  random.seed(seed)
  return random.random()

if __name__ == "__main__":
    print("\n=== This Module Contains ======")
    print("\nrando():")
    print(rando()) 
    print("\nrandoSeed(42):")
    print(randoSeed(42))
    print("\n===============================\n")