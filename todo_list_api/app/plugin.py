from abc import ABC, abstractmethod
from importlib import import_module
from typing import Any, TypeVar

from todo_list_api.app.exceptions import PluginInitializationFailed, InvalidPluginType

PluginImplementation = TypeVar("PluginImplementation")


class Plugin(ABC):
    @classmethod
    @abstractmethod
    def get_class_reference(cls) -> str:
        """
        Get the class reference name of the plugin that needs to be installed.
        This class will dynamically be imported by calling the `initialize()` method.
        """
        pass

    @classmethod
    def initialize(cls, *args, **kwargs) -> PluginImplementation:
        class_name = cls.get_class_reference()
        obj = Plugin.init_class(class_name, *args, **kwargs)
        if not isinstance(obj, cls):
            raise InvalidPluginType(obj.__class__, cls)
        return obj

    @staticmethod
    def init_class(class_name: str, *args, **kwargs) -> Any:
        """
        Imports 'class_name' provided by name and initializes with arguments
        """
        error = PluginInitializationFailed(class_name, *args, **kwargs)
        try:
            class_attr = Plugin.import_class(class_name)
        except (ImportError, AttributeError, Exception):
            raise error
        try:
            return class_attr(*args, **kwargs)
        except TypeError:
            raise error

    @staticmethod
    def import_class(full_class_name: str):
        """
        Imports 'full_class_name' based on its name
        :param full_class_name: The class absolute name
        :return: The class itself
        """
        module_path, class_name = full_class_name.rsplit(".", 1)
        module = import_module(module_path)
        clazz_attr = getattr(module, class_name)
        return clazz_attr
