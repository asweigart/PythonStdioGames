--[[Rock, Paper, Scissors
By Al Sweigart al@inventwithpython.com
The classic hand game of luck.
]]

print('Rock, Paper, Scissors by Al Sweigart')
print()
print('- Rock beats scissors.')
print('- Paper beats rocks.')
print('- Scissors beats paper.')

print('Enter your move.')
print('(R)ock (P)aper (S)cissors (Q)uit')
playerMove = string.upper(read())
if playerMove == 'Q' then
  print('Thanks for playing!')
  error()
end

-- Display what the player chose:
if playerMove == 'R' then
  print('ROCK versus...')
  playerMove = 'ROCK'
elseif playerMove == 'P' then
  print('PAPER versus...')
  playerMove = 'PAPER'
elseif playerMove == 'S' then
  print('SCISSORS versus...')
  playerMove = 'SCISSORS'
end

-- Count to three with dramatic pauses:
os.sleep(0.5)
print('1...')
os.sleep(0.25)
print('2...')
os.sleep(0.25)
print('3...')
os.sleep(0.25)

-- Display what the computer chose:
randomNumber = math.random(1, 3)
if randomNumber == 1 then
  computerMove = 'ROCK'
elseif randomNumber == 2 then
  computerMove = 'PAPER'
elseif randomNumber == 3 then
  computerMove = 'SCISSORS'
end
print(computerMove)
os.sleep(0.5)

-- Display and record the win/loss/tie:
if playerMove == computerMove then
  print('It\'s a tie!')
elseif playerMove == 'ROCK' and computerMove == 'SCISSORS' then
  print('You win!')
elseif playerMove == 'PAPER' and computerMove == 'ROCK' then
  print('You win!')
elseif playerMove == 'SCISSORS' and computerMove == 'PAPER' then
  print('You win!')
else
  print('You lose!')
end

