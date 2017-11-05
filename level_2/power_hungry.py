"""
Problem Statement: 

Power Hungry
============

Commander Lambda's space station is HUGE. And huge space stations take a LOT of power. Huge space stations with doomsday devices take even more power. To help meet the station's power needs, Commander Lambda has installed solar panels on the station's outer surface. But the station sits in the middle of a quasar quantum flux field, which wreaks havoc on the solar panels. You and your team of henchmen has been assigned to repair the solar panels, but you can't take them all down at once without shutting down the space station (and all those pesky life support systems!). 

You need to figure out which sets of panels in any given array you can take offline to repair while still maintaining the maximum amount of power output per array, and to do THAT, you'll first need to figure out what the maximum output of each array actually is. Write a function answer(xs) that takes a list of integers representing the power output levels of each panel in an array, and returns the maximum product of some non-empty subset of those numbers. So for example, if an array contained panels with power output levels of [2, -3, 1, 0, -5], then the maximum product would be found by taking the subset: xs[0] = 2, xs[1] = -3, xs[4] = -5, giving the product 2*(-3)*(-5) = 30.  So answer([2,-3,1,0,-5]) will be "30".

Each array of solar panels contains at least 1 and no more than 50 panels, and each panel will have a power output level whose absolute value is no greater than 1000 (some panels are malfunctioning so badly that they're draining energy, but you know a trick with the panels' wave stabilizer that lets you combine two negative-output panels to produce the positive output of the multiple of their power values). The final products may be very large, so give the answer as a string representation of the number.

Languages
=========

To provide a Python solution, edit solution.py
To provide a Java solution, edit solution.java

Test cases
==========

Inputs:
    (int list) xs = [2, 0, 2, 2, 0]
Output:
    (string) "8"

Inputs:
    (int list) xs = [-2, -3, 4, -5]
Output:
    (string) "60"
"""

"""
Approach:

prevent Googal lies: 
  assert the absolute value of the range of all inputs is less than 1000 
    (-1000 <= PO <= 1000) or abs(panel output) <= 1000
  assert the length of the solar panel array is between 1 and 50
    1 <= len(arr) <= 50

filter out power output levels of 0 which will break the list_product
  if remaining length is 0 then all power levels were 0 and the output should be "0"

the product of two negatives can produce a positive power output for consideration
  do not consider any negative values outright

separate positive and negative values
  positive -> filter then reduce list product using list_product
  negative -> filter and then process according to even or odd list length
    even: get list_product for complete negative list
    odd: sort by magnitude -> pop last element -> get list_product for remaining list


NOTE: output as a string type


Approach:

  Notes:
    wired in series or parallel?
      no impact on power dissipation
    "sets of panels" 
      more than one panel?

    "returns the maximum product of some non-empty subset of those numbers"
      maximum product -> cumulatively multiply each element in the subset list
      non-empty -> minimum sized subset is length 1

    range of int values in the array?
      "each panel will have a power output level whose absolute value is no greater than 1000"
        power level <= abs(1000) --> -1000 <= power level <= 10000
        min, inclusive -> -1000
          negative values? -> "draining energy" due to malfunction
          "combine two negative-output panels to produce the positive output of the multiple of their power values"
            combine 2 negative values to create a positive output
              odd number of negative values?
                sort and drop the lowest (absolute) value
        max, inclusive -> 1000

    number of panels per array?
      at least 1 (min, inclusive) -> 1
      no more than 50 panels (max, inclusive) -> 50
    
  Input:
    list of int elements
      list length from 1 to 50 inclusive
      int element range -1000 to 1000 inclusive

  Output:
    string maximum output product
      calculate then cast as a string

  Special Consideration:

    0 -> 0 represents neither a positive nor negative output (neutral) but does impacts the maximum product mathematically and should NOT be considered
      filter out values == 0
    1 -> 1 represents a positive output but has no impact on the maximum product
   -1 -> -1 represents a negative output but DOES have an impact on the maximum product
      must be considered during the even or odd determination of the negative value count
      must NOT be filtered
    
    repeating values:
      positive: no impact
      negative: no impact

    all 0's:
      filtered out may produce an empty set
        OVERRIDE: must return "0" as maximum power output
    
    all 1's: no impact

    all -1's: dependent on length of the list
      even length: product of complete set -> 1
      odd length: would produce a negative output but handled by sort and drop step for negative values

  Pseudocode:
    1) filter list of 0's
      if filtered list length is 0 return "0"
    2) split into positive and negative lists
    3) cumulative product of positive list
    4) check length of negative list
      if even then cumulative product of negative list
      if odd then sort (low -> high, default) and remove last element (representing the smallest absolute value)
    5) calculate product of the positive nad negative cumulative products
    6) cast as string and return

  
  EDIT (failing test cases 3 and 4):
    failed to handle the case of a single element list
      returns the element as a string
        passed test case 4

    failed to handle the case of [0, -1]
      signified programatically by empty negative_values and positive_values
        return maximum output of 0
"""

def answer(xs):
  xs_length = len(xs)
  copy = xs[:]

  assert all(type(x) == int and x <= 1000 and x >= -1000 for x in xs)
  assert xs_length >= 1 and xs_length <= 50

  def cumulative_list_product(input_list):
    return reduce(lambda x, y: x * y, input_list, 1)

  if(xs_length == 1): return str(xs[0]) # single element list return the value

  positive_values = filter(lambda x: x > 0, copy)
  positive_cumulative_list_product  = cumulative_list_product(positive_values)

  negative_values = filter(lambda x: x < 0, copy)
  if len(negative_values) % 2 != 0: # uneven number of negative values
    negative_values.sort() # sort - default - from low to high
    negative_values.pop() # remove the last element (lowest absolute value negative)

  negative_cumulative_list_product = cumulative_list_product(negative_values)

  if not len(positive_values) and not len(negative_values): return "0" # handles edge case where 0 is the highest output
  return str(positive_cumulative_list_product * negative_cumulative_list_product)

from unit_tester import UnitTester

test_cases = [
  ([2, 0, 2, 2, 0], "8"), 
  ([-2, -3, 4, -5], "60"),
  ([2, -3, 1, 0, -5], "30"),
  ([1, -5, 0], "1"), 
  ([0, 0, 0, 0, 1], "1"), 
  ([0, 0, 0, 0, 0], "0"),
  ([-1, -1, -1], "1"),
  ([-1, -1, -1, -1], "1"),
  ([-5, -5, -5, 2], "50"),
  ([1, 1, 1, 1], "1"),
  ([-5], '-5'),
  ([-1], '-1'),
  ([2, 2], '4'),
  ([-2, -2], '4'),
  ([0, -1, -1], "1")
  # ([-1000 for i in range(49)], str(1000**48))
  ]
UnitTester(answer, test_cases).run()
