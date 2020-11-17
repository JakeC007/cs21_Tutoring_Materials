def recBinary(x,L):
  if len(L) == 0: #base case, when the answer isn't found
      print("False")
  else:
    #compute high, low, mid
    low = 0
    high = len(L)-1
    mid = int((high+low)/2)
    #if the answer is found, else recurse on desired side of the list
    if L[mid] == x: #base case when the answer is found
      print("True")
    elif L[mid] > x:
      recBinary(x,L[0:mid])
    else:
      recBinary(x,L[mid+1:])


def main():
  L = [1,2,3,4,5]
  ans = recBinary(, L)
main()
