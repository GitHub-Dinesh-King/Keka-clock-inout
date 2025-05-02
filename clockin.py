import requests
import datetime
import os
import json

# Read token from file -- Old usage
#with open("token.txt", "r") as f:
#   bearer_token = f.read().strip()

# bearer_token = os.getenv("KEKA_TOKEN")

# Set the URL
url = "https://maveric.keka.com/k/attendance/api/mytime/attendance/webclockin"

# Get current UTC time
current_time = datetime.datetime.now(datetime.timezone.utc).isoformat()

# Set headers
headers = {
    "Authorization": f"Bearer eyJhbGciOiJSUzI1NiIsImtpZCI6IjFBRjQzNjk5RUE0NDlDNkNCRUU3NDZFMjhDODM5NUIyMEE0MUNFMTgiLCJ4NXQiOiJHdlEybWVwRW5HeS01MGJpaklPVnNncEJ6aGciLCJ0eXAiOiJKV1QifQ.eyJpc3MiOiJodHRwczovL2FwcC5rZWthLmNvbSIsIm5iZiI6MTc0NjE4NjM2MywiaWF0IjoxNzQ2MTg2MzYzLCJleHAiOjE3NDYyNzI3NjMsImF1ZCI6WyJrZWthaHIuYXBpIiwiaGlyby5hcGkiLCJodHRwczovL2FwcC5rZWthLmNvbS9yZXNvdXJjZXMiXSwic2NvcGUiOlsib3BlbmlkIiwia2VrYWhyLmFwaSIsImhpcm8uYXBpIiwib2ZmbGluZV9hY2Nlc3MiXSwiYW1yIjpbImV4dGVybmFsIl0sImNsaWVudF9pZCI6Ijk4N2NjOTcxLWZjMjItNDQ1NC05OWY5LTE2YzA3OGZhN2ZmNiIsInN1YiI6IjE5ZWI2NTg0LWYyOTgtNDk3Yi05MjQyLTE5YTg2ZTVlZWRmMiIsImF1dGhfdGltZSI6MTc0NjEwMTgyOSwiaWRwIjoiT2ZmaWNlMzY1IiwidGVuYW50X2lkIjoiZTJiMDI0NDMtOTRmNC00ZWY1LWI5YTQtZjJlZGNmMzhlNDFjIiwidGVuYW50aWQiOiJlMmIwMjQ0My05NGY0LTRlZjUtYjlhNC1mMmVkY2YzOGU0MWMiLCJzdWJkb21haW4iOiJtYXZlcmljLmtla2EuY29tIiwidXNlcl9pZCI6IjE5YjQxOTNiLWI2N2EtNDUyYi04NDYzLTM5MTdiYWNmYmM5MyIsInVzZXJfaWRlbnRpZmllciI6IjE5YjQxOTNiLWI2N2EtNDUyYi04NDYzLTM5MTdiYWNmYmM5MyIsInVzZXJuYW1lIjoiZGluZXNockBtYXZlcmljLXN5c3RlbXMuY29tIiwiZW1haWwiOiJkaW5lc2hyQG1hdmVyaWMtc3lzdGVtcy5jb20iLCJhdXRoZW50aWNhdGlvbl90eXBlIjoiMiIsInNpZCI6IjZFRTgyRDVFM0U1NTFCMzUwMjIwOTk3RjhDOTZDOEY0IiwianRpIjoiQTc5RDUzREFBNzNBODI2QkU0NjJBRDc0NjM0RDY5OTMifQ.Q3bXInF7E84wslpgRw7rXiYhxovaSycMQkoqUmHRWG2DzTgS1nnEVfvGxQBUG6zSoTByukUNlcw3DUBC-PiB9oNODK74vPqXV3j8x7wmQfymysBX7BlFdoIXyVYuby-pnZwX_9juIReeXLX5vGejxm5vrBHoh8ihoq-YUI0edK65OyvQw1BcvXSjSxiPWWUX3A9DNG8-MUmjF5Gh4YWFDpVxlQbJHpxo0oJxWTW1Z0sweUUMqMmVmWaNpiYdN5Pc26S5MOqrjHlGJyaGumq63YoR46kg_hLMLWYdAFpHz25vj7R_F0Vc0j6SZlJtC3WglJshE-ogRB8lNqQSRiMfSw",
    "Content-Type": "application/json",
    "Accept": "application/json",
    "User-Agent": "Mozilla/5.0"
}

# Set payload
payload = {
    "timestamp": current_time,
    "attendanceLogSource": 1,
    "locationAddress": None,
    "manualClockinType": 1,
    "note": "",
    "originalPunchStatus": 0
}

# Send the POST request
response = requests.post(url, headers=headers, json=payload)

# Print the response
print("Status Code:", response.status_code)
print("Clocked in")
# print("Response Text:", response.text)
