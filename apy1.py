



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
        team = get_teamName(team)
        if team == teamName:
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
