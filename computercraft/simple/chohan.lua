print('Cho-Han')

dice1 = math.random(1, 6)
dice2 = math.random(1, 6)

print('The dealer swirls the cup and you hear')
print('rattle of dice. The dealer slams the cup')
print('on the floor, still covering the dice')
print('and asks for your bet.')
print()
print('    CHO (even) or HAN (odd)?')

bet = string.upper(read())

print('The dealer lifts the cup to reveal:')
print('    ' .. dice1 .. ' - ' .. dice2)

rollIsEven = (dice1 + dice2) % 2 == 0
correctBet = ''
if rollIsEven then
  correctBet = 'CHO'
else
  correctBet = 'HAN'
end

if bet == correctBet then
  print('You won!')
else
  print('You lost!')
end



