import pywhatkit
import time
import pyautogui
from datetime import datetime, timedelta


def send_message_fully_automated(phone_number, message):
    """
    Send a WhatsApp message with full automation - no manual intervention required

    Args:
        phone_number (str): Phone number with country code
        message (str): Message to be sent
    """
    try:
        # Make sure the phone number has the correct format with + symbol
        if not phone_number.startswith('+'):
            phone_number = '+' + phone_number

        print(f"Opening WhatsApp Web for {phone_number}...")

        # Open WhatsApp Web with the phone number
        pywhatkit.sendwhatmsg_instantly(
            phone_no=phone_number,
            message=message,
            wait_time=20,  # Wait 20 seconds for WhatsApp to load
            tab_close=False
        )

        # Wait for WhatsApp Web to load completely
        time.sleep(20)

        # Press ENTER to send the message - this is automated, not manual
        pyautogui.press('enter')

        print("Message sent successfully!")

        # Wait a bit and then close the tab
        time.sleep(5)
        pyautogui.hotkey('ctrl', 'w')  # Close the current tab

        return True
    except Exception as e:
        print(f"Error: {str(e)}")
        return False


def schedule_and_wait(phone_number, message, target_hour, target_minute):
    """
    Schedule a message to be sent at specific time and wait until then

    Args:
        phone_number (str): Phone number with country code
        message (str): Message to be sent
        target_hour (int): Hour in 24-hour format
        target_minute (int): Minute
    """
    now = datetime.now()
    target_time = now.replace(hour=target_hour, minute=target_minute, second=0, microsecond=0)

    # If target time is in the past, schedule for tomorrow
    if now > target_time:
        target_time = target_time + timedelta(days=1)

    wait_seconds = (target_time - now).total_seconds()

    print(f"Current time: {now.strftime('%Y-%m-%d %H:%M:%S')}")
    print(f"Target time: {target_time.strftime('%Y-%m-%d %H:%M:%S')}")
    print(f"The program will wait for {wait_seconds:.0f} seconds until {target_time.strftime('%H:%M:%S')}")
    print("You can leave this program running. DO NOT close the terminal or put your computer to sleep.")
    print("The message will be sent automatically at the scheduled time.")

    # Wait until the scheduled time
    time.sleep(wait_seconds)

    # Send the message
    return send_message_fully_automated(phone_number, message)


if __name__ == "__main__":
    # Phone number with country code
    phone_number = "905061059913"  # Replace with the recipient's number if needed
    message = "Hey! This is an automated message sent at the scheduled time."

    print("FULLY AUTOMATED WhatsApp Message Sender")
    print("======================================")
    print("1. Send message at 12:01 AM tonight")
    print("2. Send message at custom time")
    print("3. Test send message right now (for testing)")

    choice = input("Enter your choice (1/2/3): ")

    if choice == "1":
        # Schedule for 12:01 AM
        schedule_and_wait(phone_number, message, 0, 1)
    elif choice == "2":
        # Custom time
        print("\nEnter the time you want to send the message:")
        hour = int(input("Hour (0-23): "))
        minute = int(input("Minute (0-59): "))
        schedule_and_wait(phone_number, message, hour, minute)
    elif choice == "3":
        # Send immediately for testing
        print("\nTesting immediate send...")
        send_message_fully_automated(phone_number, message)
    else:
        print("Invalid choice.")