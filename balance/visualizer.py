from matplotlib import pyplot as plt


def plot_summary(data, group_by="category"):
    if not data:
        print("No data to plot.")
        return

    labels = [entry[group_by] for entry in data]
    totals = [entry["total"] for entry in data]

    plt.figure(figsize=(10, 6))

    if group_by == "category":
        plt.bar(labels, totals, color="skyblue")
        plt.title("Spending by Category")
        plt.xlabel("Category")
    elif group_by == "date":
        plt.plot(labels, totals, marker="o", linestyle="-", color="orange")
        plt.title("Spending Over Time")
        plt.xlabel("Date")
        plt.xticks(rotation=45)

    plt.ylabel("Amount")
    plt.tight_layout()
    plt.show()
