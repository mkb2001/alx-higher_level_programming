#!usr/bin/python3
def lookup(obj):
    """
        Return the list of available attributes and methods of an object.

        Args:
        - obj: Any Python object

        Returns:
        - List of strings representing attributes and methods
        """
    return dir(obj)
