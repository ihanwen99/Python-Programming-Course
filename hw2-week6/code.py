def slope(p1, p2):
    if p2[0] - p1[0] == 0:
        return "Not Exists."
    return float(p2[1] - p1[1]) / (p2[0] - p1[0])


def intercept(p1, p2):
    if p2[0] - p1[0] == 0:
        return "Also Not Exists."
    k = slope(p1, p2)
    return p1[1] - (k * p1[0])


if __name__ == '__main__':
    point_list = []
    for i in range(2):
        x = input("Please input x coord of point{} : ".format(i))
        y = input("Please input y coord of point{} : ".format(i))
        point_list.append((x, y))

# print(point_list)
print("Slope is {}".format(slope(point_list[0], point_list[1])))
print("Intercept is {}".format(intercept(point_list[0], point_list[1])))
