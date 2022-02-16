def split_land(x: int, y: int):
    """
    x: width of land
    y: height of land
    """
    min_land = min(x, y)
    max_land = max(x, y)

    if max_land == min_land:
        return min_land

    if remaining := max_land - min_land:
        return split_land(remaining, min_land)
    return -1


if __name__ == "__main__":
    max_plot = split_land(1680, 640)
