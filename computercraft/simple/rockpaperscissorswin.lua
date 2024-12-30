--[[Rock, Paper, Scissors
By Al Sweigart al@inventwithpython.com
The classic hand game of luck, except you always
win.
]]

print('Rock, Paper, Scissors by Al Sweigart')
print()
print('- Rock beats scissors.')
print('- Paper beats rocks.')
print('- Scissors beats paper.')

-- These variables keep track of the number of
-- wins, losses, and ties:
local wins = 0

while true do -- main game loop
  local playerMove
  local computerMove
  while true do -- Ask player for their move
    print(wins .. ' Wins, 0 Losses, 0 Ties')
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
  elseif playerMove == 'P' then
    print('PAPER versus...')
  elseif playerMove == 'S' then
    print('SCISSORS versus...')
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
  if playerMove == 'R' then
    computerMove = 'SCISSORS'
  elseif playerMove == 'P' then
    computerMove = 'ROCK'
  elseif playerMove == 'S' then
    computerMove = 'PAPER'
  end
  print(computerMove)
  os.sleep(0.5)

  print('You win!')
  wins = wins + 1
end
