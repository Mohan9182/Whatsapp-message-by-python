import pyautogui as pg
import webbrowser as web

def sendwhatmsg(phone_no, message):
  web.open('https://web.whatsapp.com/send?phone='+phone_no+'&text='+message)
  pg.press('enter')
  
if __name__ == "__main__":
  phone_no = "+91"+input("Enter the Receiver Phone Number:")
  message = input("Enter Message:")
  sendwhatmsg(phone_no,message)
