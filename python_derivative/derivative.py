from array import ArrayType
import array
import types

class Derivative:

    def __init__(
        self,
        handlers: dict = {},
        default: types.FunctionType = object,
        drop_response: str = ""
    ) -> None:
        self.handlers = handlers
        self.default = default
        self.drop_response = drop_response

    def SetDropResponse(self, response: str):
        self.drop_response = response
        return self

    def IncludeDefaultImplementation(self, handler: types.FunctionType, exempt = []):
        assert(isinstance(handler, types.FunctionType)); "The paramater 'handler' must be a function object"
        self.default = handler
        return self

    def IncludePathImplementation(self, path: str, handler: types.FunctionType, exempt = []):
        assert (isinstance(path, str)); "The paramater 'path' must be an object of type str"
        assert(isinstance(handler, types.FunctionType)); "The paramater 'handler' must be a function object"
        self.paths.append(path); self.handlers[path] = handler
        return self


