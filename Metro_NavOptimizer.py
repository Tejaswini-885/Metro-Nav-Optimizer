cities = dict({
    0: "Yeshwanthpur",
    1: "Sriramapura",
    2: "Mysore road",
    3: "Chickpete",
    4: "VijayNagar",
    5: "Trinty",
    6: "Lalbagh",
    7: "Bellandur",
    8: "Cubbon Park"
})

ConnectedStations = [[0, 1], [0, 2], [0, 3], [0, 4], [0, 5], [0, 6], [0, 7], [0, 8],
                     [1, 2], [1, 3], [1, 4], [1, 5], [1, 6], [1, 7], [1, 8],
                     [2, 3], [2, 4], [2, 5], [2, 6], [2, 7], [2, 8],
                     [3, 4], [3, 5], [3, 6], [3, 7], [3, 8],
                     [4, 5], [4, 6], [4, 7], [4, 8],
                     [5, 6], [5, 7], [5, 8],
                     [6, 7], [6, 8],
                     [7, 8]]
DistanceInKM = [[2, 15, 11, 10, 11, 16, 18, 7],
                [14, 9, 9, 10, 14, 16, 4],
                [5, 8, 15, 3, 3, 2],
                [6, 12, 5, 7, 4],
                [16, 10, 9, 9],
                [13, 18, 14],
                [5, 1],
                [4]]
MetroFare = [[28, 30, 31, 24, 32, 30, 40, 20],
             [36, 32, 19, 27, 31, 34, 48],
             [14, 38, 25, 10, 15, 21],
             [18, 39, 16, 25, 17],
             [45, 26, 28, 39],
             [37, 51, 55],
             [21, 36],
             [31]]
TimeInMinutes = [[34, 15, 30, 14, 25, 29, 36, 13],
                 [17, 13, 13, 13, 16, 17, 26],
                 [16, 13, 14, 7, 7, 6],
                 [15, 12, 13, 13, 12],
                 [14, 11, 9, 35],
                 [26, 27, 27],
                 [10, 34],
                 [42]]

MetroAdjacencyList = []

for i in range(9):
    k = []
    for j in range(9):
        if i == j:
            continue
        l = []
        if i < j:
            l.append(j)
            l.append(DistanceInKM[i][j - 1 - i])
            l.append(MetroFare[i][j - 1 - i])
            l.append(TimeInMinutes[i][j - 1 - i])
        elif i > j:
            l.append(j)
            l.append(DistanceInKM[j][i - 1 - j])
            l.append(MetroFare[j][i - 1 - j])
            l.append(TimeInMinutes[j][i - 1 - j])
        k.append(l)
    if k:
        MetroAdjacencyList.append(k)


def Dijkshtra(From, To, index):
    k = [float('inf')] * 9
    v = [0] * 9
    k[From] = 0
    v[From] = 1
    p = [-1] * 9
    a = [[0, From]]
    while len(a) != 0:
        pres = a[0]
        a.pop(0)
        for i in MetroAdjacencyList[pres[1]]:
            if pres[0] + i[index] < k[i[0]]:
                k[i[0]] = pres[0] + i[index]
                a.append([k[i[0]], i[0]])
                p[i[0]] = pres[1]
        a.sort()
    z = []
    z.append(To)
    z.append(p[To])
    ele = p[To]
    while p[ele] != -1:
        z.append(p[ele])
        ele = p[ele]
    z.reverse()
    length = len(z)
    if index == 1:
        print("\nThe shortest Path from " + cities[From] + " to " + cities[To] + " is: ")
        for i in z:
            print(" -> " + cities[i], end="")
        time = 0
        cost = 0
        for i in range(1, length):
            if z[i - 1] > z[i]:
                time += TimeInMinutes[z[i]][z[i - 1] - 1 - z[i]]
                cost += MetroFare[z[i]][z[i - 1] - 1 - z[i]]
            if z[i - 1] < z[i]:
                time += TimeInMinutes[z[i - 1]][z[i] - 1 - z[i - 1]]
                cost += MetroFare[z[i - 1]][z[i] - 1 - z[i - 1]]
        print("\n\nThe Shortest Distance is: " + str(k[To]) + "KM")
        print("\nThe Cost is: " + str(cost) + "Rs")
        print("\nThe Time is: " + str(time) + "min")

    if index == 2:
        print("\nThe cheapest Path from " + cities[From] + " to " + cities[To] + " is: ")
        for i in z:
            print(" -> " + cities[i], end="")
        distance = 0
        time = 0
        for i in range(1, length):
            if z[i - 1] > z[i]:
                distance += DistanceInKM[z[i]][z[i - 1] - 1 - z[i]]
                time += TimeInMinutes[z[i]][z[i - 1] - 1 - z[i]]
            if z[i - 1] < z[i]:
                distance += DistanceInKM[z[i - 1]][z[i] - 1 - z[i - 1]]
                time += TimeInMinutes[z[i - 1]][z[i] - 1 - z[i - 1]]
        print("\n\nThe Minimum Cost is: " + str(k[To]) + "Rs")
        print("\nThe distance is: " + str(distance) + "KM")
        print("\nThe Time is: " + str(time) + "min")

    if index == 3:
        print("\nThe fastest path from " + cities[From] + " to " + cities[To] + " is: ")
        for i in z:
            print(" -> " + cities[i], end="")
        distance = 0
        cost = 0
        for i in range(1, length):
            if z[i - 1] > z[i]:
                distance += DistanceInKM[z[i]][z[i - 1] - 1 - z[i]]
                cost += MetroFare[z[i]][z[i - 1] - 1 - z[i]]
            if z[i - 1] < z[i]:
                distance += DistanceInKM[z[i - 1]][z[i] - 1 - z[i - 1]]
                cost += MetroFare[z[i - 1]][z[i] - 1 - z[i - 1]]
        print("\n\nThe Minimum Time is: " + str(k[To]) + "min")
        print("\nThe Cost is: " + str(cost) + "Rs")
        print("\nThe distance is: " + str(distance) + "KM")


def takeinput():
    print("Welcome to Namma Metro - A Metro way optimization system")
    print("Available Stations: ")
    for i in cities:
        print("code: " + str(i) + "\t\t" + str(cities[i]))
    print("Enter your From city code: ")
    From = int(input())
    print("Enter your destination city code: ")
    To = int(input())
    print("ThankYou for confirming the details")
    run = 1
    while run:
        print("Enter 1 if you want the shortest path")
        print("Enter 2 if you want the cheapest path")
        print("Enter 3 if you want the fastest path")
        print("Enter 4 to exit")
        path = int(input())
        if path == 1:
            Dijkshtra(From, To, 1)
            pass
        elif path == 2:
            Dijkshtra(From, To, 2)
            pass
        elif path == 3:
            Dijkshtra(From, To, 3)
            pass
        else:
            run = 0
            print("Thank You")


takeinput()
