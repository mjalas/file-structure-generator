""""""
import unittest
import os
import os.path
from src.structure_generator import StructureGenerator, Logger

class TestStructureGenerator(unittest.TestCase):
    """File structure generator test cases."""

    def test_generate_structure(self):
        """Structure generation test case"""
        structures = [
            "parent",
            "parent/child1",
            "parent/child1/grandchild",
            "parent/child2",
        ]

        logger = Logger()
        generator = StructureGenerator(logger)
        generator.generate_structure(os.getcwd(), structures)

        for item in structures:
            test_path = os.getcwd() + "/" + item
            self.assertTrue(os.path.exists(test_path))
        remove_structures = list(reversed(structures))
        for item in remove_structures:
            test_path = os.getcwd() + "/" + item
            os.rmdir(test_path)
