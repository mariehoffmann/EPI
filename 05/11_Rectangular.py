__author__ = 'Marie Hoffmann ozymandiaz147@googlemail.com'

# Compute rectangular of intersection of two x-/y-axes aligned rectangles
# rectangles are given by bottom left and top right points
def rectangle_intersection(a, b):
    c = [[0, 0], [0, 0]]
    c[0][0] = max(a[0][0], b[0][0]) # largest x component of bottom left point
    c[0][1] = max(a[0][1], b[0][1]) # largest y component of bottom left point
    c[1][0] = min(a[1][0], b[1][0]) # smallest x component of top right point
    c[1][1] = min(a[1][1], b[1][1]) # smallest y component of top right point
    if c[1][0] - c[0][0] > 0 and c[1][1] - c[0][1] > 0:
        return c
    else:
        return None
# lx = (x,y) left bottom, rx = (x,y) right top
def rectangle_intersection2(rec1, rec2):
    l1, r1, l2, r2 = rec1[0], rec1[1], rec2[0], rec2[1]
    l3 = (max(l1[0], l2[0]), max(l1[1], l2[1]))
    r3 = (min(r1[0], r2[0]), min(r1[1], r2[1]))
    if r3[0] - l3[0] >= 0 and r3[1] - l3[1] >= 0:
        return (l3, r3)
    else:
        return None

if __name__ == "__main__":
    # overlapping, expect: [1,2][4,3]
    a = [[0,0], [4,3]]
    b = [[1,2], [5,4]]
    print(str(rectangle_intersection2(a, b)))

    # inclusion, expect b
    b = [[1, 1], [3,2]]
    print(str(rectangle_intersection2(a, b)))

    # non-overlapping, expect None
    a = [[3,0], [4,1]]
    print(str(rectangle_intersection(a, b)))
