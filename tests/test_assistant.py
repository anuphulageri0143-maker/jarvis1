"""
Tests for the main Jarvis Assistant class
"""

import unittest
from jarvis.assistant import JarvisAssistant


class TestJarvisAssistant(unittest.TestCase):
    """Test cases for JarvisAssistant class."""

    def setUp(self):
        """Set up test fixtures."""
        self.jarvis = JarvisAssistant()

    def test_initialization(self):
        """Test assistant initialization."""
        self.assertIsNotNone(self.jarvis)
        self.assertFalse(self.jarvis.is_running)

    def test_process_command_greeting(self):
        """Test processing a greeting command."""
        response = self.jarvis.process_command("hello")
        self.assertIsNotNone(response)
        self.assertIsInstance(response, str)
        self.assertGreater(len(response), 0)

    def test_process_command_time(self):
        """Test processing a time query."""
        response = self.jarvis.process_command("what time is it")
        self.assertIsNotNone(response)
        self.assertIn("time", response.lower())

    def test_register_custom_task(self):
        """Test registering a custom task."""
        def custom_task(name):
            return f"Hello, {name}!"
        
        self.jarvis.register_task("greet", custom_task)
        self.assertIn("greet", self.jarvis.custom_tasks)

    def test_execute_custom_task(self):
        """Test executing a custom task."""
        def add_numbers(a, b):
            return a + b
        
        self.jarvis.register_task("add", add_numbers)
        result = self.jarvis.execute_task("add", 2, 3)
        self.assertEqual(result, 5)

    def test_status(self):
        """Test getting assistant status."""
        status = self.jarvis.get_status()
        self.assertIn("running", status)
        self.assertIn("version", status)
        self.assertIsInstance(status["custom_tasks"], list)


if __name__ == '__main__':
    unittest.main()
