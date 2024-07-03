def chebyshev_distance(point1, point2):
    max_diff = 0
    for a, b in zip(point1, point2):
        max_diff = max(max_diff, abs(a - b))
    return max_diff