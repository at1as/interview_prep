import copy

class ResizeableHash(object):

	# Array storage implemeneted as list of seperate arrays
	# Hash value will point to sub-array that key is contained in
	# Making look up times much faster than the same implementation as one simple list
  # Dynamically resizes when a bucket exceeds max_bucket_length items

  # Limitations
	# * user cannot pass both a key and a vaule

	def __init__(self, max_bucket_length):
		self.max_bucket_length = max_bucket_length
		self.buckets = [[]]
		self.bucket_count = 1
		self.items = 0

	def unformatted_data(self):
		# Return unformatted hash data with all contents
		return self.buckets

	def data(self):
		# Return list of all values contained within all hash buckets
		data = []
		for bucket in self.buckets:
			for value in bucket:
				data.append(value)

		return data

	def item_count(self):
		# Return number of items in the array
		return self.items

	def bucket_count(self):
		# Return number of buckets in the hash
		return self.bucket_count

	def add(self, value):
		# Add a new value to the hash
		key = self.__hash_from_string(value, self.bucket_count)
		bucket_size = len(self.buckets[key])

		if not value in self.buckets[key]:
			self.buckets[key].append(value)
			self.items += 1

			if len(self.buckets[key]) > self.max_bucket_length:
				print "Resizing hash..."
				self.__resize_hash(self.buckets)
		else:
			print "Value already stored in Hash"

			
	def remove(self, value):
		# Remove a value from the hash
		removed = False
		key = self.__hash_from_string(value, self.bucket_count)
		
		for idx, stored_entry in enumerate(self.buckets[key]):
			if stored_entry is value:
				self.buckets[key].pop(idx)
				removed = True
				self.items -= 1

		if not removed:
			print "Value not found in Hash"


	def __hash_from_string(self, string, available_buckets):
		# Hashing algorithm
		sum = 0
		for c in str(string):
			sum += ord(c)

		return sum % available_buckets

	def __resize_hash(self, buckets):
		# Once a bucket in buckets contains more than the max allowed value 
		resize_again = False
		self.bucket_count += 1
		placeholder = [ [] for x in range(0, self.bucket_count) ]

		for bucket in buckets:
			for value in bucket:
				idx = self.__hash_from_string(value, self.bucket_count)
				placeholder[idx].append(value)

				if len(placeholder[idx]) > self.max_bucket_length:
					resize_again = True

		self.buckets = copy.deepcopy(placeholder)
		
		if resize_again:
			self.__resize_hash(self.buckets)
