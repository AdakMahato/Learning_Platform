"""
Automated Test Suite for AI & Machine Learning Engineering Lab
Tests:
1. Syllabus Completeness & Matrix Validation
2. Master Curriculum Content Integrity (Cases 00 - 24)
3. Code Labs Integrity (Zero Empty Code Blocks)
4. Quiz Schema & Explanation Coverage
5. Machine Learning & Engineering Algorithm Math Correctness
6. Isolated Python Runner & Timeout Safety
"""

import sys
import os
import unittest
import numpy as np
import pandas as pd

# Ensure ai_story_lab root is on sys.path
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
if BASE_DIR not in sys.path:
    sys.path.insert(0, BASE_DIR)

import syllabus_map
import level_content
import story_data
import py_runner
import engineering_labs

class TestSyllabusCompleteness(unittest.TestCase):
    def test_all_modules_present(self):
        self.assertEqual(len(syllabus_map.SYLLABUS_MODULES), 8, "Expected 8 mandatory academic syllabus modules")
        
    def test_topic_count_and_status(self):
        stats = syllabus_map.get_coverage_stats()
        self.assertGreaterEqual(stats["total_topics"], 40, "Expected at least 40 mapped academic topics")
        self.assertEqual(stats["topic_coverage_pct"], 100.0, "Expected 100% academic topic coverage")
        
    def test_mandatory_laboratories(self):
        labs = syllabus_map.REQUIRED_LABORATORIES
        self.assertIn("LAB_A", labs, "Missing Lab A: Motor Temperature Prediction")
        self.assertIn("LAB_B", labs, "Missing Lab B: Material Property Clustering")
        self.assertIn("LAB_C", labs, "Missing Lab C: Faulty Circuit Detection")
        for key, lab in labs.items():
            self.assertEqual(lab["status"], "IMPLEMENTED", f"Lab {key} must have status IMPLEMENTED")

    def test_mandatory_industry_cases(self):
        cases = syllabus_map.REQUIRED_INDUSTRY_CASES
        self.assertIn("SIEMENS", cases, "Missing Siemens Case Study")
        self.assertIn("GE", cases, "Missing GE Case Study")
        self.assertIn("HONEYWELL", cases, "Missing Honeywell Case Study")
        for key, c in cases.items():
            self.assertEqual(c["status"], "VERIFIED_AND_DOCUMENTED", f"Case {key} must be verified and documented")
            self.assertGreater(len(c["verified_sources"]), 0, f"Case {key} must have verified references")

class TestCurriculumContentIntegrity(unittest.TestCase):
    def setUp(self):
        self.lc = level_content.LEVEL_CONTENT
        self.stories = story_data.STORIES
        
    def test_all_25_cases_exist(self):
        self.assertEqual(len(self.stories), 25, "Expected 25 cases in story_data.STORIES")
        for i in range(25):
            self.assertIn(str(i), self.lc, f"Case {i} missing from LEVEL_CONTENT")
            
    def test_case_titles_not_empty_or_generic(self):
        for i in range(25):
            c = self.lc[str(i)]
            title = c.get("title", "")
            self.assertTrue(title and title != "No Title", f"Case {i} has empty or missing title")
            self.assertTrue("Case " in title, f"Case {i} title should follow standard naming: '{title}'")

    def test_zero_empty_code_labs(self):
        empty_code_count = 0
        total_code_labs = 0
        for cid, case in self.lc.items():
            for ep in case.get("episodes", []):
                for b in ep.get("blocks", []):
                    if b.get("type") == "code_lab":
                        total_code_labs += 1
                        starter = b.get("starter_code", "").strip()
                        if not starter:
                            empty_code_count += 1
        self.assertGreater(total_code_labs, 50, "Expected at least 50 code labs across all cases")
        self.assertEqual(empty_code_count, 0, f"Found {empty_code_count} code labs with empty starter code!")

    def test_all_quizzes_have_answers_and_explanations(self):
        total_quizzes = 0
        for cid, case in self.lc.items():
            for ep in case.get("episodes", []):
                for b in ep.get("blocks", []):
                    if b.get("type") in ("interactive", "fill_in_the_blank"):
                        total_quizzes += 1
                        self.assertTrue(b.get("answer"), f"Quiz in Case {cid} missing 'answer'")
                        self.assertTrue(b.get("explanation"), f"Quiz in Case {cid} missing 'explanation'")
        self.assertGreater(total_quizzes, 80, "Expected at least 80 active quizzes across curriculum")

class TestAlgorithmAndModelCorrectness(unittest.TestCase):
    def test_motor_temperature_dataset(self):
        df = engineering_labs.load_motor_temperature_dataset(n_samples=100)
        self.assertEqual(len(df), 100)
        self.assertIn("Stator_Winding_Temp_C", df.columns)
        self.assertIn("Current_A", df.columns)
        # Physical check: current > 0 and stator temp > 0
        self.assertTrue((df["Current_A"] > 0).all())
        self.assertTrue((df["Stator_Winding_Temp_C"] > 10).all())

    def test_materials_dataset_clustering(self):
        df = engineering_labs.load_materials_dataset()
        self.assertEqual(len(df), 20)
        self.assertIn("Density", df.columns)
        self.assertIn("Tensile_MPa", df.columns)
        # Verify ceramics have high hardness
        ceramics = df[df["Family"] == "Ceramic"]
        self.assertTrue((ceramics["Hardness_HV"] > 1000).all())

    def test_circuit_dataset_distributions(self):
        df = engineering_labs.load_circuit_dataset(n_samples=200)
        self.assertEqual(len(df), 200)
        self.assertIn("Defective", df.columns)
        # Defective rate around 20%
        defect_rate = df["Defective"].mean()
        self.assertTrue(0.10 <= defect_rate <= 0.30)

class TestPyRunnerExecution(unittest.TestCase):
    def test_successful_python_execution(self):
        code = "a = 15\nb = 25\nprint('SUM:', a + b)"
        success, out, err = py_runner.run_py(code, timeout=3)
        self.assertTrue(success, f"Execution failed: {err}")
        self.assertIn("SUM: 40", out)

    def test_timeout_protection(self):
        code = "while True: pass"
        success, out, err = py_runner.run_py(code, timeout=1)
        self.assertFalse(success)
        self.assertIn("Timed Out", err)

if __name__ == "__main__":
    unittest.main()
