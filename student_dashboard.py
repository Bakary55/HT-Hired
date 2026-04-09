# ============================================================
#  HT HIRED — Student Dashboard
#  Handles: browse jobs, apply, view applications
# ============================================================

from database import get_all_jobs, submit_application, get_applications_by_student

def browse_jobs():
    print("\n" + "-"*45)
    print("           OPEN JOB POSTINGS")
    print("-"*45)

    jobs = get_all_jobs()

    if not jobs:
        print("  No open jobs at this time. Check back later!")
        return

    for job in jobs:
        job.display_info()
        print("  " + "-"*40)

def apply_to_job(student):
    print("\n" + "-"*45)
    print("             APPLY TO A JOB")
    print("-"*45)

    jobs = get_all_jobs()

    if not jobs:
        print("  No open jobs at this time. Check back later!")
        return

    for job in jobs:
        job.display_info()
        print("  " + "-"*40)

    job_id = input("\n  Enter the Job ID you want to apply to: ").strip()

    # check if the job_id they entered actually exists
    valid_ids = [str(job.job_id) for job in jobs]
    if job_id not in valid_ids:
        print("\n  Invalid Job ID. Please try again.")
        return

    submit_application(int(job_id), student.htstudent_id)
    print("\n  Application submitted successfully! Good luck! 🐏")

def view_my_applications(student):
    print("\n" + "-"*45)
    print("          MY APPLICATIONS")
    print("-"*45)

    applications = get_applications_by_student(student.htstudent_id)

    if not applications:
        print("  You haven't applied to any jobs yet!")
        return

    for i, app in enumerate(applications, start=1):
        job_title = app["jobs"]["job_title"]
        department = app["jobs"]["department"]
        status = app["status"]
        applied_at = app["applied_at"][:10]  # trims to just the date

        print(f"\n  [{i}] {job_title} — {department}")
        print(f"      Status   : {status}")
        print(f"      Applied  : {applied_at}")
        print("  " + "-"*40)

def student_menu(student):
    while True:
        print("\n" + "-"*45)
        print("       WELCOME TO HT HIRED, " + student.first_name.upper())
        print("="*45)
        print("  [1] Browse Open Jobs")
        print("  [2] Apply to a Job")
        print("  [3] View My Applications")
        print("  [4] Log Out")
        print("="*45)

        choice = input("  Enter your choice: ").strip()

        if choice == "1":
            browse_jobs()
        elif choice == "2":
            apply_to_job(student)
        elif choice == "3":
            view_my_applications(student)
        elif choice == "4":
            print("\n  Logging out...\n")
            break
        else:
            print("\n  Invalid choice. Please enter 1 - 4.")

    