size = 1
inc = 1
while true do
  for i = 1, size do
    io.write('#')
  end
  io.write('\n')
  os.sleep(0.1)
    
  size = size + inc

  if size == 10 then
    inc = -1
  elseif size == 0 then
    inc = 1
  end
end
