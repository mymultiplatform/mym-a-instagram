import time
import pyautogui
from tkinter import Tk, Label
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException, WebDriverException
# Function to automate Instagram login and infinite scroll
def automate_instagram():
options = webdriver.ChromeOptions()
options.add_argument('--no-sandbox')
options.add_argument('--disable-dev-shm-usage')
driver = webdriver.Chrome(options=options)
driver.get("https://www.instagram.com")
time.sleep(3)
# Log in to Instagram
username = driver.find_element(By.NAME, "username")
password = driver.find_element(By.NAME, "password")
username.send_keys("mymultiplatform") # Replace with your Instagram username
password.send_keys("deamon") # Replace with your Instagram password
password.send_keys(Keys.RETURN)
time.sleep(5)
# Function to scroll down
def infinite_scroll():
start_time = time.time()
while True:
driver.find_element(By.TAG_NAME, "body").send_keys(Keys.END)
time.sleep(2)
# Stop scrolling after 20 seconds
if time.time() - start_time > 20:
break
infinite_scroll()
# Find the nearest post and comment
def comment_on_post():
try:
# Find the first post
post = driver.find_element(By.XPATH, "//article//a[contains(@href, '/p/')]")
post.click()
time.sleep(3)
# Locate the comment bar
comment_bar = driver.find_element(By.XPATH, "//textarea[@aria-label='Add a
comment...']")
comment_bar.click()
# Simulate typing "Dante" using pyautogui after 7 seconds
time.sleep(7)
pyautogui.typewrite("Dante")
# Click Post
post_button = driver.find_element(By.XPATH, "//button[contains(text(),'Post')]")

post_button.click()
time.sleep(5) # Wait to ensure the comment is posted
# Keep browser open for an additional period to ensure it stays open
time.sleep(60) # Adjust the sleep time as needed to keep the browser open
except NoSuchElementException:
print("Element not found. The script might need updates to match the current Instagram
structure.")
except WebDriverException as e:
print(f"WebDriverException occurred: {e}")
comment_on_post()
# Function to start the automation
def start_automation():
automate_instagram()
# Create a simple Tkinter window
root = Tk()
root.title("MYM-A")
# Add a cool emoji using text
emoji_label = Label(root, text="😊", font=("Helvetica", 48))
emoji_label.pack(pady=10)
# Display a message
label = Label(root, text="Opening Instagram in 10 seconds...", font=("Helvetica", 16))
label.pack(pady=20)
# Schedule Instagram to open after 10 seconds
root.after(10000, start_automation)
# Start the Tkinter main loop
root.mainloop()
