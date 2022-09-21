l1 = {'one':1,'two':2,'three':3}
l2= ['a','b','c']
l3= ('x','y','z')
string = "qwerty"

print(zip())

for i in zip(l1,l2,l3):
    print(i)
        
""" using zip """
for i in zip():
    print(i)

"""using zip and converting the zip into tuple"""

print(tuple(zip(string)))

"""
output
(('q',), ('w',), ('e',), ('r',), ('t',), ('y',))
"""

"""using zip function along with range"""
for i in zip(range(1,3),l2):
    print(i)
    
"""
output
(1, 'a')
(2, 'b')

"""
"""
using zip to dictionary
"""
print(dict(zip(l1,string)))
"""
output
{'one': 'q', 'two': 'w', 'three': 'e'}
"""

"""
difference doc string and comment
->doc executes and comment not executes
->doc can be retrieved and comments can not be retrieved
"""