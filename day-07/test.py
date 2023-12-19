card_orders = ['J', '2', '3', '4', '5', '6', '7', '8', '9', 'T', 'Q', 'K', 'A']

test = {}

hand = 'J223Q'

type_score = 0
card_score = 0

# looping for each card_value
for val in range(len(card_orders)):
    card_count = 0
    # looping for each card
    for pos in range(len(hand)):
        if card_orders[val] == hand[pos]:
            test[card_orders[val]] = 1

            # card_count += 1
            # card_score += val*(10**((4-pos)*2))
print(test)