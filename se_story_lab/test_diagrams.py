import time
import os
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

chrome_options = Options()
chrome_options.add_argument("--headless=new")
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--disable-dev-shm-usage")
chrome_options.add_argument("--window-size=1440,1200")

driver = webdriver.Chrome(options=chrome_options)
artifact_dir = "/Users/aadarshamahato/.gemini/antigravity/brain/d6359211-9b16-48fb-acb0-4233b900183e"

try:
    # Test Case 12: SOLID Foundations
    driver.get("http://localhost:8504/the_solid_foundations")
    time.sleep(4)
    shot_c12 = os.path.join(artifact_dir, "se_case12_solid.png")
    driver.save_screenshot(shot_c12)
    print("Saved Case 12 screenshot")
    
    # Test Case 20: The Divergent Tree (Git)
    driver.get("http://localhost:8504/the_divergent_tree")
    time.sleep(4)
    shot_c20 = os.path.join(artifact_dir, "se_case20_git.png")
    driver.save_screenshot(shot_c20)
    print("Saved Case 20 screenshot")

finally:
    driver.quit()
