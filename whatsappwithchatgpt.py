import pywhatkit as pw
import pyautogui as pg
import time

# set up the recipient phone number, message, and time to send
phone_number = "+918985425130"  # replace with recipient's phone number
message = "Hello, this is an automated message sent using Python and Pywhatkit!"
hour = 10  # replace with hour to send message (24-hour format)
minute = 4  # replace with minute to send message

# type and send the message
pw.sendwhatmsg(phone_number, message, hour, minute)

# wait for the WhatsApp window to open
time.sleep(10)

# move the mouse to the send button and click it
pg.moveTo(1050, 680)  # replace with coordinates of the send button on your screen
pg.click()
