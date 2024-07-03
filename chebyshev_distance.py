def chebyshev_distance(point1, point2):
    max_diff = 0
    for a, b in zip(point1, point2):
        max_diff = max(max_diff, abs(a - b))
    return max_diff


def chebyshev_distance(point1, point2):
    return max(map(lambda x: abs(x[0] - x[1]), zip(point1, point2)))


def chebyshev_distance(point1, point2):
    return max([abs(a - b) for a, b in zip(point1, point2)])
