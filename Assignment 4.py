INF = 999

# Initial network cost matrix
cost = [
    [0,   2,   5, INF],
    [2,   0,   1,   4],
    [5,   1,   0,   1],
    [INF, 4,   1,   0]
]

n = len(cost)

# Distance and next-hop tables
dist = [row[:] for row in cost]
next_hop = [[None] * n for _ in range(n)]

for i in range(n):
    for j in range(n):
        if i != j and cost[i][j] != INF:
            next_hop[i][j] = j

print("INITIAL COST MATRIX")
for row in cost:
    print(row)

# Distance Vector updates
updated = True
iteration = 0

while updated:
    updated = False
    iteration += 1

    for i in range(n):
        for j in range(n):
            for k in range(n):
                if dist[i][k] != INF and dist[k][j] != INF:
                    new_cost = dist[i][k] + dist[k][j]

                    if new_cost < dist[i][j]:
                        dist[i][j] = new_cost
                        next_hop[i][j] = next_hop[i][k]
                        updated = True

print("\nFINAL ROUTING TABLES")

for i in range(n):
    print(f"\nRouter {chr(65+i)}")
    print("Destination\tCost\tNext Hop")

    for j in range(n):
        if i == j:
            print(f"{chr(65+j)}\t\t0\t-")
        else:
            print(f"{chr(65+j)}\t\t{dist[i][j]}\t{chr(65+next_hop[i][j])}")

# Shortest path
source = int(input("\nEnter source router (A=0, B=1, C=2, D=3): "))
destination = int(input("Enter destination router (A=0, B=1, C=2, D=3): "))

path = [source]
current = source

while current != destination:
    current = next_hop[current][destination]
    path.append(current)

print("\nSHORTEST PATH")
print(" -> ".join(chr(65+x) for x in path))
print("Minimum Cost:", dist[source][destination])
