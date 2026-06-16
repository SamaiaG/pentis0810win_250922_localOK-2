score = 0
level = 1

while True:
    score += 3 if level == 1 else 6  # Increase score based on level
    print(f"You gained {3 if level == 1 else 6} points. Your score is now {score}.")

    if score >= 300 and level < 2:
        level = 2
        print("Congratulations! You've reached Level 2.")
    elif score >= 400 and level < 3:
        level = 3
        print("Congratulations! You've reached Level 3.")
    elif score >= 500 and level < 4:
        level = 4
        print("Congratulations! You've reached Level 4.")
    # Add more level conditions as needed

    # Exit the loop if you've reached the maximum level
    if level == 4:
        print("Congratulations! You've reached the maximum level.")
        break
