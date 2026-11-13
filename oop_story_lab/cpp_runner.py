import subprocess
import tempfile
import os

def run_cpp(code: str, timeout: int = 3, input_data: str = None):
    """
    Compiles and runs C++ code securely with a timeout.
    Returns (success: bool, output: str, compiler_error: str)
    """
    with tempfile.TemporaryDirectory() as temp_dir:
        cpp_file = os.path.join(temp_dir, "main.cpp")
        exe_file = os.path.join(temp_dir, "main.out")
        
        with open(cpp_file, "w") as f:
            includes = []
            rest = []
            for line in code.split('\n'):
                if line.startswith('#include'):
                    includes.append(line)
                else:
                    rest.append(line)
            
            boilerplate = """
class IDelivery { public: virtual double calculateCost() const = 0; virtual ~IDelivery() {} };
class ITrackable { public: virtual void pingLocation() = 0; virtual ~ITrackable() {} };
class DataBuffer {};
class Observer {};
class IComponent { public: virtual void update() = 0; virtual ~IComponent() {} };
class Account {};
class Logger { public: void print(const char*) {} };
class Request { public: void process() {} };
class V8Engine { public: void start() {} };
struct IEngine { virtual void start() = 0; virtual ~IEngine() {} };
class FileLogger {};
class EventDispatcher {};
class Server { public: Server(EventDispatcher&, FileLogger&) {} };
bool error_occurred = true;
"""
            f.write('\n'.join(includes) + "\n" + boilerplate + "\n" + '\n'.join(rest))
            
        # Compile
        compile_process = subprocess.run(
            ["g++", "-std=c++17", cpp_file, "-o", exe_file],
            capture_output=True,
            text=True
        )
        
        if compile_process.returncode != 0:
            return False, "", compile_process.stderr
            
        # Run
        try:
            run_process = subprocess.run(
                [exe_file],
                input=input_data,
                capture_output=True,
                text=True,
                timeout=timeout
            )
            if run_process.returncode != 0:
                return False, run_process.stdout, f"Runtime Error (Exit Code: {run_process.returncode})\n{run_process.stderr}"
            return True, run_process.stdout, ""
        except subprocess.TimeoutExpired:
            return False, "", "Execution Timed Out"
