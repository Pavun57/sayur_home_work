Orders={
    "GIG 1" : {
        "start" : "07:00",
        "end" : "07:35"
    },
    "GIG 2" : {
        "start" : "07:02",
        "end" : "08:21"
    },
    "GIG 3" : {
        "start" : "08:01",
        "end" : "08:06"
    },
    "GIG 4" : {
        "start" : "08:01",
        "end" : "08:57"
    },
    "GIG 5" : {
        "start" : "08:42",
        "end" : "09:21"
    },
    "GIG 6" : {
        "start" : "16:00",
        "end" : "16:20"
    }
}
employees = {"A","B"}

employee_assignment = {"A": "GIG 1", "B": "GIG 2"}

for i in range(0, len(Orders)):
    current_gig = list(Orders.keys())[i]
    current_start_time = list(Orders.values())[i]["start"].split(":")
    print(current_start_time)
    current_end_time = list(Orders.values())[i]["end"].split(":")

    for employee in employees:
        if employee not in employee_assignment:
            employee_assignment[employee] = current_gig
            break

print(employee_assignment)