import sys

# define a class called Rope
class Rope:
	# initialize the class with a string
	def __init__(self, s):
		self.string = s
	
	# return the current string
	def result(self):
		return self.string
	
	# process the rope by taking a substring from start to end and inserting it at insert_index
	def process(self, start, end, insert_index):
		substring = self.string[start:end + 1]
		self.string = self.string[:start] + self.string[end + 1:]
		if insert_index == 0:
			self.string = substring + self.string
		else:
			self.string = self.string[:insert_index] + substring + self.string[insert_index:]

# read in a string from standard input and create a Rope object
rope = Rope(sys.stdin.readline().strip())

# read in the number of queries
num_queries = int(sys.stdin.readline())

# process each query
for _ in range(num_queries):
	# read in the start, end, and insert_index for the current query
	start, end, insert_index = map(int, sys.stdin.readline().strip().split())
	
	# process the rope with the current query
	rope.process(start, end, insert_index)

# print the final result of the rope
print(rope.result())
