import requests
import datetime
import os

def main():
    keka_token = "eyJhbGciOiJSUzI1NiIsImtpZCI6IjFBRjQzNjk5RUE0NDlDNkNCRUU3NDZFMjhDODM5NUIyMEE0MUNFMTgiLCJ4NXQiOiJHdlEybWVwRW5HeS01MGJpaklPVnNncEJ6aGciLCJ0eXAiOiJKV1QifQ.eyJpc3MiOiJodHRwczovL2FwcC5rZWthLmNvbSIsIm5iZiI6MTc3MjE3OTA4NiwiaWF0IjoxNzcyMTc5MDg2LCJleHAiOjE3NzIyNjU0ODYsImF1ZCI6WyJrZWthaHIuYXBpIiwiaGlyby5hcGkiLCJodHRwczovL2FwcC5rZWthLmNvbS9yZXNvdXJjZXMiXSwic2NvcGUiOlsib3BlbmlkIiwia2VrYWhyLmFwaSIsImhpcm8uYXBpIiwib2ZmbGluZV9hY2Nlc3MiXSwiYW1yIjpbImV4dGVybmFsIl0sImNsaWVudF9pZCI6Ijk4N2NjOTcxLWZjMjItNDQ1NC05OWY5LTE2YzA3OGZhN2ZmNiIsInN1YiI6IjE5ZWI2NTg0LWYyOTgtNDk3Yi05MjQyLTE5YTg2ZTVlZWRmMiIsImF1dGhfdGltZSI6MTc3MTY3Nzc2NiwiaWRwIjoiT2ZmaWNlMzY1IiwidGVuYW50X2lkIjoiZTJiMDI0NDMtOTRmNC00ZWY1LWI5YTQtZjJlZGNmMzhlNDFjIiwidGVuYW50aWQiOiJlMmIwMjQ0My05NGY0LTRlZjUtYjlhNC1mMmVkY2YzOGU0MWMiLCJzdWJkb21haW4iOiJtYXZlcmljLmtla2EuY29tIiwidXNlcl9pZCI6IjE5YjQxOTNiLWI2N2EtNDUyYi04NDYzLTM5MTdiYWNmYmM5MyIsInVzZXJfaWRlbnRpZmllciI6IjE5YjQxOTNiLWI2N2EtNDUyYi04NDYzLTM5MTdiYWNmYmM5MyIsInVzZXJuYW1lIjoiZGluZXNockBtYXZlcmljLXN5c3RlbXMuY29tIiwiZW1haWwiOiJkaW5lc2hyQG1hdmVyaWMtc3lzdGVtcy5jb20iLCJhdXRoZW50aWNhdGlvbl90eXBlIjoiMiIsInNpZCI6IkRCRERFREQxMDcwMjQ3NUJBOTU5RTM4RUZFRDgzQjkzIiwianRpIjoiN0JGNDM3MTYzQ0FCRTM1NDE0QzQ0M0UzNDVERjY3MUQifQ.iQqj33sk267AsSUuPiweLs2IGdmRO1nOQ4zd-msuseX2dcaSVgdZ9apK2Rcbv_4l0nDpBoeoKWz2WAEAFxlOa23cdE-oD3Dpi1HVJKV8apTaC-RnjG5W-40ooGXoZW_4EiOq80SOY3F4KE5kQlvvrwnAhMJJ_XBW4SYAEpzjZ_xxMUnWWt4p2FF33zt_QVemSrjRcqG1CQVv_D1v5LgRQENucrNELEyI807-1DpqV7VKNXIjHvr3HkCPc_1isY5M2n71vTPqQQVr-iHoBiq_oUNmIMVtbcIuc1RHrIk-ZaDkzAz78DG_mq0qyrjpVdxmzxS3uN1AZlmVIxW4nQdXuA"

    url = "https://maveric.keka.com/k/attendance/api/mytime/attendance/webclockin"
    headers = {
        "Authorization": f"Bearer {keka_token}",
        "Content-Type": "application/json",
        "Accept": "application/json",
        "User-Agent": "Mozilla/5.0"
    }

    current_time = datetime.datetime.now(datetime.timezone.utc).isoformat()
    payload = {
        "attendanceLogSource": 1,
        "locationAddress": {
            "geoLocationName": None,
            "addressLine1": None,
            "addressLine2": None,
            "countryCode": None,
            "city": None,
            "state": None,
            "stateName": None,
            "zip": None,
            "latitude": None,
            "longitude": None,
            "freeFormAddress": "\r\n\r\n\r\n\r\n\r\n"
        },
        "hasAddress": True,
        "ipAddress": "14.142.158.178",
        "manualClockinType": 1,
        "note": "",
        "originalPunchStatus": 0,
        "timestamp": current_time,
        "premiseId": 0,
        "premiseName": "Web Clock In",
        "pairSubSequentLogs": False,
    }

    response = requests.post(url, headers=headers, json=payload)
    print(f"Clocked Status code: {response.status_code}")
    #print(f"Response Text: Clocked In")

    # Check the response status and send Telegram notification
    if response.status_code == 200:
        print("Clock-in successful!")
        print(response.text)
        print(response.json())

    elif response.status_code == 401:
        print(f"Token Expired - Clock-in failed!")
        print(response.text)
        print(response.json())

    else:
        print(f"Clock-in failed!")
        print(response.status_code)
        print(response.text)
        print(response.json())

if __name__ == "__main__":
    main()
