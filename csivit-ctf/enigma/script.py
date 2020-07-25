# pip install py-enigma
from enigma.machine import EnigmaMachine 

# The key sheet with some missing values for an enigma machine and a ciphertext were provided in the challenge.
# Doing some research on the enigma machine gave the basic idea about the usage of key sheet.
# https://www.cryptomuseum.com/crypto/enigma/m4/index.htm

key_sheet = 'M4 UKW $ Gamma 2 4 $ 5 9 $ 14 3 $ 5 20 fv cd hu ik es op yl wq jm'
# M4 is the machine type
# Reflector type used is missing, either B-thin or C-thin. (UKW $)
# Gamma is the fourth wheel type with ring setting and start position given(Gamma 2 4)
# Wheel type of the three primary wheels is missing while their ring setting and start postions are given($ 5 9 $ 14 3 $ 5 20)
# Plugboard settings are also given(fv cd hu ik es op yl wq jm).

ciphertext = 'zkrtwvvvnrkulxhoywoj'

# With this information it is clear that a brute force over the wheel types(8) and reflector types(2) will be convenient and will give a list of all possible deciphered texts.
num_rotors = ["I","II","III","IV","V","VI","VII","VIII"]
sym_rotors = ["Gamma"] # Beta could also have been here

reflectors = ['B-Thin','C-Thin']
rotor_combs = []
for num_1 in num_rotors:
    for num_2 in num_rotors:
        for num_3 in num_rotors:
            for sym in sym_rotors:
                rotor_combs.append(' '.join([sym,num_1,num_2,num_3]))

# Given settings
ring_setting = ' '.join([chr(ord('a')+i-1) for i in [4,9,3,20]])
plugboard_setting = 'fv cd hu ik es op yl wq jm'
start_positions = ''.join([chr(ord('a')+i-1) for i in [2,5,14,5]])

for rotor_comb in rotor_combs:  
    for reflector in reflectors:
        
        # Create an enigma machine object from py-enigma
        machine = EnigmaMachine.from_key_sheet(
            rotors=rotor_comb,
            reflector=reflector,
            ring_settings=ring_setting,
            plugboard_settings=plugboard_setting
        )

        machine.set_display(start_positions)
        decipheredtext = machine.process_text(ciphertext)
        
        # Look for flag format:
        if(decipheredtext[:6]=="CSICTF"):
            print(decipheredtext)
