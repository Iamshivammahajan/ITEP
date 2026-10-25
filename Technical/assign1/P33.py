length = 30 
breadth = 20 
path1 = 3 
path2 = 4 
garden_area = length * breadth 
path_area = (length * path1) + (breadth * path2) - (path1 * path2) 
usable_area = garden_area - path_area 
print("Usable area =", usable_area, "m²")