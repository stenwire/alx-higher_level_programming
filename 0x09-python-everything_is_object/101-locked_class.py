#!/usr/bin/python3
"""A Locked Class"""


class LockedClass:
    """A locked class is a class that only lets 
    the user dynamically use the preset instance"""
    __slots__ = ('first_name')
