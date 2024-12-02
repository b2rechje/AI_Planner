import datetime

def generate_schedule(user):
    """Generate a schedule based on user preferences."""
    schedule = []
    start_time = datetime.datetime.now()

    # Task blocks based on focus duration
    focus_duration = user.get("focusDuration", 25)
    preferred_time = user.get("preferredStudyTime", "Afternoon")

    tasks = ["Task 1", "Task 2", "Task 3"]
    for task in tasks:
        if preferred_time == "Morning":
            task_time = start_time.replace(hour=9, minute=0)
        elif preferred_time == "Evening":
            task_time = start_time.replace(hour=18, minute=0)
        else:
            task_time = start_time.replace(hour=14, minute=0)

        schedule.append({
            "task": task,
            "start": task_time,
            "end": task_time + datetime.timedelta(minutes=focus_duration)
        })
        start_time += datetime.timedelta(minutes=focus_duration + 5)  # Add break time

    return schedule
