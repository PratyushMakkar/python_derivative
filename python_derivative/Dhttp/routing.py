import array
from multiprocessing.dummy import Array
from requests import Request
from derivative import Derivative
import types

class URLTree:

    def __init__(self, node_data: str = "", children: array = []):
        self.node_data = node_data
        self.children = children
        

    def SetNodeData(self, data: str):
        self.node_data = data
        return self
    
    def AddNodeToChildren(self, node_data: str):
        node = URLTree(node_data=node_data)
        self.children.append(node)
        return node

    def SetChildrenFromArray(self, resource_array: array):
        prefixToURLMapping = {}

        for path in resource_array:
            print(resource_array)
            prefix = path[0]
            if prefix[0] == '{':
                prefix = '{}'
            path.pop(0)
            if prefix in prefixToURLMapping:
                prefixToURLMapping[prefix].append(path)
            else:
                prefixToURLMapping[prefix] = [path]
        print(prefixToURLMapping)
        for prefix in prefixToURLMapping:
            node = self.AddNodeToChildren(prefix)
            a = prefixToURLMapping[path]
            print(a)
            if (a):
                node.SetChildrenFromArray(prefixToURLMapping[prefix])

        return self
    
    @staticmethod
    def CreateTreeFromArray(url_paths: array):
        tree = URLTree()
        resource_id_array = []

        for path in url_paths:
            path_array = path.split("/")
            path_array.pop(0)
            resource_id_array.append(path_array)
            
        return tree.SetChildrenFromArray(resource_id_array)
        

def _ParseTree(request_path: str, url_tree: URLTree):
    pass

def MatchRequestToHandler(request_path: str, derivative: Derivative) -> types.FunctionType: 
    path_array = []
    for key in derivative.handlers:
        path_array.append(key)

    url_tree = URLTree().CreateTreeFromArray()
    closest_match : str = _ParseTree(request_path, path_array)
    with derivative[path_array] as handler:
        return handler
