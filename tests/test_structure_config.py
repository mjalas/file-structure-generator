""""""
import unittest
import os
from src.structure_config import StructureConfig

class TestStructureConfig(unittest.TestCase):
    """Stucture configuration tests."""

    def test_parse(self):
        """Tests parsing of example_structure.yml to list of paths."""
        conf_file = os.getcwd() + "/tests/testconfigs/example_structure.yml"
        config = StructureConfig(conf_file)
        paths = config.get_paths()
        expected = ["/parent",
                    "/parent/child1",
                    "/parent/child1/grandchild1",
                    "/parent/child1/grandchild2",
                    "/parent/child2",
                    "/parent/child2/grandchild3",
                    "/parent/child3",
                    "/parent/child3/grandchild4",
                    "/parent/child3/grandchild5"]
        for i in range(0, len(paths)):
            self.assertEqual(expected[i], paths[i])
