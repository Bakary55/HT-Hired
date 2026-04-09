# ============================================================
#  HT HIRED — Admin Dashboard
#  Handles: view postings, post a job, view applicants, 
#           accept/reject applications
# ============================================================

from database import (get_all_jobs, create_job, 
                      get_applications_by_job, update_application_status)


def view_my_postings(admin):
    print("\n" + "-"*45)
    print("           MY JOB POSTINGS")
    print("-"*45)

    jobs = get_all_jobs()
    my_jobs = [job for job in jobs if job.admin_id == admin.id]

    if not my_jobs:
        print("  You haven't posted any jobs yet!")
        return

    for i, job in enumerate(my_jobs, start=1):
        print(f"\n  [{i}] {job.job_title} — {job.department} | {job.pay_rate}")
        print("  " + "-"*40)


def post_a_job(admin):
    print("\n" + "-"*45)
    print("             POST A NEW JOB")
    print("-"*45)

    job_title   = input("  Job Title   : ").strip()
    department  = input("  Department  : ").strip()
    description = input("  Description : ").strip()
    pay_rate    = input("  Pay Rate    : ").strip()

    create_job(job_title, department, description, pay_rate, admin.id)
    print(f"\n  '{job_title}' posted successfully!")


def view_applicants(admin):
    print("\n" + "-"*45)
    print("           VIEW APPLICANTS")
    print("-"*45)

    jobs = get_all_jobs()
    my_jobs = [job for job in jobs if job.admin_id == admin.id]

    if not my_jobs:
        print("  You have no job postings yet!")
        return

    for i, job in enumerate(my_jobs, start=1):
        print(f"  [{i}] {job.job_title} — {job.department}")

    print("="*45)
    choice = input("  Which job would you like to see applicants for? ").strip()

    if not choice.isdigit() or int(choice) < 1 or int(choice) > len(my_jobs):
        print("\n  Invalid choice. Please try again.")
        return

    selected_job = my_jobs[int(choice) - 1]
    applications = get_applications_by_job(selected_job.job_id)

    if not applications:
        print(f"\n  No applicants for {selected_job.job_title} yet!")
        return

    print(f"\n  Applicants for {selected_job.job_title}:")
    print("  " + "-"*40)

    for i, app in enumerate(applications, start=1):
        first_name = app["students_users"]["first_name"]
        last_name  = app["students_users"]["last_name"]
        major      = app["students_users"]["major"]
        status     = app["status"]
        applied_at = app["applied_at"][:10]

        print(f"\n  [{i}] {first_name} {last_name} — {major}")
        print(f"      Status  : {status}")
        print(f"      Applied : {applied_at}")
        print("  " + "-"*40)


def review_applications(admin):
    print("\n" + "-"*45)
    print("         ACCEPT / REJECT APPLICATIONS")
    print("-"*45)

    jobs = get_all_jobs()
    my_jobs = [job for job in jobs if job.admin_id == admin.id]

    if not my_jobs:
        print("  You have no job postings yet!")
        return

    for i, job in enumerate(my_jobs, start=1):
        print(f"  [{i}] {job.job_title} — {job.department}")

    print("-"*45)
    choice = input("  Which job would you like to review? ").strip()

    if not choice.isdigit() or int(choice) < 1 or int(choice) > len(my_jobs):
        print("\n  Invalid choice. Please try again.")
        return

    selected_job = my_jobs[int(choice) - 1]
    applications = get_applications_by_job(selected_job.job_id)

    pending = [app for app in applications if app["status"] == "Pending"]

    if not pending:
        print(f"\n  No pending applications for {selected_job.job_title}!")
        return

    for i, app in enumerate(pending, start=1):
        first_name = app["students_users"]["first_name"]
        last_name  = app["students_users"]["last_name"]
        print(f"  [{i}] {first_name} {last_name}")

    print("="*45)
    app_choice = input("  Which applicant would you like to review? ").strip()

    if not app_choice.isdigit() or int(app_choice) < 1 or int(app_choice) > len(pending):
        print("\n  Invalid choice. Please try again.")
        return

    selected_app = pending[int(app_choice) - 1]

    print("\n  [1] Accept")
    print("  [2] Reject")
    action = input("  Your decision: ").strip()

    if action == "1":
        update_application_status(selected_app["application_id"], "Accepted")
        print("\n  Application accepted!")
    elif action == "2":
        update_application_status(selected_app["application_id"], "Rejected")
        print("\n  Application rejected.")
    else:
        print("\n  Invalid choice.")


def admin_menu(admin):
    while True:
        print("\n" + "-"*45)
        print("       WELCOME TO HT HIRED, " + admin.first_name.upper())
        print("-"*45)
        print("  [1] View My Job Postings")
        print("  [2] Post a New Job")
        print("  [3] View Applicants")
        print("  [4] Accept / Reject Applications")
        print("  [5] Log Out")
        print("-"*45)

        choice = input("  Enter your choice: ").strip()

        if choice == "1":
            view_my_postings(admin)
        elif choice == "2":
            post_a_job(admin)
        elif choice == "3":
            view_applicants(admin)
        elif choice == "4":
            review_applications(admin)
        elif choice == "5":
            print("\n  Logging out. Have a great day!\n")
            break
        else:
            print("\n  Invalid choice. Please enter 1 - 5.")