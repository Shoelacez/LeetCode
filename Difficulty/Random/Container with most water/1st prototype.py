height = [1, 8, 6, 2, 5, 4, 8, 3, 7]
# height = [1,1]

def smallest_h(h1,h2):
    if h1<h2:
        smallest = h1
    else:
        smallest = h2

    return smallest

areas = []
for x, h in enumerate(height):
    # print(f"Case: {h}")
    for _x, _h in enumerate(height):
        # Calculate the area btn them
        w=smallest_h(height[x], height[_x])
        l = abs((x - _x))
        area = l*w
        # print(area)
        areas.append(area)

print(areas)

uniques = []
for a in areas:
    if a in uniques:
        pass
    else:
        uniques.append(a)

print(uniques)

'''Container with the most water'''
print(max(uniques))