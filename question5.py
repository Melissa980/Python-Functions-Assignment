# Question 5 Task 1
def log_activities(activities, durations):
    if len(activities) != len(durations):
        print("Error: Activities and durations lists must have the same length.")
        return None

    log = dict(zip(activities, durations))
    return log

# Question 5 Task 2
def estimate_calories_burned(activity, duration):
    return duration * 3.5

# Question 5 Task 3
def summary(log):
    total_calories = sum(log.values()) * 3.5
    return f"Total calories burned: {total_calories} calories\nActivity Log:\n{log}"

# Example usage of the functions
activities = ['Dancing', 'Swimming', 'Biking']
durations = [10, 20, 15]

log = log_activities(activities, durations)
print(log)

calories_burned = estimate_calories_burned('Swimming', 20)
print(calories_burned)

summary_report = summary(log)
print(summary_report)
