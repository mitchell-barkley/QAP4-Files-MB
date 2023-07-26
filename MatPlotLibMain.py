# Program Description: QAP4 MatPlotLib
# Written By: Mitchell Barkley
# Written On: July 21st 2023

# Libraries
import matplotlib
from matplotlib import pyplot as plt

# Main
while True:
    print()
    print("============================================================")
    print("                 MONTHLY REVENUE CHART")
    print("============================================================")
    print("Please enter the revenue for each month (0 for months with no data): ")
    Revenue = []
    Months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
    Count = 0
    for i in Months:
        RevenueItem = float(input(f"Enter the revenue for {Months[Count]}: "))
        Revenue.append(RevenueItem)
        Count += 1

    plt.plot(Months, Revenue)
    plt.scatter(Months, Revenue, marker="o", color="blue")
    plt.xlabel('Months')
    plt.ylabel('Revenue ($)')
    plt.title('Monthly Revenue')
    plt.grid(True)
    plt.show()
    print()
    Continue = input("Would you like to enter another report? (Y/N): ").upper()
    if Continue == "N":
        break
