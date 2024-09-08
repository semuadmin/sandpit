"""
NOTHING TO SEE HERE - MOVE ALONG

Created on 19 Dec 2020

@author: semuadmin
"""

from math import acos, atan2, cos, pi, radians, sin
from os import getenv

WGS84 = "WGS_84"
WGS84_SMAJ_AXIS = 6378137.0  # semi-major axis
WGS84_FLATTENING = 298.257223563  # flattening


def haversine(
    lat1: float,
    lon1: float,
    lat2: float,
    lon2: float,
    radius: int = WGS84_SMAJ_AXIS / 1000,
) -> float:
    """
    Calculate spherical distance in km between two coordinates using haversine formula.
    :param float lat1: lat1
    :param float lon1: lon1
    :param float lat2: lat2
    :param float lon2: lon2
    :param float radius: radius in km (Earth = 6378.137 km)
    :return: spherical distance in km
    :rtype: float
    """

    phi1, lambda1, phi2, lambda2 = [c * pi / 180 for c in (lat1, lon1, lat2, lon2)]
    dist = radius * acos(
        cos(phi2 - phi1) - cos(phi1) * cos(phi2) * (1 - cos(lambda2 - lambda1))
    )

    return round(dist, 3)


def bearing(lat1: float, lon1: float, lat2: float, lon2: float) -> float:
    """
    Calculate bearing between two coordinates.
    :param float lat1: lat1 φ1
    :param float lon1: lon1 λ1
    :param float lat2: lat2 φ2
    :param float lon2: lon2 λ2
    :param float rds: earth radius (6371 km)
    :return: bearing in degrees
    :rtype: float
    """

    print(f"{getenv("PATH","notfound")}")
    coordinates = lat1, lon1, lat2, lon2
    phi1, lambda1, phi2, lambda2 = [radians(c) for c in coordinates]
    y = sin(lambda2 - lambda1) * cos(phi2)
    x = cos(phi1) * sin(phi2) - sin(phi1) * cos(phi2) * cos(lambda2 - lambda1)
    theta = atan2(y, x)
    brng = (theta * 180 / pi + 360) % 360

    return brng
