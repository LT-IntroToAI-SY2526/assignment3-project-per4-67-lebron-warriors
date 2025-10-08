



from teams import team_db
from match import match
from typing import List, Tuple, Callable, Any


def get_teamName(teams: Tuple[str, int, str, List[str]]) -> str:
    return teams[0]


def get_coach(teams: Tuple[str, int, str, List[str]]) -> str:
    return teams[2]


def get_yearFounded(teams: Tuple[str, int, str, List[str]]) -> int:
    return teams[1]


def get_topFivePlayers(teams: Tuple[str, int, str, List[str]]) -> List[str]:
    return teams[3]


def players_by_teamName(match: List[str]) -> List[str]:
    result = []
    teamName = match[0]
    for team in team_db:
        Team = get_teamName(team)
        if Team == teamName:
            result = get_topFivePlayers()
    return result

def coach_by_teamName(match: List[str]) -> list[str]:
    result = []
    teamName = match[0]
    for team in team_db:
        team = get_teamName(team)
        if team == teamName:
            result.append(get_coach(team))
    return result

def teamName_by_coach(match: List[str]) -> list[str]:
    result = []
    coachName = match[0]
    for team in team_db:
        coachname = get_coach()
        if coachname == coachName:
            result.append(get_teamName(team))
    return result

def teamName_by_yearsBefore(match: List[str]) -> list[str]:
    result = []
    year = match[0]
    for team in team_db:
        Year = get_yearFounded()
        if year > Year:
            result.append(get_teamName())
    return result 

def teamName_by_yearsAfter(match: List[str]) -> list[str]:
    result = []
    year = match[0]
    for team in team_db:
        Year = get_yearFounded()
        if year < Year:
            result.append(get_teamName())
    return result 

def teamName_by_yearsBetween(match: List[str]) -> list[str]:
    result = []
    yearone = match[0]
    yeartwo = match[1]
    for team in team_db:
        Year = get_yearFounded()
        if yearone<= Year <= yeartwo:
            result.append(get_teamName())
    return result 
        