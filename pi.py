def show_tree(): # use function to draw a tree
  picture = [
    [0,0,0,1,0,0,0],
    [0,0,1,1,1,0,0],
    [0,1,1,1,1,1,0],
    [1,1,1,1,1,1,1],
    [0,0,0,1,0,0,0],
    [0,0,0,1,0,0,0],
  ]
    
  space = 0 # var access the 0 in nested list
  # var access the 1 in nested list
  aesthetic = 1
  for row in picture: # row in the nested list
    for item in row: # item takes the row value
      # Print out the space and aesthetic
      if item == space: 
        print(" ", end = "")
      elif item == aesthetic:
        print("*", end = "")
    print(" ")
  print("\n")# need a space after each row
show_tree()
