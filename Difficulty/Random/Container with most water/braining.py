height = [1, 8, 6, 2, 5, 4, 8, 3, 7]

def smallest_h(h1,h2):
    if h1<h2:
        smallest = h1
    else:
        smallest = h2

    return smallest
for x, h in enumerate(height):
    print(f"Case: {(x + 1, h)}")
    for _x, _h in enumerate(height):
        print(f"from {(x + 1, h)} to {(_x + 1, _h)}")
        # Calculate the area btn them
        w=smallest_h(height[x], height[_x])
        l = abs((x - _x))
        area = l*w
        print(f"Area: {l} * {w} = {area}")
