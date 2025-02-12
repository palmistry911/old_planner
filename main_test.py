import unittest
from main import TaskPlanner

class TestTaskPlanner(unittest.TestCase):

    def setUp(self):
        self.planner = TaskPlanner()

    def test_add_task_valid(self):
        result = self.planner.add_task("Test Task")
        self.assertTrue(result)
        self.assertEqual(len(self.planner.tasks), 1)

    def test_add_task_invalid(self):
        result = self.planner.add_task("A")
        self.assertFalse(result)
        self.assertEqual(len(self.planner.tasks), 0)

    def test_mark_task_completed(self):
        self.planner.add_task("Test Task")
        self.planner.mark_task_completed(0)
        self.assertTrue(self.planner.tasks[0].completed)

    def test_mark_task_completed_already_done(self):
        self.planner.add_task("Test Task")
        self.planner.mark_task_completed(0)
        self.planner.mark_task_completed(0)
        self.assertTrue(self.planner.tasks[0].completed)

    def test_remove_task(self):
        self.planner.add_task("Test Task")
        self.planner.remove_task(0)
        self.assertEqual(len(self.planner.tasks), 0)

    def test_remove_task_invalid_index(self):
        self.planner.add_task("Test Task")
        self.planner.remove_task(10)
        self.assertEqual(len(self.planner.tasks), 1)

if __name__ == "__main__":
    unittest.main()
