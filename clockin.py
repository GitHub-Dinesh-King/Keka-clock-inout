import requests
import datetime
import os

# Function to call Secret_keys
def get_keka_token():
    return os.getenv('KEKA_TOKEN')

def get_telegram_bot_token():
    return os.getenv('TELEGRAM_BOT_TOKEN')

def get_telegram_chat_id():
    return os.getenv('TELEGRAM_CHAT_ID')
    
# Function to send Telegram notification
def send_telegram_notification(message):
    
    telegram_bot_token = get_telegram_bot_token()
    telegram_chat_id = get_telegram_chat_id()
    
    url = f'https://api.telegram.org/bot{telegram_bot_token}/sendMessage'
    payload = {
        'chat_id': telegram_chat_id,
        'text': message
    }

    response = requests.post(url, data=payload)

    if response.status_code == 200:
        print(f"Notification sent: {message}")
    else:
        print(f"Failed to send notification. Status code: {response.status_code}")



def main():
    keka_token = get_keka_token()

    url = "https://maveric.keka.com/k/attendance/api/mytime/attendance/webclockin"
    headers = {
        "Authorization": f"Bearer {keka_token}",
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
