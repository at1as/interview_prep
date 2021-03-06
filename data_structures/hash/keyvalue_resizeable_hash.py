import copy

class KeyValueResizeableHash(object):

  # Hash storage implemented using arrays with a hashing algorithm
  # Dynamically resizes
  # Stores key - value pair

  def __init__(self, max_bucket_length):
    self.max_bucket_length = int(max_bucket_length)
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

  def get(self, key):
    found = False
    hash_key = self.__hash_from_string(key, self.bucket_count)

    for kv_pair in self.buckets[hash_key]:
      if kv_pair[0] is key:
        found = True
        return kv_pair[1]

    if not found:
      print "Could not find %s in hash" %(key)


  def add(self, key, value):
    # Add a new value to the hash
    hash_key = self.__hash_from_string(key, self.bucket_count)
    bucket_size = len(self.buckets[hash_key])

    if not key in [k for (k, v) in self.buckets[hash_key]]:
      self.buckets[hash_key].append([key, value])
      self.items += 1

      if len(self.buckets[hash_key]) > self.max_bucket_length:
        print "Resizing hash..."
        self.__resize_hash(self.buckets)
    else:
      print "Value already stored in Hash"

      
  def remove(self, key):
    # Remove a value from the hash
    removed = False
    hash_key = self.__hash_from_string(key, self.bucket_count)
    
    for idx, stored_entry in enumerate(self.buckets[hash_key]):
      if stored_entry[0] is key:
        self.buckets[hash_key].pop(idx)
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
        idx = self.__hash_from_string(value[0], self.bucket_count)
        placeholder[idx].append(value)

        if len(placeholder[idx]) > self.max_bucket_length:
          resize_again = True

    self.buckets = copy.deepcopy(placeholder)
    
    if resize_again:
      self.__resize_hash(self.buckets)
