import requests
import datetime
import os

# Function to send Telegram notification
def send_telegram_notification(message):
    bot_token = '7617784862:AAEFIF4eqIWcySITc_DPLNjvcUmll01A_is'  # Telegram bot token
    chat_id = '1332307993'
    url = f'https://api.telegram.org/bot{bot_token}/sendMessage'
    payload = {
        'chat_id': chat_id,
        'text': message
    }

    response = requests.post(url, data=payload)

    if response.status_code == 200:
        print(f"Notification sent: {message}")
    else:
        print(f"Failed to send notification. Status code: {response.status_code}")



def main():
    token = os.getenv("KEKA_TOKEN")

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
    print(f"Clocked Status code: {response.status_code}")
    #print(f"Response Text: Clocked In")
    
    # Check the response status and send Telegram notification
    if response.status_code == 200:
        print("Clock-in successful!")
        send_telegram_notification(':white_check_mark: Clock-in successful!')  # Send success notification
    else:
        print(f"Clock-in failed!")
        send_telegram_notification(':x: Clock-in failed!')  # Send failure notification



if __name__ == "__main__":
    main()
