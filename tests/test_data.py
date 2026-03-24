import requests

BASE_URL = "http://127.0.0.1:8000/api"

# Create applicant
applicant = requests.post(f"{BASE_URL}/applicants", json={
    "phone_number": "1111111111",
    "cv_url": "https://example.com/cv.pdf",
    "experience_summary": "Test applicant"
})

print("Applicant:", applicant.json())

# Create job
job = requests.post(f"{BASE_URL}/jobs", json={
    "title": "Backend Dev",
    "description": "Build APIs"
})

print("Job:", job.json())

# Apply to job
application = requests.post(f"{BASE_URL}/applications", json={
    "job_id": job.json()["id"],
    "applicant_id": applicant.json()["id"]
})

print("Application:", application.json())