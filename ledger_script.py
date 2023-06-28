player_ledger = {
    'Bi Tian Yuan': 227.59,
    'william': 173.27,
    'Kevin': 137.35,
    'Dean': 130.08,
    'elliot': 79.01,
    'jimming': 70.75,
    'Eric': 66.25,
    'Cole': 60.80,
    'Gilly': 32.08,
    'Stefano': -4.50,
    'CJ': -21.63,
    'kangdaniel': -66.89,
    'Vinay': -100,
    'Ryan padnis': -146.09,
    'Sai': -188.07,
    'Peter': -200,
    'Zach': -250.00
}

assert(sum(player_ledger.values()) < 0.001)
winners = sorted(((round(v, 2), k) for k, v in player_ledger.items() if v > 0), reverse=True)
losers = sorted(((round(abs(v), 2), k) for k, v in player_ledger.items() if v < 0), reverse=True)

payments = []
for loser_amount, loser in losers:
    while loser_amount > 0 and winners:
        winner_amount, winner = winners[0]
        payment = round(min(loser_amount, winner_amount), 2)
        payments.append((loser, winner, payment))
        loser_amount = round(loser_amount - payment, 2)
        winner_amount = round(winner_amount - payment, 2)
        if winner_amount == 0:
            winners.pop(0)
        else:
            winners[0] = (winner_amount, winner)

for payment in payments:
    loser, winner, amount = payment
    print(f"{loser} pays {winner} {round(amount, 2)}")