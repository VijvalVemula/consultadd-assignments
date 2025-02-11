def count_customers_who_walked_away(N, S):
    occupied = set()
    visited = {}
    walked_away = 0

    for c in S:
        if c not in visited:
            visited[c] = True
            if len(occupied) < N:
                occupied.add(c)
            else:
                walked_away += 1  #
        else:
            if c in occupied:
                occupied.remove(c)

    return walked_away

N = int(input("Enter the number of customers: "))
S = input("Enter the string: ")

print(count_customers_who_walked_away(N, S))

