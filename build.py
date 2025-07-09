import os
import subprocess
import sys

def build_executable():
    """Build executable using PyInstaller"""
    print("Building LazyAF executable...")
    
    # Check if PyInstaller is installed
    try:
        import PyInstaller
    except ImportError:
        print("Installing PyInstaller...")
        subprocess.run([sys.executable, "-m", "pip", "install", "pyinstaller"], check=True)
    
    # PyInstaller command
    cmd = [
        "pyinstaller",
        "--onefile",                    # Create single executable
        "--windowed",                   # Hide console window
        "--name=LazyAF_4.20",          # Executable name
        "--clean",                      # Clean build
        "auto_clicker.py"
    ]
    
    try:
        # Run PyInstaller
        result = subprocess.run(cmd, check=True, capture_output=True, text=True)
        print("Build successful!")
        print(f"Executable created at: dist/LazyAF_4.20.exe")
        
        # Create a simple batch file to run the executable
        with open("run_lazyaf.bat", "w") as f:
            f.write("@echo off\n")
            f.write("cd /d \"%~dp0\"\n")
            f.write("dist\\LazyAF_4.20.exe\n")
            f.write("pause\n")
        
        print("Also created run_lazyaf.bat for easy execution")
        
    except subprocess.CalledProcessError as e:
        print(f"Build failed: {e}")
        print("stdout:", e.stdout)
        print("stderr:", e.stderr)
        return False
    
    return True

def install_dependencies():
    """Install required dependencies"""
    print("Installing dependencies...")
    
    try:
        subprocess.run([sys.executable, "-m", "pip", "install", "-r", "requirements.txt"], check=True)
        print("Dependencies installed successfully!")
        return True
    except subprocess.CalledProcessError as e:
        print(f"Failed to install dependencies: {e}")
        return False

if __name__ == "__main__":
    print("LazyAF 4.20 Build Script")
    print("=" * 40)
    
    # Install dependencies first
    if not install_dependencies():
        print("Failed to install dependencies. Exiting.")
        sys.exit(1)
    
    # Build executable
    if build_executable():
        print("\nBuild completed successfully!")
        print("\nTo run LazyAF:")
        print("1. Double-click 'run_lazyaf.bat'")
        print("2. Or run 'dist/LazyAF_4.20.exe' directly")
    else:
        print("Build failed!")
        sys.exit(1) 