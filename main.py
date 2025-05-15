from balance.input_handler import get_cashflow_input
from balance.data_manager import init_db, save_cashflow, load_cashflow_from_csv, export_cashflow_to_csv
from balance.visualizer import plot_summary
from balance.summarizer import summarize_cashflow
import os
os.makedirs("exports", exist_ok=True)


def main():
    init_db()  # Ensure the database is initialized
    print("Welcome to your personal budget ledger!")
    while True:
        choice = input(
            """\nPress '1' to add Cashflow\n
            Press '2' to receive a summary for a specific timeslot\n
            Press '3' to upload a csv file\n
            press '4' to export your cashflow to a csv file\n
            Press '5' to exit\n
            Choose an option: """
            )
        if choice == "1":
            entry = get_cashflow_input()
            save_cashflow(entry)
        elif choice == "2":
            summary = summarize_cashflow()
            if input("Do you want to see a visual representation of your spending? (y/n) ").strip().lower() == 'y':
                group_by = input("Group by 'category' or 'date'? ").strip().lower()
                plot_summary(summary, group_by)
            else:
                print(summary)
        elif choice == "3":
            file_path = input("""
                              Enter CSV file path (remember that your csv must have
                              the following columns: date, amount, category and description):
                              """)
            entries = load_cashflow_from_csv(file_path)
            if entries:
                save_cashflow(entries)
                print(f"Imported {len(entries)} cashflow entries from CSV.")
            else:
                print("No valid cashflow entries found in the file.")
        elif choice == "4":
            file_path = input("Enter the path to save the CSV file: ")
            export_cashflow_to_csv(file_path)
            print(f"Cashflow exported to {file_path}.")
        elif choice == "5":
            break
        else:
            print("❌ Invalid choice.")


if __name__ == "__main__":
    main()
