def get_elevation(current: float, next: float) -> float:
    if next > current:
        return next - current

    return 0


def calculate_elevation(points: list) -> float:
    elevation = 0
    for i in range(len(points) - 1):
        elevation += get_elevation(points[i], points[i + 1])

    return elevation
