



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

def teamName_by_yearFounded(matches: List[str]) -> List[str]:

    year = int(matches[0])
    result = []
    for teams in team_db:
        if get_yearFounded(teams) == year:
            result.append(get_teamName(teams))
    return result










def bye_action(dummy: List[str]) -> None:
    raise KeyboardInterrupt





















pa_list: List[Tuple[List[str], Callable[[List[str]], List[Any]]]] = [
    (str.split("what team was founded in _"), teamName_by_yearFounded),
    (str.split("who plays on the %"), players_by_teamName),
    (str.split("who was the coach of %"), coach_by_teamName),
    (str.split("what movies were directed by %"), title_by_director),
    (str.split("who acted in %"), actors_by_title),
    (str.split("when was % made"), year_by_title),
    (str.split("what years did % direct"), year_by_director),
    (str.split("in what movies did % appear"), title_by_actor),
    (["bye"], bye_action),
]

def search_pa_list(src: List[str]) -> List[str]:

    for pat, act in pa_list:   
        mat = match(pat, src)

        if mat is not None:
            answer = act(mat)
            return answer if answer else ["No answers"]
    return ["I don't understand"]


def query_loop() -> None:
    """The simple query loop. The try/except structure is to catch Ctrl-C or Ctrl-D
    characters and exit gracefully.
    """
    print("Welcome to the basketball database!\n")
    while True:
        try:
            print()
            query = input("Your query? ").replace("?", "").lower().split()
            answers = search_pa_list(query)
            for ans in answers:
                print(ans)

        except (KeyboardInterrupt, EOFError):
            break

    print("\nSo long!\n")