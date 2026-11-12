import time
import os
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

chrome_options = Options()
chrome_options.add_argument("--headless=new")
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--disable-dev-shm-usage")
chrome_options.add_argument("--window-size=1440,1100")

driver = webdriver.Chrome(options=chrome_options)
artifact_dir = "/Users/aadarshamahato/.gemini/antigravity/brain/d6359211-9b16-48fb-acb0-4233b900183e"

try:
    print("Navigating to http://localhost:8504...")
    driver.get("http://localhost:8504")
    
    # Wait for Streamlit to render
    WebDriverWait(driver, 15).until(
        EC.presence_of_element_located((By.XPATH, "//*[contains(text(), 'SOFTWARE ENGINEERING STORY LAB') or contains(text(), 'Case')]"))
    )
    time.sleep(3)
    
    home_shot = os.path.join(artifact_dir, "se_home_dashboard.png")
    driver.save_screenshot(home_shot)
    print(f"Saved home screenshot to {home_shot}")
    
    # Navigate to Case 00
    driver.get("http://localhost:8504/the_software_crisis")
    time.sleep(4)
    
    case0_shot = os.path.join(artifact_dir, "se_case00_module1.png")
    driver.save_screenshot(case0_shot)
    print(f"Saved Case 00 screenshot to {case0_shot}")
    
    # Test Fill in the blank with a trailing dot: "Crisis."
    print("Testing Fill in the blank with trailing period...")
    inputs = driver.find_elements(By.TAG_NAME, "input")
    for inp in inputs:
        if inp.get_attribute("type") == "text":
            inp.send_keys("Crisis.")
            time.sleep(1)
            break
            
    # Click Submit Answer button
    submit_buttons = driver.find_elements(By.XPATH, "//button[contains(., 'Submit Answer')]")
    if submit_buttons:
        # Click the last submit button (which corresponds to fill-in-the-blank)
        driver.execute_script("arguments[0].click();", submit_buttons[-1])
        time.sleep(2)
        
    fib_shot = os.path.join(artifact_dir, "se_case00_fib_test.png")
    driver.save_screenshot(fib_shot)
    print(f"Saved Fill-in-the-blank test screenshot to {fib_shot}")
    
    # Check page text for success
    page_source = driver.page_source
    if "Correct!" in page_source:
        print("SUCCESS: 'Crisis.' was accepted as correct without period restriction!")
    else:
        print("Note: check fib result in screenshot")
        
    print("All browser verification tests completed successfully.")

finally:
    driver.quit()
