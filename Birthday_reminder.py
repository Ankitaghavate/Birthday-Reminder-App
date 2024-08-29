from plyer import notification
from datetime import datetime
import pyttsx3

def show_notification(name):
    noti_title=f"Today's {name} Birthday"
    noti_desc=f"Happy Birthday {name}🎂🎉"

    notification.notify(
        title=noti_title,
        message=noti_desc,
        timeout=0
    )
def Text_To_Speech(text):
    engine=pyttsx3.init()
    engine.say(text)
    engine.runAndWait()

if __name__=="__main__":
    birthday_info = {
        "Payel": "2024-02-24",
        "Sai": "2024-08-29",
        "Sanavi": "2024-04-20",
        "Shrisha": "2024-04-20",
        "Ishavari": "2024-08-29",
        "Aaradha": "2024-04-20",
    }
    today_date=datetime.now().strftime("%Y-%m-%d")

    for name,birthday_day in birthday_info.items():
        if today_date==birthday_day:
            show_notification(name)

            Text_To_Speech(f"Today's is {name} Birthday")
        else:
            print(f"No birthdays for {name} today")

