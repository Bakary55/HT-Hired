# ============================================================
#  HT HIRED — Iman's Main
#  Entry point: runs the program and routes to the right dashboard
# ============================================================

from auth import sign_up, login
from student_dashboard import student_menu
from admin_dashboard import admin_menu


def main():
    while True:
        print("\n" + "-"*45)
        print("       🐏 WELCOME TO HT HIRED 🐏")
        print("    HT's Campus Job & Work-Study Board")
        print("  Iman and Bakary's Intermediate Python Project")
        print("-"*45)
        print("  [1] Log In")
        print("  [2] Sign Up")
        print("  [3] Exit")
        print("-"*45)

        choice = input("  Enter your choice: ").strip()

        if choice == "1":
            user = login()
            if user:
                if user.role == "student":
                    student_menu(user)
                elif user.role == "admin":
                    admin_menu(user)

        elif choice == "2":
            sign_up()

        elif choice == "3":
            print("\n  Thanks for using HT Hired. Good luck out there! 🐏\n")
            break

        else:
            print("\n  Invalid choice. Please enter 1 - 3.")


if __name__ == "__main__":
    main()