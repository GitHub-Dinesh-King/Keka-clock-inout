import requests
import datetime
import os

# Read token from file -- Old usage
 with open('token.txt', 'r') as f:
    bearer_token = f.read().strip()

# bearer_token = os.getenv("KEKA_TOKEN")

# Set the URL
url = "https://maveric.keka.com/k/attendance/api/mytime/attendance/webclockin"

# Get current UTC time
current_time = datetime.datetime.now(datetime.timezone.utc).isoformat()

# Set headers
headers = {
    "Authorization": f"Bearer {bearer_token}",
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
