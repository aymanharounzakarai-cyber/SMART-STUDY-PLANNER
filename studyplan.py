import json
sessions = []
# Question (b): Add a study session
def add_session():
    print("\n===== SELECT SUBJECT =====")
    print("1. Python Programming")
    print("2. Database Systems")
    print("3. Web Development")
    print("4. Computer Networks")
    print("5. Mathematics")
    subject_choice = input("Choose a subject (1-5): ")
    if subject_choice == "1":
        subject = "Python Programming"
    elif subject_choice == "2":
        subject = "Database Systems"
    elif subject_choice == "3":
        subject = "Web Development"
    elif subject_choice == "4":
        subject = "Computer Networks"
    elif subject_choice == "5":
        subject = "Mathematics"
    else:
        print("Invalid subject choice.")
        return
    topic = input("Enter topic covered: ")
    date = input("Enter date or day: ")
    while True:
        try:
            duration = float(input("Enter duration in minutes: "))
            if duration > 0:
                break
            else:
                print("Duration must be a positive number.")
        except ValueError:
            print("Please enter a valid number.")
    session = {
        "subject": subject,
        "topic": topic,
        "date": date,
        "duration": duration
    }
    sessions.append(session)
    print("Study session added successfully.")
# Question (c): Classify the study session
def classify_session(duration):
    if duration < 30:
        return "Short"
    elif duration <= 90:
        return "Medium"
    else:
        return "Long"
# Question (d): View all study sessions
def view_sessions():
    if len(sessions) == 0:
        print("\nNo study sessions recorded.")
        return
    print("\n==================== ALL STUDY SESSIONS ====================")
    print(f"{'Subject':<22}{'Topic':<25}{'Duration':<12}{'Class'}")
    print("-" * 70)
    for session in sessions:
        classification = classify_session(session["duration"])
        print(
            f"{session['subject']:<22}"
            f"{session['topic']:<25}"
            f"{session['duration']:<12.1f}"
            f"{classification}"
        )
# Question (e): Search sessions by subject
def search_by_subject(subject):
    found_sessions = []
    total_time = 0
    for session in sessions:
        if session["subject"].lower() == subject.lower():
            found_sessions.append(session)
            total_time += session["duration"]
    if len(found_sessions) == 0:
        print("\nNo sessions found for that subject.")
        return
    print("\n==================== SEARCH RESULTS ====================")
    print(f"{'Subject':<22}{'Topic':<25}{'Duration':<12}{'Class'}")
    print("-" * 70)
    for session in found_sessions:
        classification = classify_session(session["duration"])
        print(
            f"{session['subject']:<22}"
            f"{session['topic']:<25}"
            f"{session['duration']:<12.1f}"
            f"{classification}"
        )
    print("-" * 70)
    print(f"Total time spent on {subject}: {total_time:.1f} minutes")
# Question (f): Study statistics
def study_statistics():
    if len(sessions) == 0:
        print("\nNo study sessions recorded.")
        return
    total_minutes = 0
    subject_totals = {}
    for session in sessions:
        duration = session["duration"]
        subject = session["subject"]
        total_minutes += duration
        if subject in subject_totals:
            subject_totals[subject] += duration
        else:
            subject_totals[subject] = duration
    total_hours = total_minutes / 60
    print("\n==================== STUDY STATISTICS ====================")
    print(f"Total hours studied overall: {total_hours:.2f} hours")
    print("\nTotal hours studied per subject:")
    for subject, minutes in subject_totals.items():
        hours = minutes / 60
        print(f"{subject}: {hours:.2f} hours")
    weakest_subject = min(subject_totals, key=subject_totals.get)
    longest_session = max(
        sessions,
        key=lambda session: session["duration"]
    )
    print(f"\nSubject with the least study time: {weakest_subject}")
    print(
        f"Longest study session: "
        f"{longest_session['subject']} - "
        f"{longest_session['topic']} "
        f"({longest_session['duration']:.1f} minutes)"
    )
# Question (g): Save sessions to file
def save_sessions():
    with open("study_log.txt", "w") as file:
        json.dump(sessions, file, indent=4)
    print("Study sessions saved successfully.")
# Question (g): Load sessions from file
def load_sessions():
    global sessions
    try:
        with open("study_log.txt", "r") as file:
            sessions = json.load(file)
    except FileNotFoundError:
        sessions = []
# Question (a): Main menu
def main():
    load_sessions()
    while True:
        print("\n===== SMART STUDY PLANNER =====")
        print("1. Add a study session")
        print("2. View all sessions")
        print("3. Search sessions by subject")
        print("4. View statistics")
        print("5. Save and exit")
        choice = input("Enter your choice: ")
        if choice == "1":
            add_session()
        elif choice == "2":
            view_sessions()
        elif choice == "3":
            print("\n===== SEARCH SUBJECT =====")
            print("1. Python Programming")
            print("2. Database Systems")
            print("3. Web Development")
            print("4. Computer Networks")
            print("5. Mathematics")
            subject_choice = input("Choose a subject (1-5): ")
            if subject_choice == "1":
                search_by_subject("Python Programming")
            elif subject_choice == "2":
                search_by_subject("Database Systems")
            elif subject_choice == "3":
                search_by_subject("Web Development")
            elif subject_choice == "4":
                search_by_subject("Computer Networks")
            elif subject_choice == "5":
                search_by_subject("Mathematics")
            else:
                print("Invalid subject choice.")
        elif choice == "4":
            study_statistics()
        elif choice == "5":
            save_sessions()
            print("Thank you for using Smart Study Planner.")
            break
        else:
            print("Invalid choice. Please enter a number from 1 to 5.")
if __name__ == "__main__":
    main()