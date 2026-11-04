path_length = 120 * 100 
path_breadth = 2.4 * 100 
brick_length = 24 
brick_breadth = 15 
path_area = path_length * path_breadth 
brick_area = brick_length * brick_breadth 
bricks = path_area / brick_area 
print("Bricks required =", int(bricks))