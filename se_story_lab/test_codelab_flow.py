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
    
    # Unlock module 1 & 2
    for m in range(1, 3):
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(1)
        btn = driver.find_element(By.XPATH, "//button[contains(., 'Unlock Next') or contains(., 'Proceed')]")
        driver.execute_script("arguments[0].click();", btn)
        time.sleep(3)
        
    print("On Module 3!")
    time.sleep(2)
    
    # 1. Click "Compile & Run Tests" on incomplete starter code
    run_btn = driver.find_element(By.XPATH, "//button[contains(., 'Compile & Run Tests')]")
    driver.execute_script("arguments[0].click();", run_btn)
    time.sleep(3)
    
    shot_fail = os.path.join(artifact_dir, "se_codelab_starter_assertion_fail.png")
    driver.save_screenshot(shot_fail)
    print(f"Saved starter fail screenshot to {shot_fail}")
    
    # 2. Open Expander and click "Inject Solution into Editor ⬇"
    expander = driver.find_element(By.XPATH, "//*[contains(text(), 'Need help? Click for Hints & Complete Reference Solution')]")
    driver.execute_script("arguments[0].click();", expander)
    time.sleep(2)
    
    inject_btn = driver.find_element(By.XPATH, "//button[contains(., 'Inject Solution into Editor')]")
    driver.execute_script("arguments[0].click();", inject_btn)
    time.sleep(3)
    
    # 3. Click "Compile & Run Tests" on the injected solution
    run_btn2 = driver.find_element(By.XPATH, "//button[contains(., 'Compile & Run Tests')]")
    driver.execute_script("arguments[0].click();", run_btn2)
    time.sleep(4)
    
    shot_pass = os.path.join(artifact_dir, "se_codelab_solution_passed.png")
    driver.save_screenshot(shot_pass)
    print(f"Saved solution pass screenshot to {shot_pass}")
    
    page_text = driver.page_source
    if "All Automated Test Cases Passed!" in page_text:
        print("SUCCESS: Unit tests ran and PASSED on the solution code!")
    else:
        print("Check page text/screenshot for details.")

finally:
    driver.quit()
