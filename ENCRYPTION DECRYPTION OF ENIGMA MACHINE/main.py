alphabets = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
operation = input()
pseudo_random_number = int(input())
rotors = []
for i in range(3):
    rotor = input()
    rotors.append(rotor)
message = input()

def rotorEnigma(message, rotor, operation):
	global alphabets
	if operation == 'ENCODE':
		result = [rotor[alphabets.index(letter)] for letter in message]
	else:
		result = [alphabets[rotor.index(letter)] for letter in message]

	return ''.join(result)

def caesarShift(message, pseudo_random_number):
    global alphabets
    
    i = 0
    caesar_shift = ''
    for c in message:
        if operation == 'ENCODE':
            pos = (alphabets.find(c) + pseudo_random_number + i)%len(alphabets)
        else:
            pos = (alphabets.find(c) - pseudo_random_number - i)%len(alphabets)
        caesar_shift += alphabets[pos]
        i += 1
    return caesar_shift


def encode(message, pseudo_random_number, rotors):
    encoded = caesarShift(message, pseudo_random_number)
    
    for rotor in rotors:
        encoded = rotorEnigma(encoded, rotor, operation)
    
    return encoded

def decode(message, pseudo_random_number, rotors):
    
    for i in range(len(rotors)-1, -1, -1):
        message = rotorEnigma(message, rotors[i], operation)
    
    decoded = caesarShift(message, pseudo_random_number)
    
    return decoded

result = encode(message, pseudo_random_number, rotors) if operation == 'ENCODE' else decode(message, pseudo_random_number, rotors)


print(result)