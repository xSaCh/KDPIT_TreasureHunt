import logging
import random as rand
from riddle import *

TOTAL_TEAM = 6
TOTAL_RIDDLES = 6
teams = ["" for i in range(TOTAL_TEAM)]

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


def setRoute(grpName):
    global teams
    if all(len(i) > 0 for i in teams):
        logger.warning("Routes are full %s", teams)
        return

    for r in range(len(teams)):
        if len(teams[r]) == 0:
            teams[r] = grpName
            break
    logger.info("Routes: %s", teams)


def getRiddle(teamName, level, code):
    tInd = teams.index(teamName)

    tn = codeToTeam(code)

    if tn != str(f"{tInd+1}{level}"):
        return -1

    return RIDDLES[tInd][level]
