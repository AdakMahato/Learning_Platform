import os
import sys
import json
import re

# Add path to import ultra files from dbms_story_lab
sys.path.append("/Users/aadarshamahato/Downloads/LEARNING_PLATFORM/dbms_story_lab")

import level_content
import story_data

try:
    import ultra_01_05
    import ultra_07_11
    import ultra_12_16
    import ultra_17_24
except ImportError as e:
    print(f"Warning importing ultra files: {e}")

def normalize_quizzes_and_code():
    print("Normalizing and repairing level_content.py...")
    lc = level_content.LEVEL_CONTENT
    sd_map = {s["id"]: s for s in story_data.STORIES}

    # 1. First, repair titles for all cases
    for cid_str, case in lc.items():
        cid = int(cid_str) if cid_str.isdigit() else -1
        sd = sd_map.get(cid, {})
        full_title = f"Case {cid:02d}: {sd.get('title', 'AI Investigation')}" if cid >= 0 else case.get("title", "")
        case["title"] = full_title

    # 2. Re-extract and repair Cases 7 to 11 from ultra_07_11
    if "ultra_07_11" in sys.modules:
        c_07_11 = ultra_07_11.CONTENT_07_11
        for cid_str in ['7', '8', '9', '10', '11']:
            if cid_str in c_07_11 and cid_str in lc:
                raw_case = c_07_11[cid_str]
                episodes = lc[cid_str].get("episodes", [])
                raw_modules = raw_case.get("modules", [])
                
                for mod_idx, (ep, raw_mod) in enumerate(zip(episodes, raw_modules)):
                    raw_blocks = raw_mod.get("episodes", [])
                    
                    # Find code and interactive blocks in raw_blocks
                    raw_code_blocks = [b for b in raw_blocks if b.get("type") == "code_lab"]
                    raw_quiz_blocks = [b for b in raw_blocks if b.get("type") == "interactive"]
                    
                    # Update code_lab blocks in ep
                    cur_code_idx = 0
                    cur_quiz_idx = 0
                    new_blocks = []
                    
                    for b in ep.get("blocks", []):
                        btype = b.get("type")
                        if btype == "code_lab":
                            if cur_code_idx < len(raw_code_blocks):
                                raw_cb = raw_code_blocks[cur_code_idx]
                                code_content = raw_cb.get("code") or raw_cb.get("content") or ""
                                cur_code_idx += 1
                                if code_content:
                                    # Add print trace if missing
                                    if "print(" not in code_content:
                                        code_content += "\n\n# Execution trace\nprint('Module code executed successfully.')"
                                    b["starter_code"] = code_content
                                    b["solution_code"] = code_content
                                    b["explanation"] = f"**Why it works:** Implements the algorithmic formulation for {ep.get('title', 'this module')}."
                            new_blocks.append(b)
                        elif btype in ("interactive", "fill_in_the_blank"):
                            new_blocks.append(b)
                        else:
                            new_blocks.append(b)
                            
                    # If ep has no quizzes, inject the quizzes from raw_quiz_blocks!
                    has_quiz = any(b.get("type") in ("interactive", "fill_in_the_blank") for b in new_blocks)
                    if not has_quiz and raw_quiz_blocks:
                        for qb in raw_quiz_blocks:
                            q_text = qb.get("question") or qb.get("content") or "Knowledge Check"
                            options = qb.get("options", ["Option A", "Option B"])
                            correct_val = qb.get("correct", 0)
                            if isinstance(correct_val, int) and 0 <= correct_val < len(options):
                                ans_text = options[correct_val]
                            else:
                                ans_text = str(correct_val) if correct_val else options[0]
                                
                            explanation = qb.get("explanation") or f"**Correct Answer:** {ans_text}. Understanding this principle is essential for correctly applying this method in engineering."
                            
                            # Decide whether to make it fill_in_the_blank or interactive
                            if len(options) == 2 and any(k in q_text.lower() for k in ["what is", "define", "primary"]):
                                new_blocks.append({
                                    "type": "fill_in_the_blank",
                                    "title": "Recall Challenge",
                                    "question": f"{q_text}\n\nKey Term: _____",
                                    "answer": ans_text,
                                    "explanation": explanation
                                })
                            else:
                                new_blocks.append({
                                    "type": "interactive",
                                    "title": "Mastery Challenge",
                                    "question": q_text,
                                    "options": options,
                                    "answer": ans_text,
                                    "explanation": explanation
                                })
                                
                    ep["blocks"] = new_blocks
                print(f"Repaired Case {cid_str} code labs and quizzes.")

    # 3. Re-extract and repair Cases 12 to 16 from ultra_12_16
    if "ultra_12_16" in sys.modules:
        c_12_16 = ultra_12_16.CONTENT_12_16
        for cid_str in ['12', '13', '14', '15', '16']:
            if cid_str in c_12_16 and cid_str in lc:
                raw_case = c_12_16[cid_str]
                episodes = lc[cid_str].get("episodes", [])
                raw_modules = raw_case.get("modules", [])
                
                for mod_idx, (ep, raw_mod) in enumerate(zip(episodes, raw_modules)):
                    raw_blocks = raw_mod.get("episodes", [])
                    raw_quiz_blocks = [b for b in raw_blocks if b.get("type") == "interactive"]
                    
                    has_quiz = any(b.get("type") in ("interactive", "fill_in_the_blank") for b in ep.get("blocks", []))
                    if not has_quiz and raw_quiz_blocks:
                        for qb in raw_quiz_blocks:
                            q_text = qb.get("question") or qb.get("content") or "Knowledge Check"
                            options = qb.get("options", ["True", "False"])
                            ans_text = qb.get("answer") or options[0]
                            explanation = qb.get("explanation") or f"**Analysis:** {ans_text} is correct because this mathematical relationship determines how uncertainty propagates through the system."
                            
                            ep["blocks"].append({
                                "type": "interactive",
                                "title": "Probabilistic Reasoning Check",
                                "question": q_text,
                                "options": options,
                                "answer": ans_text,
                                "explanation": explanation
                            })
                print(f"Repaired Case {cid_str} quizzes.")

    # 4. Re-extract and repair Cases 17 to 24 from ultra_17_24
    if "ultra_17_24" in sys.modules:
        c_17_24 = ultra_17_24.CONTENT_17_24
        for cid_str in ['17', '18', '19', '20', '21', '22', '23', '24']:
            if cid_str in c_17_24 and cid_str in lc:
                raw_case = c_17_24[cid_str]
                episodes = lc[cid_str].get("episodes", [])
                raw_modules = raw_case.get("modules", [])
                
                for mod_idx, (ep, raw_mod) in enumerate(zip(episodes, raw_modules)):
                    raw_blocks = raw_mod.get("episodes", [])
                    raw_quiz_blocks = [b for b in raw_blocks if b.get("type") == "interactive"]
                    
                    has_quiz = any(b.get("type") in ("interactive", "fill_in_the_blank") for b in ep.get("blocks", []))
                    if not has_quiz and raw_quiz_blocks:
                        for qb_idx, qb in enumerate(raw_quiz_blocks):
                            q_text = qb.get("content") or qb.get("question") or "Machine Learning Check"
                            options = qb.get("options", ["Option 1", "Option 2"])
                            ans_text = qb.get("answer") or options[0]
                            explanation = qb.get("explanation") or f"**Evaluation:** {ans_text} is the correct conclusion based on the training dynamics and mathematical formulation."
                            
                            if qb_idx % 2 == 1:
                                ep["blocks"].append({
                                    "type": "fill_in_the_blank",
                                    "title": "Engineering Concept Check",
                                    "question": f"{q_text}\n\nExact Term: _____",
                                    "answer": ans_text,
                                    "explanation": explanation
                                })
                            else:
                                ep["blocks"].append({
                                    "type": "interactive",
                                    "title": "ML Mastery Quiz",
                                    "question": q_text,
                                    "options": options,
                                    "answer": ans_text,
                                    "explanation": explanation
                                })
                print(f"Repaired Case {cid_str} quizzes.")

    # 5. Fix Case 06 (The Game of Minds)
    if '6' in lc:
        lc['6']["title"] = "Case 06: The Game of Minds"
        # Add a 4th module if it only has 3
        if len(lc['6'].get("episodes", [])) == 3:
            lc['6']["episodes"].append({
                "title": "Module 4: Evaluation Functions and Horizon Effects",
                "blocks": [
                    {
                        "type": "concept",
                        "title": "Heuristic Evaluation Functions",
                        "content": "In real-world engineering games (and chess/Go), we cannot search to terminal leaf states due to exponential branching factor ($b^d$). We must cut off search at a specified depth and apply an **Evaluation Function** $Eval(s)$ that estimates the expected utility of state $s$."
                    },
                    {
                        "type": "visual",
                        "title": "Search Cutoff & Evaluation",
                        "code": "graph TD\n  Root[\"Current State\"] --> D1A[\"Depth 1\"]\n  Root --> D1B[\"Depth 1\"]\n  D1A --> D2A[\"Depth 2 Cutoff\"]:::cutoff\n  D1A --> D2B[\"Depth 2 Cutoff\"]:::cutoff\n  D1B --> D2C[\"Depth 2 Cutoff\"]:::cutoff\n  classDef cutoff fill:#f59e0b2a,stroke:#F59E0B,stroke-width:2px;"
                    },
                    {
                        "type": "code_lab",
                        "title": "Depth-Limited Minimax Implementation",
                        "starter_code": "def eval_board(pieces_count, mobility_score):\n    # Weighted evaluation function\n    return (pieces_count * 10) + (mobility_score * 1.5)\n\nprint('Heuristic State Value:', eval_board(5, 12))",
                        "solution_code": "def eval_board(pieces_count, mobility_score):\n    return (pieces_count * 10) + (mobility_score * 1.5)\n\nprint('Heuristic State Value:', eval_board(5, 12))",
                        "expected_output": "Heuristic State Value: 68.0",
                        "explanation": "Weighted linear evaluation functions combine independent features into a single scalar utility value.",
                        "test_cases": []
                    },
                    {
                        "type": "interactive",
                        "title": "Horizon Effect Challenge",
                        "question": "What is the 'Horizon Effect' in game tree search?",
                        "options": [
                            "Pushing an unavoidable damaging move just beyond the search depth limit",
                            "Searching too fast and exceeding memory buffers",
                            "Pruning the winning branch accidentally"
                        ],
                        "answer": "Pushing an unavoidable damaging move just beyond the search depth limit",
                        "explanation": "The Horizon Effect occurs when the agent delays a detrimental move by making stalling moves, pushing the disaster past its search horizon."
                    }
                ]
            })
            print("Added Module 4 to Case 06.")

    # Write back clean level_content.py
    with open("/Users/aadarshamahato/Downloads/LEARNING_PLATFORM/ai_story_lab/level_content.py", "w", encoding="utf-8") as f:
        f.write("# Master Curriculum Database for AI Story Lab\n")
        f.write("LEVEL_CONTENT = \\\n")
        json.dump(lc, f, indent=4, ensure_ascii=False)
    print("SUCCESS: Successfully normalized and saved level_content.py!")

if __name__ == "__main__":
    normalize_quizzes_and_code()
