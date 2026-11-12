import time
import os
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

chrome_options = Options()
chrome_options.add_argument("--headless=new")
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--disable-dev-shm-usage")
chrome_options.add_argument("--window-size=1440,1600")

driver = webdriver.Chrome(options=chrome_options)
artifact_dir = "/Users/aadarshamahato/.gemini/antigravity/brain/d6359211-9b16-48fb-acb0-4233b900183e"

try:
    driver.get("http://localhost:8504/the_software_crisis")
    time.sleep(3)
    
    # Unlock module 1 & 2
    for m in range(1, 3):
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(1)
        btn = driver.find_element(By.XPATH, "//button[contains(., 'Unlock Next') or contains(., 'Proceed')]")
        driver.execute_script("arguments[0].click();", btn)
        time.sleep(3)
        
    time.sleep(2)
    
    # Inject Solution
    expander = driver.find_element(By.XPATH, "//*[contains(text(), 'Need help? Click for Hints & Complete Reference Solution')]")
    driver.execute_script("arguments[0].click();", expander)
    time.sleep(2)
    
    inject_btn = driver.find_element(By.XPATH, "//button[contains(., 'Inject Solution into Editor')]")
    driver.execute_script("arguments[0].click();", inject_btn)
    time.sleep(3)
    
    # Run tests
    run_btn2 = driver.find_element(By.XPATH, "//button[contains(., 'Compile & Run Tests')]")
    driver.execute_script("arguments[0].click();", run_btn2)
    time.sleep(3)
    
    # Scroll right below the run button to see the passed card
    driver.execute_script("window.scrollTo(0, 1100);")
    time.sleep(1)
    
    shot_result = os.path.join(artifact_dir, "se_codelab_result_card.png")
    driver.save_screenshot(shot_result)
    print(f"Saved result card screenshot to {shot_result}")

finally:
    driver.quit()
