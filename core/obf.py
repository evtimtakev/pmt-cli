from project import *
from issue import *


class ObjectFactory:  # Factory that create class instances

    @staticmethod
    def get_instance_of(object_type, params):  # Create a instance of core classes
        """Create instance of core classes"""
        if object_type is "project":
            return Project(params["name"], params["project_version"])
        elif object_type is "issue":
            return Issue(params['type'], params['status'], params['title'], params['description'], params['project_id'])
        else:
            empty_typle = {}
            return empty_typle
