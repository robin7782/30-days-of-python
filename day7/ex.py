Python 3.7.9 (tags/v3.7.9:13c94747c7, Aug 17 2020, 18:58:18) [MSC v.1900 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license" for more information.
>>> #creating an empty set
>>> st{}
  File "<stdin>", line 1
    st{}
      ^
SyntaxError: invalid syntax
>>> st={}
>>> #or another type
>>> st=set()
>>> #creating a set with initial items
>>> st={'i1','i2'}
>>> print(st)
{'i2', 'i1'}
>>> # how to calculate lenth
>>> st={'i1','i2'}
>>> len(st)
2
>>> #accessing item in a set
>>> st={'i1','i2'}
>>> print("",'i1' in st)
 True
>>> #adding ietms to sets
>>> st={'i1','i2'}
>>> #add single data in set
>>> st={'i1','i2'}
>>> st.add('i3')
>>> st.add('i3')
>>> print(st)
{'i2', 'i3', 'i1'}
>>> #for multiple adding
>>> st.update(['i2', 'i3', 'i1', 'i4','i5'])
>>> st.print
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
AttributeError: 'set' object has no attribute 'print'
>>> print(st)
{'i3', 'i2', 'i5', 'i4', 'i1'}
>>> #removing items from a set
>>> set.remove('i5')
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: descriptor 'remove' requires a 'set' object but received a 'str'
>>> set.remove('i5')
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: descriptor 'remove' requires a 'set' object but received a 'str'
>>> print(set)
<class 'set'>
>>> set = {'i3', 'i2', 'i5', 'i4', 'i1'}
>>> set.remove('i5')
>>> print(set)
{'i3', 'i2', 'i4', 'i1'}
>>> #remove the last element from the set
>>> print(set)
{'i3', 'i2', 'i4', 'i1'}
>>> st.pop()
'i3'
>>> st.pop()
'i2'
>>> st.pop()
'i5'
>>> st.pop()
'i4'
>>> st.pop()
'i1'
>>> st.pop()
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
KeyError: 'pop from an empty set'
>>> set = {'i3', 'i2', 'i5', 'i4', 'i1'}
>>> #clearing item in a set
>>> set.clear()
>>> print(set)
set()
>>> set = {'i3', 'i2', 'i5', 'i4', 'i1'}
>>> del i3
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'i3' is not defined
>>> set = {'i3', 'i2', 'i5', 'i4', 'i1'}
>>> del set
>>> print(set)
<class 'set'>
>>> set = {'i3', 'i2', 'i5', 'i4', 'i1'}
>>> #coverting a list to set
>>> set = {'i3', 'i2', 'i5', 'i4', 'i1'}
>>> list = ['i3', 'i2', 'i5', 'i4', 'i1']
>>> set = set(list)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: 'set' object is not callable
>>> s = set(list)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: 'set' object is not callable
>>> list = ['i3', 'i2', 'i5', 'i4', 'i1']
>>> s = set(list)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: 'set' object is not callable
>>> list=set(list)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: 'set' object is not callable
>>> lis = ['i3', 'i2', 'i5', 'i4', 'i1']
>>> lis = set(lis)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: 'set' object is not callable
>>> lis = ['i3', 'i2', 'i5', 'i4', 'i1']
>>> s = {}
>>> s = set(lis)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: 'set' object is not callable
>>> set.clear
<built-in method clear of set object at 0x00000242E0E07128>
>>> set.clear()
>>> lis = ['i3', 'i2', 'i5', 'i4', 'i1']
>>> s = set(lis)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: 'set' object is not callable
>>> p = {}
>>> l = {'fupu','nanu','kaka','amma', 'abba'}
>>> p = set(l)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: 'set' object is not callable
>>>
it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}
age = [22, 19, 24, 25, 26, 24, 25, 24]

#Problem 1
print(len(it_companies))

#Problem 2
it_companies.add('insta')
print(it_companies)

#Problem 3
it_companies.update(['Facebook', 'Bkdsl'])
print(it_companies)

#Problem 4
it_companies.remove('selu')
print(it_companies)

#Problem 6
print(A.union(B))

#Problem 7
print(A.intersection(B))

#Problem 8
print(A.issubset(B))

#Problem 9
print(A.isdisjoint(B))

#Problem 10
print(A.union(B))
print(B.union(A))

#Problem 11
print(A.symmetric_difference(B))

#Problem 12
del A
del B

#Problem 13
ages = set(age)
print(ages)
print(len(age))
print(len(ages))

#Problem 15
words = ['I', 'am', 'a', 'teacher', 'and', 'I', 'love', 'to', 'inspire', 'and', 'teach', 'people']
unique_words = set(words)
print(unique_words)
print(len(unique_words))

