import pandas as pd
import matplotlib.pyplot as plt

data = {
    "Customer": [
        "Aman", "Riya", "Rahul", "Sneha",
        "Karan", "Pooja", "Neha", "Arjun"
    ],
    "City": [
        "Delhi", "Mumbai", "Lucknow", "Pune",
        "Delhi", "Mumbai", "Pune", "Lucknow"
    ],
    "Account_Type": [
        "Savings", "Current", "Savings", "Current",
        "Savings", "Current", "Savings", "Current"
    ],
    "Balance": [
        85000, 120000, 65000, 150000,
        98000, 110000, 72000, 135000
    ],
    "Transactions": [
        25, 40, 18, 52,
        30, 35, 22, 48
    ]
}

df = pd.DataFrame(data)

print("Bank Customer Analysis")
print(df)

print("\nHead")
print(df.head())

print("\nTail")
print(df.tail())

print("\nInfo")
df.info()

print("\nDescribe")
print(df.describe())

Highest_Balance = df["Balance"].max()
print("\nHighest Balance:", Highest_Balance)

Lowest_Balance = df["Balance"].min()
print("\nLowest Balance:", Lowest_Balance)

Customer_Highest_Balance = df.loc[df["Balance"].idxmax()]
print("\nCustomer with Highest Balance")
print(Customer_Highest_Balance)

Customer_Lowest_Balance = df.loc[df["Balance"].idxmin()]
print("\nCustomer with Lowest Balance")
print(Customer_Lowest_Balance)

High_Balance = df[df["Balance"] > 100000]
print("\nCustomers with Balance > 100000")
print(High_Balance)

Savings_Account_Customers = df[df["Account_Type"] == "Savings"]
print("\nSavings Account Customers")
print(Savings_Account_Customers)

Current_Account_Customers = df[df["Account_Type"] == "Current"]
print("\nCurrent Account Customers")
print(Current_Account_Customers)

Total_Balance = df.groupby("City")["Balance"].sum()
print("\nCity Wise Total Balance")
print(Total_Balance)

Average_Balance = df.groupby("Account_Type")["Balance"].mean()
print("\nAccount Wise Average Balance")
print(Average_Balance)

Total_Customers = df["City"].value_counts()
print("\nNumber of Customers in Each City")
print(Total_Customers)

print("\nUnique Cities")
print(df["City"].unique())

print("\nNumber of Unique Cities")
print(df["City"].nunique())

df = df.rename(columns={"Balance": "Bank Balance"})

print("\nRenamed Dataset")
print(df.head())

df["Interest"] = df["Bank Balance"] * 0.06

df["Final Balance"] = df["Bank Balance"] + df["Interest"]

df["Percentage Contribution"] = (
    df["Final Balance"] / df["Final Balance"].sum()
) * 100

print("\nPercentage Contribution")
print(df[["Customer", "Percentage Contribution"]])

df = df.sort_values(
    ["Transactions", "Bank Balance"],
    ascending=[False, False]
)

print("\nSorted Data")
print(df)

High_Balanced_Customers = df[
    (df["Bank Balance"] > 100000) &
    (df["Transactions"] > 30)
]

print("\nCustomers with Balance >100000 AND Transactions >30")
print(High_Balanced_Customers)

plt.bar(df["Customer"], df["Final Balance"])
plt.title("Customer VS Final Balance")
plt.xlabel("Customer")
plt.ylabel("Final Balance")
plt.show()

City_Balance = df.groupby("City")["Final Balance"].sum()

plt.bar(City_Balance.index, City_Balance.values)
plt.title("City VS Total Balance")
plt.xlabel("City")
plt.ylabel("Final Balance")
plt.show()