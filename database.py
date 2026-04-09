# ============================================================
#  HT HIRED — Database
#  Handles: Supabase connection + all database functions
# ============================================================

import os
from supabase import create_client
from dotenv import load_dotenv
from models import Student, Supervisor, JobPosting

load_dotenv()

# ---- CONNECTION ----

url = os.getenv("SUPABASE_URL")
key = os.getenv("SUPABASE_KEY")
supabase = create_client(url, key)


# ---- USER FUNCTIONS ----

def get_student_by_email(email):
    result = supabase.table("students_users").select("*").eq("email", email).execute()
    if result.data:
        row = result.data[0]
        return Student(
            id=row["id"],
            first_name=row["first_name"],
            last_name=row["last_name"],
            htstudent_id=row["htstudent_id"],
            classification=row["classification"],
            major=row["major"],
            email=row["email"],
            password=row["password"]
        )
    return None


def get_admin_by_email(email):
    result = supabase.table("admin_users").select("*").eq("email", email).execute()
    if result.data:
        row = result.data[0]
        return Supervisor(
            id=row["id"],
            first_name=row["first_name"],
            last_name=row["last_name"],
            department=row["department"],
            title=row["title"],
            email=row["email"],
            password=row["password"]
        )
    return None


def create_student(first_name, last_name, htstudent_id, classification, major, email, password):
    supabase.table("students_users").insert({
        "first_name": first_name,
        "last_name": last_name,
        "htstudent_id": htstudent_id,
        "classification": classification,
        "major": major,
        "email": email,
        "password": password
    }).execute()


def create_admin(first_name, last_name, department, title, email, password):
    supabase.table("admin_users").insert({
        "first_name": first_name,
        "last_name": last_name,
        "department": department,
        "title": title,
        "email": email,
        "password": password
    }).execute()


# ---- JOB FUNCTIONS ----

def get_all_jobs():
    result = supabase.table("jobs").select("*").execute()
    jobs = []
    for row in result.data:
        jobs.append(JobPosting(
            job_id=row["job_id"],
            job_title=row["job_title"],
            department=row["department"],
            description=row["description"],
            pay_rate=row["pay_rate"],
            admin_id=row["admin_id"],
            created_at=row["created_at"]
        ))
    return jobs


def create_job(job_title, department, description, pay_rate, admin_id):
    supabase.table("jobs").insert({
        "job_title": job_title,
        "department": department,
        "description": description,
        "pay_rate": pay_rate,
        "admin_id": admin_id
    }).execute()


# ---- APPLICATION FUNCTIONS ----

def submit_application(job_id, htstudent_id):
    supabase.table("applications").insert({
        "job_id": job_id,
        "htstudent_id": htstudent_id,
        "status": "Pending"
    }).execute()


def get_applications_by_student(htstudent_id):
    result = supabase.table("applications").select("*, jobs(job_title, department)").eq("htstudent_id", htstudent_id).execute()
    return result.data


def get_applications_by_job(job_id):
    result = supabase.table("applications").select("*, students_users(first_name, last_name, major)").eq("job_id", job_id).execute()
    return result.data


def update_application_status(application_id, status):
    supabase.table("applications").update({"status": status}).eq("application_id", application_id).execute()