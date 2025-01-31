"""
Author: Arina Mirzakhani
Assignment: #1
"""

# Variable declarations with data types commented
gym_member = "Alex Alliton"  # str
preferred_weight_kg = 20.5  # float
highest_reps = 25  # int
membership_active = True  # bool

# Dictionary containing workout statistics
# Data type: dict[str, tuple[int, int, int]]
workout_stats = {
    "Alex": (30, 45, 20),
    "Jamie": (25, 50, 15),
    "Taylor": (40, 35, 25)
}

# Adding total workout minutes to the dictionary
# Iterate over a copy of the dictionary's items to avoid modifying it during iteration
for friend, activities in list(workout_stats.items()):
    total_minutes = sum(activities)
    workout_stats[f"{friend}_Total"] = total_minutes

# Creating a 2D list (nested list) from workout minutes
# Data type: list[list[int]]
workout_list = [list(activities) for friend, activities in workout_stats.items() if isinstance(activities, tuple)]

# Slicing the workout list
# Yoga and running for all friends
yoga_running_minutes = [row[:2] for row in workout_list]
print("Yoga and Running Minutes for all friends:", yoga_running_minutes)

# Weightlifting for the last two friends
weightlifting_last_two = [row[2] for row in workout_list[-2:]]
print("Weightlifting Minutes for the last two friends:", weightlifting_last_two)

# Check if any friend's total workout minutes >= 120
print("\nFriends with great activity levels:")
for friend, total in workout_stats.items():
    if isinstance(total, int) and total >= 120:
        friend_name = friend.replace("_Total", "")
        print(f" - Great job staying active, {friend_name}!")

# Allow user input to query a friend's workout stats
while True:
    friend_name_input = input("\nEnter a friend's name to view their workout stats (or 'exit' to quit): ").strip()
    if friend_name_input.lower() == 'exit':
        print("Goodbye!")
        break

    # Normalize input and dictionary keys for case-insensitive comparison
    normalized_stats = {k.lower(): (v if "_total" not in k.lower() else None) for k, v in workout_stats.items()}
    normalized_totals = {k.lower(): v for k, v in workout_stats.items() if "_total" in k.lower()}

    if friend_name_input.lower() in normalized_stats:
        friend_key = friend_name_input.capitalize()
        stats = workout_stats.get(friend_key)
        total = workout_stats.get(f"{friend_key}_Total", sum(stats))
        if stats:
            yoga, running, weightlifting = stats
            print(f"\n{friend_key}'s Workout Stats:")
            print(f" - Yoga: {yoga} minutes")
            print(f" - Running: {running} minutes")
            print(f" - Weightlifting: {weightlifting} minutes")
            print(f" - Total Workout Minutes: {total}")
    else:
        print(f"\nFriend '{friend_name_input}' not found in the records. Please check the name and try again.")

# Find the friend with the highest and lowest workout minutes
total_minutes_only = {friend: total for friend, total in workout_stats.items() if isinstance(total, int)}
highest_friend_key = max(total_minutes_only, key=total_minutes_only.get)
highest_friend = highest_friend_key.replace("_Total", "")
lowest_friend_key = min(total_minutes_only, key=total_minutes_only.get)
lowest_friend = lowest_friend_key.replace("_Total", "")

print(f"\nFriend with the highest total workout minutes: {highest_friend} ({total_minutes_only[highest_friend_key]} minutes)")
print(f"Friend with the lowest total workout minutes: {lowest_friend} ({total_minutes_only[lowest_friend_key]} minutes)")

