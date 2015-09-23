# Class Node For File System
class Node:
	def __init__(self, fd, name):
		self.name = name
        	self.fd = fd
        	self.children = dict()
    	@property
    	def fd(self):
        	return self.fd
	@property
	def name(self):
		return self.name
    	@property
    	def children(self):
        	return self.children

    	def add_child(self, name, fd):
        	self.children[name] = fd
	
