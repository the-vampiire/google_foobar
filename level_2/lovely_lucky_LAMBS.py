def answer(total_lambs):
  if total_lambs < 10 or total_lambs > 1000000000: return 0 # Because Googal lied to me :[
  def distributor(generous):
    henchman_minus_2_payout = 1
    henchman_minus_1_payout = 2 if generous else 1
    paid_henchman_count = 2
    remaining_LAMBs = total_lambs - henchman_minus_2_payout - henchman_minus_1_payout
    
    while(True):  # handles rules 1) - 3)
      requested_payout = (2 * henchman_minus_1_payout) if generous else (henchman_minus_2_payout + henchman_minus_1_payout)

      rule = (requested_payout > (henchman_minus_1_payout + henchman_minus_2_payout))
      if (generous and not rule) or requested_payout > remaining_LAMBs: break

      henchman_minus_2_payout = henchman_minus_1_payout
      henchman_minus_1_payout = requested_payout
      remaining_LAMBs -= requested_payout
      paid_henchman_count += 1
      
    if remaining_LAMBs > 0 and remaining_LAMBs >= henchman_minus_1_payout + henchman_minus_2_payout:
       paid_henchman_count += 1 # handles rule 4)
    return paid_henchman_count
  return distributor(generous = False) - distributor(generous = True)

print(answer(13))

"""
Problem Statement:

Lovely Lucky LAMBs
==================

Being a henchman isn't all drudgery. Occasionally, when Commander Lambda is feeling generous, she'll hand out Lucky LAMBs (Lambda's All-purpose Money Bucks). Henchmen can use Lucky LAMBs to buy things like a second pair of socks, a pillow for their bunks, or even a third daily meal!

However, actually passing out LAMBs isn't easy. Each henchman squad has a strict seniority ranking which must be respected - or else the henchmen will revolt and you'll all get demoted back to minions again! 

There are 4 key rules which you must follow in order to avoid a revolt:
    1. The most junior henchman (with the least seniority) gets exactly 1 LAMB.  (There will always be at least 1 henchman on a team.)
    2. A henchman will revolt if the person who ranks immediately above them gets more than double the number of LAMBs they do.
    3. A henchman will revolt if the amount of LAMBs given to their next two subordinates combined is more than the number of LAMBs they get.  (Note that the two most junior henchmen won't have two subordinates, so this rule doesn't apply to them.  The 2nd most junior henchman would require at least as many LAMBs as the most junior henchman.)
    4. You can always find more henchmen to pay - the Commander has plenty of employees.  If there are enough LAMBs left over such that another henchman could be added as the most senior while obeying the other rules, you must always add and pay that henchman.

Note that you may not be able to hand out all the LAMBs. A single LAMB cannot be subdivided. That is, all henchmen must get a positive integer number of LAMBs.

Write a function called answer(total_lambs), where total_lambs is the integer number of LAMBs in the handout you are trying to divide. It should return an integer which represents the difference between the minimum and maximum number of henchmen who can share the LAMBs (that is, being as generous as possible to those you pay and as stingy as possible, respectively) while still obeying all of the above rules to avoid a revolt.  For instance, if you had 10 LAMBs and were as generous as possible, you could only pay 3 henchmen (1, 2, and 4 LAMBs, in order of ascending seniority), whereas if you were as stingy as possible, you could pay 4 henchmen (1, 1, 2, and 3 LAMBs). Therefore, answer(10) should return 4-3 = 1.

To keep things interesting, Commander Lambda varies the sizes of the Lucky LAMB payouts: you can expect total_lambs to always be between 10 and 1 billion (10 ^ 9).                                                                                                                            NOT TRUE ^^^^^

Languages
=========

To provide a Python solution, edit solution.py
To provide a Java solution, edit solution.java

Test cases
==========

Inputs:
    (int) total_lambs = 10
Output:
    (int) 1

Inputs:
    (int) total_lambs = 143
Output:
    (int) 3
"""

"""
Approach: 

  Rules:
    1) there will be at minimum 1 henchman and they will get 1 LAMB
      starting value is always 1
        10 is the minimum LAMBs
        1,000,000,000 is maximum LAMBs

    2) revolt if next henchman has more than double
       next henchman can be at most 2 * the previous henchman payout
         next henchman payout <= 2 * previous payout

    3) revolt if total LAMB payment to previous 2 henchman is more than double
       next henchman must be >= than previous 2 henchman payouts combined

    4) check remaining LAMBs and increase the number of henchman paid by issuing those LAMBs
          ensure that rules 1) - 3) are abided by before distributing

    NOTE: LAMB can not be subdivided - always distributed as integers

  Need:
    two distributor functons are needed: generous and greedy
      generous -> use maximum rules
        1) next henchman payout = 2 * previous payout
        2) [index 2+] next henchman payout > previous 2 payouts combined

      greedy -> use minimum rules
        1) next henchman payout = henchman_minus_1_payout + henchman_minus_2_payout
        2) [index 2+] next henchman payout == previous 2 payouts combined

      in both distributor functions
        index 0 -> 1
        index 1 -> first rule applies
        index 2 -> first and second rules apply 

    calculate both a generous and greedy output (number of henchman that can be paid under each rule-set)
      calculate the difference between the outputs and return the value

    NOTE: rather than store a list of payouts (will crash for large values of total_lambs)
          use the following approach

          Variables:
            henchman_minus_1_payout (last henchman payout)
              initial value (generous distributor function) -> 2
              initial value (greedy distributor function) -> 1

            henchman_minus_2_payout (last last henchman payout)
              initial value (both distributor functions) -> 1

            requested_payout (the next calculated payout)
              apply respective distibutor function rules to calculate

            remaining_lambs (amount remaining after removing the last payout)
              initial value (both distributor functions) -> total_lambs - henchman_minus_2_payout - henchman_minus_1_payout

            paid_henchman_count (number of henchman who have been paid)
              initial value (both dsitributor functions) -> 2 (initial 2 henchman)

          Pseudocode:
            calculate requested_payout for the next henchman
              if requested_payout <= remaining_lambs then a payout is possible 
                henchman_minus_2 = henchman_minus_1
                henchman_minus_1 = requested payout
                paid_henchman_count += 1
                remaining_lambs -= requested_payout
                  loop
                    break when requested_payout > remaining_lambs
                    return paid_henchman_count

EDITS:
  assert type(total_lambs) == int --> passed
  assert total_lambs > 0 --> passed
  assert total_lambs > 10 --> failed (problem statement lied)
  assert total_lambs > 1 -->  passed
  assert total_lambs != 2 --> FAILED (you lied to me Googal :[ )

    added a bounds check which returns 0 for out of bounds 
    added support for rule 4) 
"""