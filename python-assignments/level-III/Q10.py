"""
10. A cafe has N computers. Several customers come to the cafe to
use these computers. A customer will be serviced only if there is
any unoccupied computer at the moment the customer visits the
cafe. If there is no unoccupied computer, the customer leaves the
cafe.
"""


def count_unsatisfied_customers(N, customers):
    occupied_computers = 0
    unsatisfied_customers = 0

    for _ in customers:
        if occupied_computers < N:
            occupied_computers += 1
        else:
            unsatisfied_customers += 1

    return unsatisfied_customers


N = int(input("Enter N: "))
customers = list(input("Enter customers: "))

result = count_unsatisfied_customers(N, customers)
print("Number of customers who couldn't get a computer:", result)
