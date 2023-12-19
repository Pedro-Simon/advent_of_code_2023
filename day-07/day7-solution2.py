import re

class PokerClassifier():

    def __init__(self, file_name):
        file = open(file_name, "r")
        self.hands_bids = file.readlines()
        
        self.card_orders = ['J', '2', '3', '4', '5', '6', '7', '8', '9', 'T', 'Q', 'K', 'A']

    def classify_cards(self, hand):
        type_list = []
        card_score = 0
        joker_count = 0
        # looping for each card_value
        for val in range(len(self.card_orders)):
            card_count = 0
            # looping for each card
            for pos in range(len(hand)):
                if self.card_orders[val] == hand[pos]:
                    card_score += val*(10**((4-pos)*2))

                    if hand[pos] == 'J':
                        joker_count += 1
                    else:
                        card_count += 1                    
            type_list.append(card_count)

        type_list = sorted(type_list, reverse=True)
        type_list[0] += joker_count

        type_score = sum([x**2 for x in type_list])

        # print(f'hand: {hand} got type_score of {type_score} and card_score of {card_score}')
        return type_score*10**(5*2)+card_score

    def get_ranks(self):
        list_bids = []
        list_scores = []
        list_hands = []
        for hand_bid in self.hands_bids:
            hand = hand_bid.split(' ')[0].strip()
            bid = int(hand_bid.split(' ')[1].strip())
            list_scores.append(self.classify_cards(hand))
            list_bids.append(bid)
            list_hands.append(hand)

        # Gets the ranks for each hand and multiplies by its bid
        sorted_index = [sorted(list_scores).index(x)+1 for x in list_scores]
        result = list(map(lambda x, y: x * y, sorted_index, list_bids))

        return sum(result)

if __name__ == '__main__':
    game = PokerClassifier('input.txt')
    print(game.get_ranks())
