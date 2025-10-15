



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
    for teams in team_db:
        Team = get_teamName(teams)
        if Team == teamName:
            result = get_topFivePlayers(teams)
    return result

def coach_by_teamName(match: List[str]) -> list[str]:
    result = []
    teamName = match[0]
    for teams in team_db:
        team = get_teamName(teams)
        if team == teamName:
            result.append(get_coach(teams))
    return result
3
def teamName_by_coach(match: List[str]) -> list[str]:
    result = []
    coachName = match[0]
    for teams in team_db:
        coachname = get_coach(teams)
        if coachname == coachName:
            result.append(get_teamName(teams))
    return result

def teamName_by_yearsBefore(match: List[str]) -> list[str]:
    result = []
    year = int(match[0])
    for teams in team_db:
        Year = get_yearFounded(teams)
        if year > Year:
            result.append(get_teamName(teams))
    return result 

def teamName_by_yearsAfter(match: List[str]) -> list[str]:
    result = []
    year = int(match[0])
    for teams in team_db:
        Year = get_yearFounded(teams)
        if year < Year:
            result.append(get_teamName(teams))
    return result 

def teamName_by_yearsBetween(match: List[str]) -> list[str]:
    result = []
    yearone = int(match[0])
    yeartwo = int(match[1])
    for teams in team_db:
        Year = get_yearFounded(teams)
        if yearone<= Year <= yeartwo:
            result.append(get_teamName(teams))
    return result 
        
def teamName_by_yearFounded(match: List[str]) -> List[str]:

    year = int(match[0])
    result = []
    for teams in team_db:
        Year = get_yearFounded(teams)
        if Year == year:
            result.append(get_teamName(teams))
    return result

def teamName_by_player(match: List[str]) -> list[str]:
    result = []
    playerpicked = match[0]
    for teams in team_db:
        players = get_topFivePlayers(teams)
        for topFivePlayers in players:
            if playerpicked in players:
                result.append(get_teamName(teams))
                break
    return result 




def bye_action(dummy: List[str]) -> None:
    raise KeyboardInterrupt



pa_list: List[Tuple[List[str], Callable[[List[str]], List[Any]]]] = [
    (str.split("what team was founded in _"), teamName_by_yearFounded),
    (str.split("who plays on the %"), players_by_teamName),
    (str.split("who is the coach of %"), coach_by_teamName),
    (str.split("what teams were founded between the years %"),  teamName_by_yearsBetween),
    (str.split("what teams were founded after the year %"), teamName_by_yearsAfter),
    (str.split("what teams were founded before the year %"), teamName_by_yearsBefore),
    (str.split("what team does % coach"), teamName_by_coach),
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


assert isinstance(players_by_teamName(["los angeles clippers"]), list), "players_by_teamName not returning a list"
assert sorted(players_by_teamName(["los angeles clippers"])) == sorted(["kawhi leonard", "james harden", "norman powell", "ivica zubac", "derrick jones jr"]), "failed players_by_teamName test"



assert isinstance(coach_by_teamName(["new york knics"]), list), "coach_by_teamName not returning a list"
assert sorted(coach_by_teamName(["new york knics"])) == sorted(["tom thinbadeau"]), "failed coach_by_teamName test"



assert isinstance(teamName_by_coach(["joe muzzulla"]), list), "teamName_by_coach not returning a list"
assert sorted(teamName_by_coach(["joe muzzulla"])) == sorted(["boston celtics"]), "failed teamName_by_coach test"


assert isinstance(teamName_by_yearsBefore(["1950"]), list), "teamName_by_yearsBefore not returning a list"
assert sorted(teamName_by_yearsBefore(["1950"])) == sorted(["los angelos lakers", "boston celtics", "new york knics"]), "failed teamName_by_yearsBefore test"


assert isinstance(teamName_by_yearsAfter(["1990"]), list), "teamName_by_yearsAfter not returning a list"
assert sorted(teamName_by_yearsAfter(["1990"])) == sorted(["oklahoma city thunder"]), "failed teamName_by_yearsAfter test"


assert isinstance(teamName_by_yearsBetween(["1970", "1980"]), list), "teamName_by_yearsBetween not returning a list"
assert sorted(teamName_by_yearsBetween(["1970", "1980"])) == sorted(["clevand cavaliers", "los angeles clippers"]), "failed teamName_by_yearsBetween test"


assert isinstance(teamName_by_yearFounded(["1967"]), list), "teamName_by_yearFounded not returning a list"
assert sorted(teamName_by_yearFounded(["1967"])) == sorted(["houston rockets","denver nuggets"]), "failed teamName_by_yearFounded test"

assert isinstance(teamName_by_player(["rudy gobert"]), list), "teamName_by_player not returning a list"
assert sorted(teamName_by_player(["rudy gobert"])) == sorted(["minnesota timberwolves"]), "failed teamName_by_player test"

assert sorted(search_pa_list(["what", "team", "does", "mark daignaeult", "coach"])) == sorted(["oklahoma city thunder"]), "Failed PA search"

assert sorted(search_pa_list(["who", "is", "the", "coach", "of", "clevand cavaliers"])) == sorted(["kenny atkinson"]), "Failed 22PA search"

print("tests passed")






































































        