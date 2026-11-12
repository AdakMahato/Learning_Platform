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
    driver.get("http://localhost:8504/the_solid_foundations")
    time.sleep(3)
    
    # Click Module 4 in the sidebar
    m4_btn = driver.find_element(By.XPATH, "//button[contains(., 'Module 4')]")
    driver.execute_script("arguments[0].click();", m4_btn)
    time.sleep(3)
    
    shot_m4 = os.path.join(artifact_dir, "se_case12_module4_codelab.png")
    driver.save_screenshot(shot_m4)
    print("Saved Case 12 Module 4 screenshot")
    
    # Click "Load Clean Architectural Solution"
    load_sol_btns = driver.find_elements(By.XPATH, "//button[contains(., 'Solution')]")
    if load_sol_btns:
        driver.execute_script("arguments[0].click();", load_sol_btns[0])
        time.sleep(2)
        
    # Click "Execute & Run Test Suite"
    run_test_btns = driver.find_elements(By.XPATH, "//button[contains(., 'Run Test Suite') or contains(., 'Execute')]")
    for btn in run_test_btns:
        if "Execute" in btn.text or "Run Test Suite" in btn.text:
            driver.execute_script("arguments[0].click();", btn)
            time.sleep(3)
            break
            
    shot_executed = os.path.join(artifact_dir, "se_case12_codelab_executed.png")
    driver.save_screenshot(shot_executed)
    print("Saved Code Lab execution screenshot")

finally:
    driver.quit()
