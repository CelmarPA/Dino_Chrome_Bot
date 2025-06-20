# Import required libraries
import cv2
import numpy as np
from PIL import ImageGrab
import pyautogui
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

# Selenium browser configuration
options = Options()
options.add_argument("--start-maximized")   # Start the browser maximized

# Initialize the Chrome browser using WebDriver Manager
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

game_url = "https://chromedino.com/"
driver.get(game_url)

driver.implicitly_wait(2.0) # wait for the pago to load

# Locate the dinosaur on the screen
print("Looking for the dinosaur...")

dino_template = cv2.imread("dino_temp/dino.png", cv2.IMREAD_UNCHANGED)

if dino_template is None:
    print("Dinosaur image not found. Check the path!")
    driver.quit()
    exit()

template_gray = cv2.cvtColor(dino_template, cv2.COLOR_BGR2GRAY)
w, h = template_gray.shape[::-1]

# Capture the entire screen
screen = np.array(ImageGrab.grab())
screen_gray = cv2.cvtColor(screen, cv2.COLOR_BGR2GRAY)

# Search for the template
result = cv2.matchTemplate(screen_gray, template_gray, cv2.TM_CCOEFF_NORMED)
_, max_val, _, max_loc = cv2.minMaxLoc(result)

if max_val >= 0.7:
    dino_x, dino_y = max_loc
    print(f"Dinosaur found at coordinates: {dino_x}, {dino_y}")
else:
    print("Dinosaur not found. Adjust your template image!")
    driver.quit()
    exit()

# Initialize variables
speed = 0

print("🚀 Starting the bot... Press Ctrl+C to stop.")

try:
    while True:
        # Define the detection region based on the dino
        box_x = dino_x + 60 + int(speed * 1.0)  # Adjust with speed
        box_y = dino_y - 5                      # Climb up a little to catch birds
        box_width = 40
        box_height = 30

        current_box = (box_x, box_y, box_width, box_height)

        # Capture the region
        screenshot = pyautogui.screenshot(region = current_box)
        pixels = screenshot.load()
        width, height = screenshot.size

        # Flag for detection
        obstacle_detected = False

        for x in range(width):
            for y in range(height):
                r, g, b = pixels[x, y]

                if r < 90 and g < 90  and b < 90:    # Dark pixel (obstacle) detection
                    print(f"Obstacle detected at ({x}, {y})")

                    # Make the dinosaur jump
                    pyautogui.keyDown("space")
                    time.sleep(max(0.20, 0.3 - speed * 0.005))  # Jump's delay adjusted by speed
                    pyautogui.keyUp("space")

                    # Change the flag
                    obstacle_detected = True
                    speed += 1  # Simulates speed increase over time
                    break

            if obstacle_detected:
                break

        # Small sleep to relieve CPU
        time.sleep(0.01)

except KeyboardInterrupt:
    print("Bot terminated by user.")
    driver.quit()