import datetime


def current_time(format):
    t = datetime.datetime.now()
    return t.strftime(format)


def save_to_file(content, file, team_a, team_b):
    for element in content:
        file.write("[{}-{}] Point for {}! {}\n".format(element["score"]["team_a"], element["score"]["team_b"], element["team"], element["type"]))


def add_record(team, score_team_a, score_team_b, ptype):
    return {"team": team, "score": {"team_a": score_team_a, "team_b": score_team_b}, "type": ptype}


def choose_type():
    print("Choose type:\n[1] - attack \n[2] - block\n[3] - ace\n[4] - opponent error")
    ptype = input("Type: ")

    while True:
        if ptype == "1":
            return "Attack"
        elif ptype == "2":
            return "Block"
        elif ptype == "3":
            return "Ace"
        elif ptype == "4":
            return "OpponentError"
        else:
            print("Incorrect Input")


def main():
    team_a = "mFinanse"
    team_b = "BoatSystems"
    setno = 3
    tmp = []
    score = {team_a: 0, team_b: 0}

    f = open("matchLog_{}_{}_{}_set{}.txt".format(team_a, team_b, current_time("%d-%m-%Y %H-%M-%S"), setno), "a")

    while True:

        print("[1] - log action \n[2] - show score\n[3] - save and exit")
        action = input("Option: ")

        if action == "1":
            print("Point for: [1] - {}, [2] - {}".format(team_a, team_b))
            point = input("Team: ")
            if point == "1":
                score[team_a] += 1
                ptype = choose_type()
                tmp.append(add_record(team_a, score[team_a], score[team_b], ptype))
            elif point == "2":
                score[team_b] += 1
                ptype = choose_type()
                tmp.append(add_record(team_b, score[team_a], score[team_b], ptype))
            else:
                print("Incorrect input!")

        elif str(action) == "2":
            print("Score: {} {} - {} {}".format(team_a, score[team_a], team_b, score[team_b]))

        elif str(action) == "3":
            save_to_file(tmp, f, team_a, team_b)
            print("End of the session")
            break

        else:
            print("Incorrect input!")

    f.close()


main()