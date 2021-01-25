--[[Cho-Han by Al Sweigart al@inventwithpython.com
The traditional Japanese dice game of even-odd.
]]

local JPN_NUMS = {[1]='ICHI', [2]='NI', [3]='SAN',
  [4]='SHI', [5]= 'GO', [6]='ROKU'}

print('Cho-Han by Al Sweigart al@inventwithpython.com')
print()
print('In this traditional Japanese dice game, two dice')
print('are rolled and the player must guess if the')
print('total is even (cho) or odd (han).')

local purse = 5000
while true do
  -- Place your bet:
  print('You have ' .. purse .. ' mon.')
  print('How much do you bet? (or QUIT)')
  while true do
    pot = read()
    if string.upper(pot) == 'QUIT' then
      error()
    elseif tonumber(pot) == nil then
      print('Please enter a number.')
    elseif tonumber(pot) > purse then
      print('You do not have enough money.')
    else
      -- This is a valid bet.
      pot = tonumber(pot)
      break
    end
  end

  local dice1 = math.random(1, 6)
  local dice2 = math.random(1, 6)

  print('The dealer swirls the cup and you hear')
  print('rattle of dice. The dealer slams the cup')
  print('on the floor, still covering the dice')
  print('and asks for your bet.')
  print()
  print('    CHO (even) or HAN (odd)?')

  -- Let the player bet cho or han:
  local bet = ''
  while true do
    bet = string.upper(read())
    if bet ~= 'CHO' and bet ~= 'HAN' then
      print('Please enter either "CHO" or "HAN".')
    else
      break
    end
  end

  -- Reveal the dice results:
  print('The dealer lifts the cup to reveal:')
  print('  ' .. JPN_NUMS[dice1] .. ' - ' .. JPN_NUMS[dice2])
  print('    ' .. dice1 .. ' - ' .. dice2)

  -- Determine if the player won:

  local rollIsEven = (dice1 + dice2) % 2 == 0
  local correctBet = ''
  if rollIsEven then
    correctBet = 'CHO'
  else
    correctBet = 'HAN'
  end

  local playerWon = bet == correctBet

  -- Display the bet results:
  if playerWon then
    print('You won! You take ' .. pot .. ' mon.')
    purse = purse + pot
    print('The house collects a ' .. math.floor(pot / 10) .. ' mon fee.')
    purse = purse - math.floor(pot / 10)
  else
    purse = purse - pot
    print('You lost!')
  end

  -- Check if the player has run out of money:
  if purse == 0 then
    print('You have run out of money!')
    print('Thanks for playing!')
    error()
  end
end


