import requests
import datetime

def get_token():
    with open('token.txt', 'r') as f:
        return f.read().strip()

def main():
    token = get_token()

    url = "https://maveric.keka.com/k/attendance/api/mytime/attendance/webclockin"
    headers = {
        "Authorization": f"Bearer {token}",
        "Content-Type": "application/json",
        "Accept": "application/json",
        "User-Agent": "Mozilla/5.0"
    }

    current_time = datetime.datetime.now(datetime.timezone.utc).isoformat()
    payload = {
        "timestamp": current_time,
        "attendanceLogSource": 1,
        "locationAddress": None,
        "manualClockinType": 1,
        "note": "",
        "originalPunchStatus": 0
    }

    response = requests.post(url, headers=headers, json=payload)
    print(f"Status code: {response.status_code}")
    print(f"Response Text: Clocked In")

if __name__ == "__main__":
    main()
