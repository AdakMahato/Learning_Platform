import json
import os

all_cases = {}

for part in range(1, 5):
    json_path = f"/Users/aadarshamahato/Downloads/LEARNING_PLATFORM/cloud_story_lab/cases_part{part}.json"
    with open(json_path, 'r', encoding='utf-8') as f:
        part_data = json.load(f)
        all_cases.update(part_data)

print(f"Total merged syllabus cases for Cloud Story Lab: {len(all_cases)}")
expected_keys = [str(i) for i in range(16)]
missing = [k for k in expected_keys if k not in all_cases]
if missing:
    print(f"ERROR: Missing cases: {missing}")
else:
    print("All 16 Cloud syllabus cases (0-15) are present and accounted for!")

# Write level_content.py
output_path = "/Users/aadarshamahato/Downloads/LEARNING_PLATFORM/cloud_story_lab/level_content.py"
with open(output_path, 'w', encoding='utf-8') as f:
    f.write("# Master Curriculum Database for Cloud Story Lab (Syllabus Aligned)\n")
    f.write("# 16 University-Level Cases Covering the Complete Cloud Computing Body of Knowledge\n\n")
    f.write("LEVEL_CONTENT = ")
    json.dump(all_cases, f, indent=2, ensure_ascii=False)
    f.write("\n")

print(f"Successfully compiled {output_path} ({os.path.getsize(output_path)} bytes)")
