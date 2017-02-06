""""""
import yaml

class StructureConfig(object):
    """Holds structure configuration nodes."""

    def __init__(self, conf_path):
        with open(conf_path, 'r') as stream:
            data = yaml.load(stream)
            self.nodes = data['hierarchy']
        self.depth_limit = 5

    def __load(self, conf_path):
        with open(conf_path, 'r') as stream:
            data = yaml.load(stream)
        return data['hierarchy']

    def get_paths(self):
        """Get the node paths as a list."""
        paths_list = []
        self.__get_paths(paths_list, self.nodes, 0, "/")
        return paths_list

    def __get_paths(self, output, nodes, depth, parent):
        if isinstance(nodes, dict):
            for key, value in nodes.items():
                path = self.__create_path_string(parent, key)
                output.append(path)
                if isinstance(value, list) or isinstance(value, dict):
                    self.__get_paths(output, value, depth+1, path)
                else:
                    return
        elif isinstance(nodes, list):
            for item in nodes:
                if isinstance(item, list) or isinstance(item, dict):
                    self.__get_paths(output, item, depth+1, parent)


    def __create_path_string(self, parent, child):
        if parent == "":
            path = "/" + child
        elif parent == "/":
            path = parent + child
        else:
            path = parent + "/" + child
        return path



