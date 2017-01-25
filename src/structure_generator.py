"""Structure generator module"""
import os
import os.path

class Logger(object):
    """Simple logger class."""

    def __init__(self):
        pass

    def log(self, message):
        """Prints the message to stdout."""
        print(message)


class StructureGenerator(object):
    """Generates folder structures."""

    def __init__(self, logger):
        self.logger = logger

    def generate_structure(self, startfrom, structure):
        """Generates folder structure."""
        base_path = startfrom
        dir_separator = "/"
        if not os.path.exists(base_path):
            self.logger.log("The startfrom (" + base_path + ") path does not exist!")
            raise FileExistsError("Base path does not exist (" + base_path + ")")

        for item in structure:
            if not base_path.endswith(dir_separator) and not item.startswith(dir_separator):
                path = base_path + dir_separator
            else:
                path = base_path
            path = path + item
            if not os.path.exists(path):
                self.logger.log("Generating path: " + path)
                os.makedirs(path)
