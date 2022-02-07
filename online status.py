statuses = {
    "Alice": "online",
    "Bob": "offline",
    "Eve": "online",
}

def online_count(x):
    online_person = 0
    new_dict = x.values()
    for i in new_dict:
        if i == "online":
            online_person += 1
    return online_person

print(online_count(statuses)) 