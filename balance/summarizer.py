from balance.data_manager import get_summary


def summarize_cashflow():
    start = input("Enter start date (YYYY-MM-DD): ").strip()
    end = input("Enter end date (YYYY-MM-DD): ").strip()
    group_by = input("Group by 'category' or 'date'? ").strip().lower()

    try:
        summary = get_summary(start, end, group_by)
        print(f"\nSummary ({group_by}) from {start} to {end}:")
        for row in summary:
            print(f"{row[group_by]}: €{row['total']:.2f}")
    except ValueError as ve:
        print(f"Error: {ve}")
    except Exception as e:
        print(f"Something went wrong: {e}")
    return summary
