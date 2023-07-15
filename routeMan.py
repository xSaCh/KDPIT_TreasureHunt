import logging
import random as rand
from riddle import *

TOTAL_ROUTE = 3
TOTAL_TEAM = 6
routes = [[] for i in range(TOTAL_ROUTE)]

logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO,
)
logger = logging.getLogger(__name__)


def getRouteRand(grpName):
    i = rand.randint(0, 2)

    if all(len(i) >= TOTAL_TEAM / TOTAL_ROUTE for i in routes):
        logger.warning("Routes are full %s", routes)
        return

    while len(routes[i]) >= TOTAL_TEAM / TOTAL_ROUTE:
        i = rand.randint(0, 2)
    routes[i].append(grpName)

    logger.info("Routes: %s", routes)


def getRoute(grpName):
    if all(len(i) >= TOTAL_TEAM / TOTAL_ROUTE for i in routes):
        logger.warning("Routes are full %s", routes)
        return

    for r in routes:
        if len(r) < TOTAL_TEAM / TOTAL_ROUTE:
            r.append(grpName)
            break
    logger.info("Routes: %s", routes)


def getRiddle(grpName, level):
    r, grp = -1, -1
    for i in range(len(routes)):
        if routes[i].count(grpName):
            r = i
            grp = routes[i].index(grpName)

    k = list(RIDDLES.keys())[r]
    return RIDDLES[k][grp][level]
