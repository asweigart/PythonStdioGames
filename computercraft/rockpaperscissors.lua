--[[Rock, Paper, Scissors
By Al Sweigart al@inventwithpython.com
The classic hand game of luck.
]]

print('Rock, Paper, Scissors by Al Sweigart')
print()
print('- Rock beats scissors.')
print('- Paper beats rocks.')
print('- Scissors beats paper.')

-- These variables keep track of the number of
-- wins, losses, and ties:
local wins = 0
local losses = 0
local ties = 0

while true do -- main game loop
  local playerMove
  local computerMove
  while true do -- Ask player for their move
    print(wins .. ' Wins, ' .. losses .. ' Losses, ' .. ties .. ' Ties')
    print('Enter your move.')
    print('(R)ock (P)aper (S)cissors (Q)uit')
    playerMove = string.upper(read())
    if playerMove == 'Q' then
      print('Thanks for playing!')
      error()
    end

    if playerMove == 'R' or playerMove == 'P' or playerMove == 'S' then
      break
    else
      print('Type one of R, P, S, or Q.')
    end
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
  local randomNumber = math.random(1, 3)
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
    ties = ties + 1
  elseif playerMove == 'ROCK' and computerMove == 'SCISSORS' then
    print('You win!')
    wins = wins + 1
  elseif playerMove == 'PAPER' and computerMove == 'ROCK' then
    print('You win!')
    wins = wins + 1
  elseif playerMove == 'SCISSORS' and computerMove == 'PAPER' then
    print('You win!')
    wins = wins + 1
  elseif playerMove == 'ROCK' and computerMove == 'PAPER' then
    print('You lose!')
    losses = losses + 1
  elseif playerMove == 'PAPER' and computerMove == 'SCISSORS' then
    print('You lose!')
    losses = losses + 1
  elseif playerMove == 'SCISSORS' and computerMove == 'ROCK' then
    print('You lose!')
    losses = losses + 1
  end
end
