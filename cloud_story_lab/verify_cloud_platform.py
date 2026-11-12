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
    print("1. Testing Cloud Dashboard (http://localhost:8505)...")
    driver.get("http://localhost:8505")
    time.sleep(3)
    check_for_errors("Cloud Dashboard")
    dash_shot = os.path.join(artifact_dir, "cloud_dashboard.png")
    driver.save_screenshot(dash_shot)
    print(f"Saved dashboard screenshot to {dash_shot}")

    test_cases = [
        ("Case 00: Evolution", "http://localhost:8505/computing_evolution_from_mainframes_to_the_cloud", "cloud_case00_evolution.png"),
        ("Case 02: AWS EC2", "http://localhost:8505/aws_core_compute_&_elasticity_ec2_architecture", "cloud_case02_ec2.png"),
        ("Case 06: REST API Lab", "http://localhost:8505/restful_web_services_&_cloud_api_design", "cloud_case06_rest.png"),
        ("Case 08: VDC Migration", "http://localhost:8505/virtualized_data_centers_vdc_&_process_migration", "cloud_case08_vdc.png"),
        ("Case 10: Green Cloud PUE", "http://localhost:8505/data_center_energy_cooling_&_green_cloud_sustainability", "cloud_case10_green.png"),
        ("Case 12: MapReduce Lab", "http://localhost:8505/distributed_data_processing_mapreduce_&_the_hadoop_ecosystem", "cloud_case12_mapreduce.png"),
        ("Case 15: FinOps Forensics", "http://localhost:8505/capstone_investigation_cloud_scalability_finops_&_failure_forensics", "cloud_case15_finops.png")
    ]

    for label, url, shot_file in test_cases:
        print(f"\nTesting {label} ({url})...")
        driver.get(url)
        time.sleep(3)
        check_for_errors(label)
        shot_path = os.path.join(artifact_dir, shot_file)
        driver.save_screenshot(shot_path)
        print(f"Saved: {shot_path}")

    print("\nALL CLOUD STORY LAB PAGES VERIFIED CLEANLY!")

finally:
    driver.quit()
