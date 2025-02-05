#part A:

"""
Author: Stanley Balakai
Assignment: #1
"""

# part B: 

gym_member = "Alex Alliton" # str
preferred_weight_kg = 20.5  # float
highest_reps = 25           # int
membership_active = True    # bool

# part C:

# (dictionary with string keys and tuples (3 ints) as values)
workout_stats = {

    "Alex": (30, 45, 20),   
    "Sam": (40, 30, 35),
    "Roy": (20, 25, 15),
    "Wei": (35, 40, 10),
    "Jasper": (50, 50, 40),
    "Sherry": (50, 10, 30),
    "Ellen": (25, 15, 35),
}

# part D: 

for friend, activities in list(workout_stats.items()):

    if not friend.endswith("_Total"):
        total_minutes = sum(activities)
        workout_stats[friend + "_Total"] = total_minutes

# part E:


workout_list = []
for friend, activities in workout_stats.items():
    if not friend.endswith("_Total"):
        workout_list.append(list(activities))


# part F:



print("Yoga and Running for all friends:")

for friend_row in workout_list:
    print(friend_row[0:2])  # yoga and running

print("\n Weightlifting for the last two friends in workout_list:")


for friend_row in workout_list[-2:]:
    print(friend_row[2])  # only the weightlifting column

# part G: 


print("\n Checking for friends with total workout minutes >= 120:")

for friend, activities in workout_stats.items():

    if friend.endswith("_Total"):
        friend_name = friend.replace("_Total", "")

        if activities >= 120:
            print(f"Great job staying active, {friend_name}!")

# part H: 


name_input = input("Enter a friend's name to see their workout stats: ")

if name_input in workout_stats and isinstance(workout_stats[name_input], tuple):
    yoga, running, weightlifting = workout_stats[name_input]
    total_for_friend = workout_stats.get(name_input + "_Total", sum((yoga, running, weightlifting)))
    
    print(f"\n{name_input}'s workout minutes:")
    print(f" - Yoga: {yoga}")
    print(f" - Running: {running}")
    print(f" - Weightlifting: {weightlifting}")
    print(f"Total: {total_for_friend} minutes")

else:
    print(f"\nFriend {name_input} not found in the records.")

# part I: 


friend_totals = {k: v for k, v in workout_stats.items() if k.endswith("_Total")}

max_friend_key = max(friend_totals, key=friend_totals.get)
max_minutes = friend_totals[max_friend_key]
max_friend_name = max_friend_key.replace("_Total", "")

min_friend_key = min(friend_totals, key=friend_totals.get)
min_minutes = friend_totals[min_friend_key]
min_friend_name = min_friend_key.replace("_Total", "")

print(f"Friend with the highest total workout minutes: {max_friend_name} ({max_minutes} minutes).")
print(f"Friend with the lowest total workout minutes: {min_friend_name} ({min_minutes} minutes).")