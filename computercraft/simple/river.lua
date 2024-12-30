WIDTH = 40

leftWidth = 20

while true do
  io.write(string.rep(' ', leftWidth))
  io.write(string.rep('~', 10))
  io.write('\n')

  os.sleep(0.05)

  diceRoll = math.random(1, 6)
  if diceRoll == 1 and leftWidth > 1 then
    leftWidth = leftWidth - 1
  elseif diceRoll == 2 and leftWidth < WIDTH - 1 then
    leftWidth = leftWidth + 1
  end
end