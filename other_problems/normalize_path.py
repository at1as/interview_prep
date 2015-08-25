def path(relative_path):
  
  directory_buffer = ""
  directories = []

  for x in range(0, len(relative_path)):
    
    if relative_path[x] != "/":
      directory_buffer += relative_path[x]

      if x == len(relative_path) - 1:
        if not directory_buffer == "..":
          directories.append(directory_buffer)

      if directory_buffer == "..":
        directory_buffer = ""
        directories = directories[:-1]
    
    elif relative_path[x] == "/" or x == len(relative_path) - 1:
      if directory_buffer != "":
        directories.append(directory_buffer)
        directory_buffer = ""
  
  return "".join([directory + "/" for directory in directories])

if __name__ == "__main__":
  paths = [
      "/a/b/c",
      "/a/b/c/",
      "/a/b/../../e/",
      "/a/b/c/..",
      "/a/b/../../../../q/",
      "/////a",
      "a/b/../d"
      ]
  
  for path_example in paths:
    print "%s \n\t=> %s\n" %(path_example, path(path_example))
