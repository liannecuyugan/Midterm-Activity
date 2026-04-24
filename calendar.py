class Calendar:
    def __init__(self):
        # This dictionary stores all events
        # Key = " YYYY-MM-DD",Value = list of events
        self.events = {}

    def is_leap_year(self, year):
        if year % 4 == 0:
            return True
        else:
            return False

    def get_days_in_month(self, month, year):
        match month:
            case 1:
                return 31
            case 2:
                if self.is_leap_year(year):
                    return 29
                else:
                    return 28
            case 3:
                return 31
            case 4:
                return 30
            case 5:
                return 31
            case 6:
                return 30
            case 7:
                return 31
            case 8:
                return 31
            case 9:
                return 30
            case 10:
                return 31
            case 11:
                return 30
            case 12:
                return 31
            case _:
                return -1  # Invalid month

    def get_month_name(self, month):
        match month:
            case 1:
                return "January"
            case 2:
                return "February"
            case 3:
                return "March"
            case 4:
                return "April"
            case 5:
                return "May"
            case 6:
                return "June"
            case 7:
                return "July"
            case 8:
                return "August"
            case 9:
                return "September"
            case 10:
                return "October"
            case 11:
                return "November"
            case 12:
                return "December"
            case _:
                return "Unknown"

    def is_valid_date(self, day, month, year):
        # Check year range
        if year < 2026 or year > 2028:
            print(" [ERROR] Year must be between 2026 and 2028 only!")
            return False

        # Check month range
        if month < 1 or month > 12:
            print(" [ERROR] Month must be between 1 and 12 only!")
            return False

        # Check day range
        max_days = self.get_days_in_month(month, year)
        if day < 1 or day > max_days:
            print(f" [ERROR] Day must be between 1 and {max_days} for {self.get_month_name(month)} {year}!")
            return False

        return True

    def make_date_key(self, day, month, year):
        # Format: YYYY-MM-DD (e.g., 2026-03-05)
        return f"{year}-{month:02d}-{day:02d}"

    def add_event(self, day, month, year, event_name):
        key = self.make_date_key(day, month, year)

        if key in self.events:
            self.events[key].append(event_name)
        else:
            self.events[key] = [event_name]

        print(f"\n[SUCCESS] Event '{event_name}' added on {self.get_month_name(month)} {day}, {year}!")

    def view_events_on_date(self, day, month, year):
        key = self.make_date_key(day, month, year)
        if key in self.events and self.events[key]:
            print(f"\nEvents on {self.get_month_name(month)} {day}, {year}:")
            for i, event in enumerate(self.events[key], 1):
                print(f"  {i}. {event}")
        else:
            print(f"No events found for {self.get_month_name(month)} {day}, {year}.")

    def view_all_events(self):
        if not self.events:
            print("\nNo events in calendar.")
            return

        print("\n--- ALL EVENTS ---")
        for date_key in sorted(self.events.keys()):
            year, month, day = map(int, date_key.split('-'))
            month_name = self.get_month_name(month)
            print(f"{month_name} {day}, {year}:")
            for event in self.events[date_key]:
                print(f"  - {event}")
            print()

    def delete_event(self, day, month, year, event_index):
        key = self.make_date_key(day, month, year)
        if key in self.events and self.events[key]:
            if 1 <= event_index <= len(self.events[key]):
                removed_event = self.events[key].pop(event_index - 1)
                print(f"\n[SUCCESS] Event '{removed_event}' deleted from {self.get_month_name(month)} {day}, {year}!")
                if not self.events[key]:
                    del self.events[key]
            else:
                print("\n[ERROR] Invalid event index!")
        else:
            print(f"\n[ERROR] No events found for {self.get_month_name(month)} {day}, {year}!")


def main():
    calendar = Calendar()

    while True:
        print("\n---- MAIN MENU ----")
        print("1. Add an Event")
        print("2. View Events on a Date")
        print("3. View All Events")
        print("4. Delete an Event")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ")

        if choice == '1':
            print("\n--- ADD AN EVENT ---")
            print("Enter the date:")
            year = int(input("Year (2026-2028): "))
            month = int(input("Month (1-12): "))
            day = int(input("Day: "))

            if calendar.is_valid_date(day, month, year):
                event_name = input("Enter event name: ")
                calendar.add_event(day, month, year, event_name)
            else:
                input("Press Enter to continue...")

        elif choice == '2':
            print("\n--- VIEW EVENTS ON A DATE ---")
            year = int(input("Year (2026-2028): "))
            month = int(input("Month (1-12): "))
            day = int(input("Day: "))

            if calendar.is_valid_date(day, month, year):
                calendar.view_events_on_date(day, month, year)
            input("\nPress Enter to continue...")

        elif choice == '3':
            calendar.view_all_events()
            input("\nPress Enter to continue...")

        elif choice == '4':
            print("\n--- DELETE AN EVENT ---")
            year = int(input("Year (2026-2028): "))
            month = int(input("Month (1-12): "))
            day = int(input("Day: "))

            if calendar.is_valid_date(day, month, year):
                calendar.view_events_on_date(day, month, year)
                if calendar.events.get(calendar.make_date_key(day, month, year)):
                    try:
                        event_index = int(input("Enter event number to delete: "))
                        calendar.delete_event(day, month, year, event_index)
                    except ValueError:
                        print("[ERROR] Invalid input!")
            input("\nPress Enter to continue...")

        elif choice == '5':
            print("Goodbye!")
            break

        else:
            print("[ERROR] Invalid choice!")
            input("Press Enter to continue...")


if __name__ == "__main__":
    main()
