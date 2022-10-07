import sys

def main(text): 
     x = sorted(sys.argv[1].split(), key = len)
     return x[0]
   
print("The shortest word is", main(sys.argv[1]).upper())