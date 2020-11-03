"""
You are the manager of a number of employees who all sit in a row. The CEO would like to give all of your employees bonuses, but since the company did not perform so well this year the CEO would like to keep the bonuses to a minimum.

The rule of the distribution:
- Each Employee begins with a bonus factor of 1x.
- For each employee, if they perform better than the persoin sitting next to them, the employee is given a +1 higher bonus (and up to +2 if they perform better than both people to their sides).

Given a list of employee's performance, find the bonuses each employee should get. 

Example:
Input: [1,2,3,2,3,5,1]
Output: [1,2,3,1,2,3,1]
"""

def getBonuses(performance):
  #Count to keep track of lenght of array.
  count = len(performance)
  #Initialize all the workers to 1
  bonus = [1] * count

  #Loop through the array from first element to the length
  for i in range(1, count):
    #If the person to the left of this worker did worse, then we increase his/her bonus
    if performance[i-1] < performance[i]:
      bonus[i] = bonus[i-1] + 1

  #Loop from the maximum length - 2, to -1 in the list, and incremenet by -1
  for i in range(count - 2, -1, -1):
    #If they have a better rating than the person to the right, their bonus is increased
    if performance[i+1] < performance[i]:
      #If their bonus is already higher than the worker to the right + 1, leave it as is
      bonus[i] = max(bonus[i], bonus[i+1] + 1)
  
  #Return your results 
  return bonus

print("The workers ratings are: " + str([1,2,3,4,5,1]))
print("So their bonuses will be: " + str(getBonuses([1,2,3,4,5,1])))
