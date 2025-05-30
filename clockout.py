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

def get_telegram_username():
    return os.getenv('TELEGRAM_USERNAME')
    
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

def make_phone_call():
    username = get_telegram_username()
    cc = "Keka+Token+Expired" #Telegram Message if call is Missed or Rejected   
    call_url = (
        f"http://api.callmebot.com/start.php?"
        f"user={username}&text=Hi+Boss+the+Keka+Token+is+Expired&lang=en-US-Standard-A&rpt=1&cc={cc}&timeout=30"
    )
    
    response = requests.get(call_url)
    print(f"Calling URL:", call_url)
    print(f"Telegram Call Response:", response.text)
    try:
        print(f"Telegram Call Response:", response.status_code)
    except Exception as e:
        print(f"Unable to get the Status code of Telegram Call Response")
        

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
        "originalPunchStatus": 1
    }

    response = requests.post(url, headers=headers, json=payload)
    print(f"Clocked Status code: {response.status_code}")
    #print(f"Response Text: Clocked In")
    
    # Check the response status and send Telegram notification
    if response.status_code == 200:
        print("Clock-out successful!")
        send_telegram_notification('✅ Clock-out successful!')  # Send success notification
    elif response.status_code == 401:
        print(f"Token Expired - Clock-out failed!")
        send_telegram_notification('🔒 Keka Token Expired!')  # Send keka token expired notification
        make_phone_call()
    else:
        print(f"Clock-out failed!")
        send_telegram_notification('❌ Clock-out failed!')  # Send failure notification



if __name__ == "__main__":
    main()
