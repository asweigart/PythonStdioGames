--[[Deep Cave by Al Sweigart al@inventwithpython.com
An animation of a deep cave that goes forever
into the earth.
]]

local WIDTH = 50
local PAUSE_AMOUNT = 0.05

print('Deep Cave by Al Sweigart al@inventwithpython.com')
print('Press Ctrl-T to stop.')
os.sleep(2)

local leftWidth = 20
local gapWidth = 10

while true do
  -- Display the tunnel segment:
  local rightWidth = WIDTH - gapWidth - leftWidth
  io.write(string.rep('#', leftWidth))
  io.write(string.rep(' ', gapWidth))
  io.write(string.rep('#', rightWidth))
  io.write('\n')

  os.sleep(PAUSE_AMOUNT)

  -- Adjust the left side width:
  local diceRoll = math.random(1, 6)
  if diceRoll == 1 and leftWidth > 1 then
    leftWidth = leftWidth - 1
  elseif diceRoll == 2 and leftWidth + gapWidth < WIDTH - 1 then
    leftWidth = leftWidth + 1
  end

  -- Adjust the gap width:
  diceRoll = math.random(1, 6)
  if diceRoll == 1 and gapWidth > 1 then
    gapWidth = gapWidth - 1
  elseif diceRoll == 2 and leftWidth + gapWidth < WIDTH - 1 then
    gapWidth = gapWidth + 1
  end

end