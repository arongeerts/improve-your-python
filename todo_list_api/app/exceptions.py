from typing import Type


class HTTPException(Exception):
    def __init__(self, status_code: int, reason: str):
        self.status_code = status_code
        self.reason = reason


class PluginInitializationFailed(Exception):
    def __init__(self, class_name: str, *args, **kwargs):
        self.class_name = class_name
        self.args = args
        self.kwargs = kwargs


class InvalidPluginType(Exception):
    def __init__(self, got_class: Type, expected_class: Type):
        self.got_class = got_class
        self.expected_class = expected_class


class ListNotFoundException(HTTPException):
    def __init__(self, name: str):
        super().__init__(status_code=404, reason=f"No list found with name '{name}'")
