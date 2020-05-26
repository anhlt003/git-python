# exception StopIteration
# The StopIteration error is raised by built-in function next() and an iterator‘s __next__() method to signal that all items are produced by the iterator
# -------------------------------------------------------------------------------------------------------
arr = [1,2,3,4,5,6]
a = next(b for b in arr if b - 6 <= 0)
c = []
c.append(a)
print (c)
# ---------------------------
Arr = [3, 1, 2] 
i=iter(Arr) 
  
print i 
print i.next() 
print i.next() 
print i.next() 
print i.next()
# -------------------------------------------------------------------------------------------------------
# from __future__ import annotations
# @properties.
# Use annotation getter/setter/deleter to create method access protected properties.
class House:
	def __init__(self, price):
		self._price = price

	@property
	def price(self):
		return self._price
	
	@price.setter
	def price(self, new_price):
		if new_price > 0 and isinstance(new_price, float):
			self._price = new_price
		else:
			print("Please enter a valid price")

	@price.deleter
	def price(self):
		del self._price

# set // 
# like a list but access by value instead index. 
s = set([1,2,'a','b','c'])
s.remove('a')
print(s)
for i in s: 
    print(i)