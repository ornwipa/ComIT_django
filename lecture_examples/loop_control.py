count = 0
while count < 5:
    print(f'The count is: {count}')
    count = count + 1
    if count == 3:
        break # exit the iteration (all loops) entirely

for letter in 'ComIT':
    if letter == 'm':
        continue # skip the rest of commands in current loop and start the next loop
    print(f'Current Letter: {letter}')

for letter in 'ComIT':
    if letter == 'm':
        pass # placeholder or null operation before implementation
    print(f'Current Letter: {letter}')