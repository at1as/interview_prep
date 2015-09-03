def create_summations(desired, stack = None):
  global results

  if stack is None:
    stack = []
  
  current_sum = sum(stack)

  if current_sum == desired:
    results.append(stack)

  if current_sum < desired:
    delta = desired - current_sum

    for x in range(1, delta + 1):
      create_summations(desired, stack + [x])


if __name__ == "__main__":

  # Given an interger, print all integers that can sum to the value
  # 4 -> [1, 1, 1, 1], [1, 1, 2], [1, 3], [4]
  # http://www.careercup.com/question?id=5957030143590400

  results = []

  create_summations(4)

  print results
