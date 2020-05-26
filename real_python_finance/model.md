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


# __hash__ // __repr__
# if __str__ not defined and __repr__ will be used as fallback
# __repr__ can return to any expression in python grammar
batch_01 = Batch('batch_01','BitCoin',300,today) 
print(batch_01)
print(batch_01.__hash__())
print(hash(batch_01))


# __gt__ //greate than starndard definition
# __le__ //less than or equal starndard definition
print ((2.5).__gt__(1))
print ((1).__le__(1))
def __le__(self,other): 
	if self.batch_time is None:
		return False
	if other.batch_time is None:
		return True
	return self.batch_time <= other.batch_time    