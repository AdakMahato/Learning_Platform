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
    
    # Click Module 1 complete button
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(1)
    btn1 = driver.find_element(By.XPATH, "//button[contains(., 'Unlock Next') or contains(., 'Proceed')]")
    print("Found button 1:", btn1.text)
    driver.execute_script("arguments[0].click();", btn1)
    time.sleep(3)
    
    # Click Module 2 complete button
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(1)
    btn2 = driver.find_element(By.XPATH, "//button[contains(., 'Unlock Next') or contains(., 'Proceed')]")
    print("Found button 2:", btn2.text)
    driver.execute_script("arguments[0].click();", btn2)
    time.sleep(3)
    
    print("Arrived at Module 3!")
    time.sleep(2)
    
    # Check page source for error
    page_text = driver.page_source
    assert "AttributeError" not in page_text, "Found AttributeError on page!"
    assert "Traceback" not in page_text, "Found Traceback on page!"
    print("SUCCESS: Zero errors on Module 3!")
    
    shot_m3 = os.path.join(artifact_dir, "se_case00_m3_fixed_verified.png")
    driver.save_screenshot(shot_m3)
    print(f"Saved verified screenshot to {shot_m3}")
    
    # Check tabs
    tab_labels = [el.text for el in driver.find_elements(By.XPATH, "//*[contains(@data-baseweb, 'tab')]")]
    print("Found tab elements:", tab_labels)

finally:
    driver.quit()
