# ============================================================
# HT HIRED — Classes
# User, Student, Supervisor, JobPosting classes
# ============================================================


class User:
    def __init__(self, id, first_name, last_name, email, password, role):
        self.id = id
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.password = password
        self.role = role

    def display_info(self):
        print(f"  Name  : {self.first_name} {self.last_name}")
        print(f"  Email : {self.email}")
        print(f"  Role  : {self.role}")


class Student(User):
    def __init__(self, id, first_name, last_name, htstudent_id, classification, major, email, password):
        super().__init__(id, first_name, last_name, email, password, role="student")
        self.htstudent_id = htstudent_id
        self.classification = classification
        self.major = major

    def display_info(self):
        super().display_info()
        print(f"  Student ID     : {self.htstudent_id}")
        print(f"  Classification : {self.classification}")
        print(f"  Major          : {self.major}")


class Supervisor(User):
    def __init__(self, id, first_name, last_name, department, title, email, password):
        super().__init__(id, first_name, last_name, email, password, role="admin")
        self.department = department
        self.title = title

    def display_info(self):
        super().display_info()
        print(f"  Department : {self.department}")
        print(f"  Title.     : {self.title}")


class JobPosting:
    def __init__(self, job_id, job_title, department, description, pay_rate, admin_id, created_at=None):
        self.job_id = job_id
        self.job_title = job_title
        self.department = department
        self.description = description
        self.pay_rate = pay_rate
        self.admin_id = admin_id
        self.created_at = created_at

    def display_info(self):
        print(f"\n  Job Title  : {self.job_title}")
        print(f"  Department : {self.department}")
        print(f"  Pay Rate   : {self.pay_rate}")
        print(f"  Description: {self.description}")