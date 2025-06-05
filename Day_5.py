# Day 5: Cricket Batting Scores Tracker 🏏
def calculate_sum_and_average(scores):
    total = sum(scores)
    average = total / len(scores)
    return total, average

batting_scores = []

print("🏏 Enter your cricket batting scores one by one. Type 'done' to finish:")

while True:
    entry = input("Enter score (or 'done' to finish): ")
    if entry.lower() == 'done':
        break
    try:
        score = int(entry)
        batting_scores.append(score)
    except ValueError:
        print("Please enter a valid number.")
        continue

if len(batting_scores) == 0:
    print("No scores entered.")
else:
    # Apply a bonus using a lambda function (extra 5 runs for each score)
    bonus_runs = lambda x: x + 5
    updated_scores = [bonus_runs(s) for s in batting_scores]

    total, average = calculate_sum_and_average(updated_scores)

    print(f"🏆 Total Runs (with bonus): {total}")
    print(f"📊 Batting Average: {average:.2f}")

    if average >= 50:
        print("💪 Great batting performance! Keep it up! 🎉")
    else:
        print("🏃 Keep practicing to improve your average. 💪")
