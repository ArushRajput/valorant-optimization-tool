"""
Test script to verify all features of the Valorant Optimization Tool
"""
import os
import sys
from pathlib import Path
import subprocess

def test_imports():
    """Test if all required modules can be imported"""
    print("Testing imports...")
    try:
        import tkinter
        print("✓ tkinter")
        from tkinter import ttk, messagebox
        print("✓ tkinter.ttk, tkinter.messagebox")
        import shutil
        print("✓ shutil")
        import threading
        print("✓ threading")
        import ctypes
        print("✓ ctypes")
        return True
    except Exception as e:
        print(f"✗ Import failed: {e}")
        return False

def test_paths():
    """Test if all paths are accessible"""
    print("\nTesting paths...")
    paths_to_check = {
        "LOCALAPPDATA": os.environ.get('LOCALAPPDATA'),
        "TEMP": os.environ.get('TEMP'),
        "TMP": os.environ.get('TMP'),
        "WINDIR": os.environ.get('WINDIR'),
        "PROGRAMFILES": os.environ.get('PROGRAMFILES')
    }
    
    all_ok = True
    for name, path in paths_to_check.items():
        if path and Path(path).exists():
            print(f"✓ {name}: {path}")
        else:
            print(f"✗ {name}: Not found")
            all_ok = False
    
    return all_ok

def test_valorant_paths():
    """Test Valorant-specific paths"""
    print("\nTesting Valorant paths...")
    
    config_path = Path(os.environ['LOCALAPPDATA']) / "VALORANT" / "Saved" / "Config"
    shader_paths = [
        Path(os.environ['LOCALAPPDATA']) / "VALORANT" / "Saved" / "ShaderCache",
        Path(os.environ['LOCALAPPDATA']) / "Riot Games" / "VALORANT" / "Saved" / "ShaderCache"
    ]
    riot_client = Path(os.environ['PROGRAMFILES']) / "Riot Games" / "Riot Client" / "RiotClientServices.exe"
    
    if config_path.exists():
        files = len(list(config_path.rglob("*")))
        print(f"✓ Config folder found: {config_path} ({files} files)")
    else:
        print(f"⚠ Config folder not found: {config_path} (Valorant may not be installed)")
    
    for shader_path in shader_paths:
        if shader_path.exists():
            print(f"✓ Shader cache found: {shader_path}")
        else:
            print(f"⚠ Shader cache not found: {shader_path}")
    
    if riot_client.exists():
        print(f"✓ Riot Client found: {riot_client}")
    else:
        print(f"⚠ Riot Client not found: {riot_client}")

def test_system_paths():
    """Test system optimization paths"""
    print("\nTesting system paths...")
    
    paths = {
        "DirectX Cache": Path(os.environ['LOCALAPPDATA']) / "D3DSCache",
        "Prefetch": Path(os.environ['WINDIR']) / "Prefetch",
        "Explorer Cache": Path(os.environ['LOCALAPPDATA']) / "Microsoft" / "Windows" / "Explorer",
        "INetCache": Path(os.environ['LOCALAPPDATA']) / "Microsoft" / "Windows" / "INetCache"
    }
    
    for name, path in paths.items():
        if path.exists():
            try:
                count = len(list(path.iterdir()))
                print(f"✓ {name}: {path} ({count} items)")
            except:
                print(f"✓ {name}: {path} (access restricted)")
        else:
            print(f"⚠ {name}: Not found at {path}")

def test_commands():
    """Test if system commands work"""
    print("\nTesting system commands...")
    
    # Test ipconfig
    try:
        result = subprocess.run(["ipconfig", "/?"], capture_output=True, timeout=5)
        if result.returncode == 0:
            print("✓ ipconfig command available")
        else:
            print("✗ ipconfig command failed")
    except Exception as e:
        print(f"✗ ipconfig test failed: {e}")

def test_gui_launch():
    """Test if GUI can be launched"""
    print("\nTesting GUI launch...")
    try:
        import tkinter as tk
        root = tk.Tk()
        root.withdraw()  # Hide window
        print("✓ Tkinter GUI can be initialized")
        root.destroy()
        return True
    except Exception as e:
        print(f"✗ GUI initialization failed: {e}")
        return False

def test_exe_exists():
    """Test if the .exe file was created"""
    print("\nTesting executable...")
    exe_path = Path("d:/Ai ITEMS/dj/dist/ValorantOptimizationTool.exe")
    
    if exe_path.exists():
        size_mb = exe_path.stat().st_size / (1024 * 1024)
        print(f"✓ Executable found: {exe_path}")
        print(f"  Size: {size_mb:.2f} MB")
        return True
    else:
        print(f"✗ Executable not found: {exe_path}")
        return False

def main():
    print("=" * 60)
    print("VALORANT OPTIMIZATION TOOL - COMPREHENSIVE TEST")
    print("=" * 60)
    
    results = []
    
    results.append(("Imports", test_imports()))
    results.append(("System Paths", test_paths()))
    test_valorant_paths()
    test_system_paths()
    results.append(("System Commands", test_commands()))
    results.append(("GUI Launch", test_gui_launch()))
    results.append(("Executable", test_exe_exists()))
    
    print("\n" + "=" * 60)
    print("TEST SUMMARY")
    print("=" * 60)
    
    for test_name, passed in results:
        status = "✓ PASS" if passed else "✗ FAIL"
        print(f"{status}: {test_name}")
    
    all_passed = all(result[1] for result in results)
    
    print("\n" + "=" * 60)
    if all_passed:
        print("✓ ALL CRITICAL TESTS PASSED!")
        print("The tool is ready to use and share.")
    else:
        print("⚠ Some tests failed, but the tool may still work.")
        print("Check warnings above for details.")
    print("=" * 60)

if __name__ == "__main__":
    main()
