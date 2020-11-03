"""
H-Index

The H-index is a metric that attempt to measure the productivity and citation impact of the publication of a scholar. The definition of H-index is if a scholar has a least h of their papers cited h times.

Given a list of publications of the number of citations a scholar has, find their h-index.

Example:
Input: [3,5,0,1,3]
Output: 3
Explanation:
there are 3 publications with 3 or more citations, hence the h-index is 3.

Here's a starting point:
"""

def hIndex(publications):
  # Get the length of the publications array
  n = len(publications)
  # Create a citations array with the len of publications + 1 (For later use)
  citations = [0] * (n + 1)

  # Loop through publications values and check if the value is less than the length
  for pub in publications:
  # If the value is less than the length then the citations array and index(That value) + 1
    if pub < n:
      citations[pub] += 1
    # If the value at pub is greater than or equal to the length of publications you add 1 at that n index
    else:
      citations[n] += 1
  
  total = 0
  i = n
  # Now you have to itterate backwards to find H-index
  while i > 0:
    total += citations[i]
    # If your total matches the current index value, you know that you have found your
    # maximum publication score given the ascneded order of the citaitons array
    if total >= i:
      return i
    i -= 1
    # You then return your H-Index being that index that surpasses total
  return i


print("Your publication citations are: " + str([5,3,3,1,0]))
print("Your H-Index is: " + str(hIndex([5,3,3,1,0])))
# The result should be 3