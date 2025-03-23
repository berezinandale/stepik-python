def count_points_in_quadrants(points):

    q1 = q2 = q3 = q4 = 0

    for x, y in points:
        if x > 0 and y > 0:
            q1 += 1
        if x < 0 and y > 0:
            q2 += 1
        if x < 0 and y < 0:
            q3 += 1
        if x > 0 and y < 0:
            q4 += 1

    return q1, q2, q3, q4

def main():
    n = int(input())
    points = []

    for _ in range(n):
        x, y = map(int, input().split())
        points.append((x, y))

    q1, q2, q3, q4 = count_points_in_quadrants(points)

    print("Первая четверть:", q1)
    print("Вторая четверть:", q2)
    print("Третья четверть:", q3)
    print("Четвертая четверть:", q4)

if __name__ == "__main__":
    main()

