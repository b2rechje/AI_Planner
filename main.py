from database import insert_user, find_users, update_user_schedule
from scheduler import generate_schedule

def main():
    # Sample user data
    user_data = {
        "name": "Jane Doe",
        "focusDuration": 30,
        "stressLevel": "Moderate",
        "preferredStudyTime": "Morning",
        "motivation": "Internal",
        "recurringActivities": ["Yoga", "Gym"],
        "unavailableDays": ["Sunday"],
        "uploadedManual": False
    }

    # Step 1: Insert the user
    insert_user(user_data)

    # Step 2: Generate a schedule
    schedule = generate_schedule(user_data)

    # Step 3: Update the user's schedule in the database
    update_user_schedule("Jane Doe", schedule)

    # Step 4: Retrieve all users and print
    all_users = find_users()
    for user in all_users:
        print(user)

if __name__ == "__main__":
    main()
