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
employees = ["A", "B"]
e1={}
key=list(Orders.keys())
for i in range(len(key) and len(employees)):
        e1[employees[i]]=key[i],Orders[key[i]]
for key,value in e1.items():
    print(f"Key: {key}, Value: {value}")