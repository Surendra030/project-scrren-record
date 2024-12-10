import os
import subprocess
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from mega import Mega


options = Options()
options.add_argument("--disable-gpu")
options.add_argument("--window-size=1920x1080")
options.add_argument("--headless")  # Headless mode
options.add_argument("--disable-notifications")  # Disable notifications
options.add_argument("--disable-blink-features=AutomationControlled")  # Disable WebDriver flag

# Specify the path to your chromedriver
chromedriver_path = r"chromedriver"
service = Service(executable_path=chromedriver_path)
driver = webdriver.Chrome(service=service, options=options)

try:
    driver.get("https://accounts.google.com/signin")
    time.sleep(2)

    email_input = driver.find_element(By.ID, "identifierId")
    email_input.send_keys("afg154006@gmail.com")
    email_input.send_keys(Keys.RETURN)

    time.sleep(2)

    password_input = driver.find_element(By.NAME, "Passwd")
    password_input.send_keys("passwordtwo")  # Replace with actual password
    password_input.send_keys(Keys.RETURN)
except Exception as e:
    print(e)

time.sleep(5)

driver.get("https://online.arivupro.com/learn/account/signin")
time.sleep(5)

email_input = driver.find_element(By.NAME, "Email*")
email_input.send_keys("afg154006@gmail.com")

pass_input = driver.find_element(By.NAME, "Password*")
pass_input.send_keys("arivuproAac02335!")  # Replace with actual password

time.sleep(2)

pass_input.send_keys(Keys.ENTER)

time.sleep(5)

driver.get("https://online.arivupro.com/learn/home/CA-Intermediate-Online-Video-lecture-classes/CA-Intermediate-Advanced-Accounting-Online-Video-Lecture-Classes-for-free/section/532337/lesson/3310969")

time.sleep(5)

# Step 2: Move the mouse to the position (x=336, y=243)
actions = ActionChains(driver)
actions.move_by_offset(336, 243).perform()
actions.double_click().perform()

time.sleep(2)

# Define download path (use /tmp in GitHub Actions runner for temp files)
download_path = "output_video.mp4"  # Temp path for storing the video

# Define FFmpeg command to record screen with audio (using PulseAudio for virtual audio)
ffmpeg_command = [
    'ffmpeg',
    '-f', 'x11grab',  # Screen capture format
    '-s', '1920x1080',  # Screen resolution
    '-i', ':0.0',  # Input display
    '-f', 'pulse',  # Audio capture format (PulseAudio)
    '-i', 'default',  # Default audio device
    '-vcodec', 'libx264',  # Video codec
    '-acodec', 'aac',  # Audio codec
    '-t', '00:00:10',  # Duration for 12 seconds
    download_path  # Output file path
]

# Start screen recording with FFmpeg
subprocess.Popen(ffmpeg_command)

# Wait for the screen recording to finish (12 seconds)
time.sleep(12)

# Stop the FFmpeg process
subprocess.call(['pkill', 'ffmpeg'])

print("Recording completed..")
time.sleep(20)

# Quit the driver
driver.quit()

try:
    try:
        mega = Mega()
        m = mega.login("afg154006@gmail.com","megaMac02335!")

    except Exception as e:
        print("login failded")
    m.upload(download_path)
except Exception as e:
    print("uploading failed..")
