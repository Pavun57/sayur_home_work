from datetime import datetime

def match_orders_to_employees(orders, employees):
    # Sort orders by start time
    sorted_orders = sorted(orders.items(), key=lambda x: x[1]['start'])

    # Initialize data structures
    employee_to_orders = {employee: [] for employee in employees}
    employee_earnings = {employee: 0 for employee in employees}
    total_company_earnings = 0

    # Assign orders to employees
    for order, details in sorted_orders:
        start_time = datetime.strptime(details['start'], '%H:%M')
        end_time = datetime.strptime(details['end'], '%H:%M')

        for employee in employees:
            if not employee_to_orders[employee] or datetime.strptime(employee_to_orders[employee][-1][1]['end'], '%H:%M') <= start_time:
                # Assign the order to the employee
                employee_to_orders[employee].append((order, details))
                # Calculate earnings for this order
                duration_minutes = (end_time - start_time).seconds // 60
                earnings = duration_minutes * 50
                employee_earnings[employee] += earnings
                total_company_earnings += earnings
                break

    # Print results
    for employee in employees:
        print(f"{employee} worked on {', '.join([order for order, _ in employee_to_orders[employee]])}")

    print("\nEmployee Earnings:")
    for employee, earnings in employee_earnings.items():
        print(f"{employee}: Rs. {earnings}")

    print(f"\nTotal Company Earnings: Rs. {total_company_earnings}")

# Sample input
orders = {
    "GIG 1": {
        "start": "07:00",
        "end": "07:35"
    },
    "GIG 2": {
        "start": "07:02",
        "end": "08:21"
    },
    "GIG 3": {
        "start": "08:01",
        "end": "08:06"
    },
    "GIG 4": {
        "start": "08:01",
        "end": "08:57"
    },
    "GIG 5": {
        "start": "08:42",
        "end": "09:21"
    },
    "GIG 6": {
        "start": "16:00",
        "end": "16:20"
    }
}
employees = ["A", "B"]

# Call the function
match_orders_to_employees(orders, employees)
