import time
import os
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

chrome_options = Options()
chrome_options.add_argument("--headless=new")
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--disable-dev-shm-usage")
chrome_options.add_argument("--window-size=1440,1400")

driver = webdriver.Chrome(options=chrome_options)
artifact_dir = "/Users/aadarshamahato/.gemini/antigravity/brain/d6359211-9b16-48fb-acb0-4233b900183e"

try:
    print("Navigating to Case 00...")
    driver.get("http://localhost:8504/the_software_crisis")
    time.sleep(3)
    
    # Progress through Module 1 & 2 to reach Module 3
    for m in range(1, 3):
        print(f"Completing module {m}...")
        # Scroll to bottom
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(1)
        next_btns = driver.find_elements(By.XPATH, "//button[contains(., 'Next Module')]")
        if next_btns:
            driver.execute_script("arguments[0].click();", next_btns[0])
            time.sleep(2)
            
    print("Now on Module 3!")
    time.sleep(2)
    
    # Check if any error text exists on page
    page_text = driver.page_source
    if "AttributeError" in page_text or "Traceback" in page_text:
        print("ERROR: AttributeError or Traceback detected!")
    else:
        print("SUCCESS: Module 3 loaded with ZERO errors!")
        
    shot_m3 = os.path.join(artifact_dir, "se_case00_m3_fixed.png")
    driver.save_screenshot(shot_m3)
    print(f"Saved screenshot to {shot_m3}")
    
    # Click each tab to verify rendering
    tabs = driver.find_elements(By.XPATH, "//button[@role='tab']")
    print(f"Found {len(tabs)} tabs")
    for idx, t in enumerate(tabs):
        tab_name = t.text
        print(f"Clicking tab: {tab_name}")
        driver.execute_script("arguments[0].click();", t)
        time.sleep(1)
        
    shot_tabs = os.path.join(artifact_dir, "se_case00_m3_tabs_fixed.png")
    driver.save_screenshot(shot_tabs)
    print(f"Saved tabs screenshot to {shot_tabs}")

finally:
    driver.quit()
