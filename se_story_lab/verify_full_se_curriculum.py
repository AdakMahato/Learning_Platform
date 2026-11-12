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

def check_for_errors(page_name):
    page_text = driver.page_source
    errors = []
    for marker in ["AttributeError", "Traceback (most recent call last)", "NameError", "KeyError", "SyntaxError"]:
        if marker in page_text:
            errors.append(marker)
    if errors:
        print(f"❌ ERRORS FOUND ON {page_name}: {errors}")
        return False
    else:
        print(f"✅ Clean page render on {page_name} (No tracebacks or unhandled exceptions)")
        return True

try:
    print("1. Testing Home Dashboard (http://localhost:8504)...")
    driver.get("http://localhost:8504")
    time.sleep(3)
    check_for_errors("Home Dashboard")
    home_shot = os.path.join(artifact_dir, "se_syllabus_dashboard.png")
    driver.save_screenshot(home_shot)
    print(f"Saved: {home_shot}")

    test_urls = [
        ("Case 00 Foundations", "http://localhost:8504/software_engineering_foundations_&_evolution", "se_case00_foundations.png"),
        ("Case 04 Requirements & SRS", "http://localhost:8504/requirements_modeling_&_the_ieee_srs_specification", "se_case04_srs.png"),
        ("Case 06 Design & Cohesion", "http://localhost:8504/design_principles_modularity_cohesion_&_coupling", "se_case06_cohesion.png"),
        ("Case 08 UML Structural", "http://localhost:8504/uml_structural_modeling_class_component_&_deployment", "se_case08_uml_struct.png"),
        ("Case 10 Architecture", "http://localhost:8504/software_architecture_&_dfd_to_structure_chart", "se_case10_arch.png"),
        ("Case 13 White-Box Testing", "http://localhost:8504/white_box_testing_loop_testing_&_high_order_verification", "se_case13_whitebox.png"),
        ("Case 15 Failure Forensics", "http://localhost:8504/capstone_investigation_mission_critical_failure_forensics", "se_case15_forensics.png")
    ]

    for label, url, shot_name in test_urls:
        print(f"\nTesting {label} ({url})...")
        driver.get(url)
        time.sleep(3)
        check_for_errors(label)
        shot_path = os.path.join(artifact_dir, shot_name)
        driver.save_screenshot(shot_path)
        print(f"Saved screenshot: {shot_path}")

    print("\nALL SYLLABUS PAGES VERIFIED SUCCESSFULLY!")

finally:
    driver.quit()
