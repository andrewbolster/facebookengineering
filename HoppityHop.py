#! /usr/bin/env python
#HoppityHop
#Created for Facebook Engineering Puzzles by Andrew Bolster
# andrew.bolster@gmail.com

#REQUIREMENTS
#  Input:
#    Positive Int : n
#  Output:
#    For 1..n
#    %3 : Hoppity
#    %5 : HopHop
#    %3 AND %5 : Hop


n = int(raw_input("Please Enter an Integer: "))

for this in range(1,n):
  if (this % 3 == 0) and (this % 5 == 0):
    print 'Hop'
  elif (this % 3 == 0):
    print 'Hoppity'
  elif (this % 5 == 0):
    print 'HopHop'



  
