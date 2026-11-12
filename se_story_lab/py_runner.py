import subprocess
import tempfile
import os

def run_py(code: str, timeout: int = 3, input_data: str = None):
    """
    Runs Python code securely in an isolated subprocess with a timeout.
    Returns (success: bool, output: str, runtime_error: str)
    """
    with tempfile.TemporaryDirectory() as temp_dir:
        py_file = os.path.join(temp_dir, "main.py")
        
        with open(py_file, "w", encoding="utf-8") as f:
            f.write(code)
            
        try:
            run_process = subprocess.run(
                ["python3", py_file],
                input=input_data,
                capture_output=True,
                text=True,
                timeout=timeout
            )
            if run_process.returncode != 0:
                return False, run_process.stdout, f"Runtime Error:\n{run_process.stderr}"
            return True, run_process.stdout, ""
        except subprocess.TimeoutExpired:
            return False, "", "Execution Timed Out (Infinite Loop?)"
