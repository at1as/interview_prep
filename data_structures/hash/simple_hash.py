class SimpleHash(object):

  # Array storage implemeneted as list of seperate arrays
  # Hash value will point to sub-array that key is contained in
  # Making look up times much faster than the same implementation as one simple list

  # Limitations:
  # * Unbounded contents per bucket
  # * no resizing of hash
  # * user cannot pass both a key and vaule

  def __init__(self, number_of_buckets):
    self.number_of_buckets = number_of_buckets
    self.buckets = [[] for x in range(0, self.number_of_buckets)]
    self.items = 0

  def unformatted_data(self):
    # Return unformatted SimpleHash with all contents
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
    return self.number_of_buckets

  def add(self, value):
    # Add a new value to the hash
    key = self.__hash_from_string(value)
    if not value in self.buckets[key]:
      self.buckets[key].append(value)
      self.items += 1
    else:
      print "Value already stored in Hash"

  def remove(self, value):
    # Remove a value from the hash
    removed = False
    key = self.__hash_from_string(value)
    
    for idx, stored_entry in enumerate(self.buckets[key]):
      if stored_entry is value:
        self.buckets[key].pop(idx)
        removed = True
        self.items -= 1

    if not removed:
      print "Value not found in Hash"



  def __hash_from_string(self, string):
    # Hashing algorithm
    sum = 0
    for c in str(string):
      sum += ord(c)

    return sum % self.number_of_buckets

