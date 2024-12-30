secretNumber = math.random(1, 100)
print('I am thinking of a number between 1 and 100.')

for i = 0, 9 do -- Give the player 10 guesses.
  print('You have ' .. (10 - i) .. ' guesses left.')
  print('Take a guess.')

  guess = read()
  if guess == secretNumber then
    break
  end

  if guess < secretNumber then
    print('Your guess is too low.')
  end
  if guess > secretNumber then
    print('Your guess is too high.')
  end
end

if guess == secretNumber then
  print('Yay! You guessed my number!')
else
  print('Game over. The number was ' .. secretNumber)
end
