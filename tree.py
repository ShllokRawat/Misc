class Tree:

	def __init__(self, data, branches):
		self.data = data
		for b in branches:
			assert isinstance(b, Tree)
		self.branches = branches

	def is_leaf():
		return self.branches == []




