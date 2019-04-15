import itertools
import random


def main():
    deck = deck_object()
    puzzle = generate_n_solution_puzzle(0, deck)
    print("Puzzle:")
    print_cards(puzzle)
    solution_sets = find_all_solutions(puzzle)
    print("Solutions:")
    for solution in solution_sets:
        print_cards(solution)




class card_object:
    def __init__(self, number, shading, color, shape):
        self.features = {
            "number": number,
            "shading": shading,
            "color": color,
            "shape": shape
        }

    def __str__(self):
        return(str(self.features))


class deck_object:
    def __init__(self):
        possible_features = {
            "number": [
                "one",
                "two",
                "three"
            ],
            "shading": [
                "solid",
                "striped",
                "outlined"
            ],
            "color": [
                "green",
                "purple",
                "red"
            ],
            "shape": [
                "oval",
                "diamond",
                "squiggle"
            ]
        }
        self.cards = []
        all_combinations = itertools.product(*possible_features.values())
        for combo in all_combinations:
            self.cards.append(card_object(*combo))
        print(str(len(self.cards)) + " cards created.")



def check_solution(card_set):

    features_seen = {
        "number": {},
        "shading": {},
        "color": {},
        "shape":{}
    }
    for card in card_set:
        for f in features_seen.keys():
            features_seen[f][card.features[f]] = True
    errors = []
    for f in features_seen:
        if len(features_seen[f]) == 2: #should be only 1 or 3 features for a true set
            error_message = f + " error: " + str(tuple(features_seen[f].keys()))
            errors.append(error_message)
    if len(errors) > 0:
        return errors
    else:
        return True


def find_all_solutions(all_cards):
    all_possible_sets = itertools.combinations(all_cards, 3)
    solution_sets = []
    for possible_set in all_possible_sets:
        answer = check_solution(possible_set)
        if answer == True:
            solution_sets.append(possible_set)
    return solution_sets


def generate_puzzle(deck):
    puzzle = []
    for c in random.sample(range(len(deck.cards)), 12):
        puzzle.append(deck.cards[c])
    return puzzle


def generate_n_solution_puzzle(n, deck):
    num_solutions = -1
    while num_solutions != n:
        puzzle = generate_puzzle(deck)
        num_solutions = len(find_all_solutions(puzzle))
    return puzzle



def print_cards(card_list):
    print("------------")
    for card in card_list:
        print(card)
    print("------------")



if __name__ == "__main__":
    main()
