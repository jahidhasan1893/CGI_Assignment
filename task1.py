import matplotlib.pyplot as plt

def draw_line(x1, y1, x2, y2):
    points = []
    dx = x2 - x1
    dy = y2 - y1
    x = x1
    y = y1
    points.append((x, y))
    if dy > dx:
        p = 2 * dx - dy
        while y < y2:
            y += 1
            if p < 0:
                p += 2 * dx
            else:
                x += 1
                p += 2 * (dx - dy)
            points.append((x, y))
    else:
        p = 2 * dy - dx
        while x < x2:
            x += 1
            if p < 0:
                p += 2 * dy
            else:
                y += 1
                p += 2 * (dy - dx)
            points.append((x, y))
    return points

# Points A and B
x1, y1 = 1, 1
x2, y2 = 8, 4
points = draw_line(x1, y1, x2, y2)
print(points)

# Plotting the points
plt.figure(figsize=(6, 6))
plt.plot([x1, x2], [y1, y2], 'ro-', label='Line AB')
for point in points:
    plt.plot(point[0], point[1], 'bo')
    plt.text(point[0], point[1], f'({point[0]}, {point[1]})', fontsize=8, verticalalignment='bottom')
plt.xlabel('x')
plt.ylabel('y')
plt.title('Bresenham\'s Line Drawing Algorithm')
plt.grid(True)
plt.legend()
plt.show()
