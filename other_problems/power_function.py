#http://www.careercup.com/question?id=5709839151923200

def power(base, exponent, sum=0, count=1):
  if sum == 0:
    sum = base

  if count == exponent:
    return sum

  return power(base, exponent, sum * base, count + 1)


if __name__ == "__main__":
  print power(3, 6)
