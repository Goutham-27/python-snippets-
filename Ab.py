#assigning elements to different lists
colors = ['red', 'blue', 'green']
  print colors[0]    ## red
  print colors[2]    ## green
  print len(colors)  ## 3
Output:
b = colors   ## Does not copy the list

#accessing elements from a tuple
tup1 = ('physics', 'chemistry', 1997, 2000);
tup2 = (1, 2, 3, 4, 5, 6, 7 );
print "tup1[0]: ", tup1[0];
print "tup2[1:5]: ", tup2[1:5];
O/p:
tup1[0]:  physics
tup2[1:5]:  [2, 3, 4, 5]

#deleting different dictionary elements 
syntax:
dict.clear()
Example:
inp_dict = {"A":"Python","B":"Java","C":"Fortan","D":"Javascript"}
print("Elements of the dict before performing the deletion operation:\n")
print(str(inp_dict))
inp_dict.clear()
print("\nElements of the dict after performing the deletion operation:")
print(str(inp_dict))
Output:Elements of the dict before performing the deletion operation:
 
{'B': 'Java', 'D': 'Javascript', 'C': 'Fortan', 'A': 'Python'}
 
Elements of the dict after performing the deletion operation:
{}
