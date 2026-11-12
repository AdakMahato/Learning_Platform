import json
import py_runner

with open("/Users/aadarshamahato/Downloads/LEARNING_PLATFORM/se_story_lab/level_content.py") as f:
    data = json.loads(f.read().split("LEVEL_CONTENT = ", 1)[1])

total_labs = 0
passed_labs = 0

print("Testing all Code Labs across all 25 cases...")

for cid, case in sorted(data.items(), key=lambda x: int(x[0])):
    for m_idx, ep in enumerate(case.get("episodes", [])):
        for b_idx, b in enumerate(ep.get("blocks", [])):
            if b.get("type") == "code_lab":
                total_labs += 1
                title = b.get("title", f"Lab {total_labs}")
                sol = b.get("solution_code", "")
                test = b.get("test_code", "")
                
                full_code = sol + "\n" + test
                success, stdout, stderr = py_runner.run_py(full_code)
                
                if success:
                    passed_labs += 1
                    print(f"  [PASS] Case {cid.zfill(2)} M{m_idx+1}: {title}")
                else:
                    print(f"  [FAIL] Case {cid.zfill(2)} M{m_idx+1}: {title}")
                    print("  Error:", stderr or stdout)

print(f"\nResult: {passed_labs}/{total_labs} Code Labs executed and verified successfully!")
