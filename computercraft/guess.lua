--[[Guess the Number
by Al Sweigart al@inventwithpython.com
Try to guess the secret number based on hints.
]]

function askForGuess()
  while true do
    local guess = read() -- Enter the guess.

    if tonumber(guess) ~= nil then
      return tonumber(guess)
    end
    print('Enter a number between 1 and 100.')
  end
end

print('Guess the Number')
print('By Al Sweigart al@inventwithpython.com')
local secretNumber = math.random(1, 100)
print('I am thinking of a number between 1 and 100.')

for i = 0, 9 do -- Give the player 10 guesses.
  print('You have ' .. (10 - i) .. ' guesses left.')
  print('Take a guess.')

  local guess = askForGuess()
  if guess == secretNumber then
    break
  end

  -- Offer a hint:
  if guess < secretNumber then
    print('Your guess is too low.')
  end
  if guess > secretNumber then
    print('Your guess is too high.')
  end
end

-- Reveal the results:
if guess == secretNumber then
  print('Yay! You guessed my number!')
else
  print('Game over. The number was ' .. secretNumber)
end
