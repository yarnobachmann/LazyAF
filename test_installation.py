#!/usr/bin/env python3
"""
Test script to verify LazyAF installation and dependencies.
This script tests that all required dependencies can be imported
and basic functionality works correctly.
"""

import sys
import os
import unittest
from unittest.mock import Mock, patch

def test_imports():
    """Test that all required dependencies can be imported."""
    try:
        import customtkinter
        print("✅ CustomTkinter imported successfully")
    except ImportError as e:
        print(f"❌ Failed to import CustomTkinter: {e}")
        return False
    
    try:
        import pyautogui
        print("✅ PyAutoGUI imported successfully")
    except ImportError as e:
        print(f"❌ Failed to import PyAutoGUI: {e}")
        return False
    
    try:
        import pynput
        print("✅ Pynput imported successfully")
    except ImportError as e:
        print(f"❌ Failed to import Pynput: {e}")
        return False
    
    try:
        from PIL import Image
        print("✅ Pillow (PIL) imported successfully")
    except ImportError as e:
        print(f"❌ Failed to import Pillow: {e}")
        return False
    
    return True

def test_file_structure():
    """Test that required files exist."""
    required_files = [
        'auto_clicker.py',
        'build.py',
        'requirements.txt',
        'README.md',
        'LICENSE'
    ]
    
    missing_files = []
    for file in required_files:
        if not os.path.exists(file):
            missing_files.append(file)
    
    if missing_files:
        print(f"❌ Missing required files: {missing_files}")
        return False
    
    print("✅ All required files present")
    return True

def test_settings_template():
    """Test that we can create a basic settings template."""
    try:
        import json
        
        template_settings = {
            "hours": 0,
            "minutes": 0,
            "seconds": 1,
            "milliseconds": 0,
            "random_offset": False,
            "offset_range": 100,
            "mouse_button": "left",
            "click_type": "single",
            "position_mode": "current",
            "repeat_mode": "until_stopped",
            "repeat_count": 1,
            "keyboard_key": "space"
        }
        
        # Test JSON serialization
        json_str = json.dumps(template_settings, indent=2)
        parsed = json.loads(json_str)
        
        assert parsed == template_settings
        print("✅ Settings template creation successful")
        return True
        
    except Exception as e:
        print(f"❌ Settings template test failed: {e}")
        return False

class TestLazyAF(unittest.TestCase):
    """Unit tests for LazyAF components."""
    
    def test_imports(self):
        """Test that all imports work."""
        self.assertTrue(test_imports())
    
    def test_file_structure(self):
        """Test file structure."""
        self.assertTrue(test_file_structure())
    
    def test_settings_template(self):
        """Test settings template."""
        self.assertTrue(test_settings_template())
    
    @patch('pyautogui.click')
    def test_pyautogui_mock(self, mock_click):
        """Test that PyAutoGUI can be mocked (for testing)."""
        import pyautogui
        
        # Test that we can mock pyautogui.click
        pyautogui.click(100, 100)
        mock_click.assert_called_once_with(100, 100)
        
        print("✅ PyAutoGUI mocking works")
    
    def test_timing_calculation(self):
        """Test timing calculation logic."""
        def calculate_total_ms(hours, minutes, seconds, milliseconds):
            return (hours * 3600000 + 
                   minutes * 60000 + 
                   seconds * 1000 + 
                   milliseconds)
        
        # Test cases
        test_cases = [
            (0, 0, 1, 0, 1000),      # 1 second = 1000ms
            (0, 1, 0, 0, 60000),     # 1 minute = 60000ms
            (1, 0, 0, 0, 3600000),   # 1 hour = 3600000ms
            (0, 0, 0, 500, 500),     # 500ms = 500ms
            (0, 1, 30, 500, 90500),  # 1min 30.5sec = 90500ms
        ]
        
        for hours, minutes, seconds, ms, expected in test_cases:
            result = calculate_total_ms(hours, minutes, seconds, ms)
            self.assertEqual(result, expected)
        
        print("✅ Timing calculation tests passed")

def main():
    """Run all tests."""
    print("🚀 Starting LazyAF Installation Tests...")
    print("=" * 50)
    
    # Run basic tests
    tests_passed = 0
    total_tests = 3
    
    if test_imports():
        tests_passed += 1
    
    if test_file_structure():
        tests_passed += 1
    
    if test_settings_template():
        tests_passed += 1
    
    print("=" * 50)
    print(f"Basic Tests: {tests_passed}/{total_tests} passed")
    
    # Run unit tests
    print("\n🧪 Running Unit Tests...")
    test_suite = unittest.TestLoader().loadTestsFromTestCase(TestLazyAF)
    test_runner = unittest.TextTestRunner(verbosity=2)
    result = test_runner.run(test_suite)
    
    # Summary
    print("\n" + "=" * 50)
    if tests_passed == total_tests and result.wasSuccessful():
        print("🎉 All tests passed! LazyAF is ready to use.")
        return 0
    else:
        print("❌ Some tests failed. Please check the output above.")
        return 1

if __name__ == "__main__":
    sys.exit(main()) 