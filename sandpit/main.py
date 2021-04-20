"""
NOTHING TO SEE HERE - MOVE ALONG

Created on 19 Dec 2020

@author: semuadmin
"""

from random import choice

TWATS = [
    "Bailey",
    "Buckland",
    "Cameron",
    "Drax",
    "Gove",
    "Hancock",
    "Johnson",
    "Raab",
    "Rees-Mogg",
    "Patel",
    "Thatcher",
    "Wallace",
    "Williamson",
]


class Classof2020:
    """
    classdocs
    """

    def __init__(self, **kwargs):
        """
        Constructor
        """

    def random_twat(self):
        """
        They can't think of a good word for them, but I can...
        """

        return choice(TWATS)
