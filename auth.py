# ============================================================
#  HT HIRED — Sign up and login for students and admins
# ============================================================

from database import (get_student_by_email, get_admin_by_email,
                      create_student, create_admin)


# ---- SIGN UP ----

def sign_up():
    print("\n" + "="*45)
    print("              CREATE AN ACCOUNT")
    print("="*45)
    print("  [1] I am a Student")
    print("  [2] I am an Admin")
    print("="*45)

    role = input("  Enter your role: ").strip()

    first_name = input("  First Name     : ").strip()
    last_name  = input("  Last Name      : ").strip()
    email      = input("  Email          : ").strip()
    password   = input("  Password       : ").strip()

    if role == "1":
        htstudent_id   = input("  HT Student ID  : ").strip()
        classification = input("  Classification : ").strip()
        major          = input("  Major          : ").strip()
        create_student(first_name, last_name, htstudent_id, classification, major, email, password)
        print("\n  Account created! You can now log in.")

    elif role == "2":
        department = input("  Department     : ").strip()
        title      = input("  Title          : ").strip()
        create_admin(first_name, last_name, department, title, email, password)
        print("\n  Account created! You can now log in.")

    else:
        print("\n  Invalid choice. Please try again.")


# ---- LOGIN ----

def login():
    print("\n" + "="*45)
    print("                  LOG IN")
    print("="*45)

    email    = input("  Email    : ").strip()
    password = input("  Password : ").strip()

    # check students first, then admins
    user = get_student_by_email(email) or get_admin_by_email(email)

    if user and user.password == password:
        print(f"\n  Welcome back, {user.first_name}!")
        return user
    else:
        print("\n  Invalid email or password. Please try again.")
        return None