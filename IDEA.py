def generate_subkeys(key):
    subkeys = key
    subkeys += key[6:] + key[:6]  # Concatenate the last 26 bits with the first 6 bits
    subkeys += key[12:] + key[:12]
    subkeys += key[18:] + key[:2]  # Split the concatenated subkeys into 4-bit chunks
    subkeys_list = [int(subkeys[i:i+4], 2) for i in range(0, len(subkeys), 4)]
    return subkeys_list

def encrypt(plaintext, key):
    # Convert plaintext and key from binary to decimal
    plaintext_decimal = [int(plaintext[i:i+4], 2) for i in range(0, len(plaintext), 4)]
    subkeys = generate_subkeys(key)
    print(f"subkeys: {subkeys}")

    # Perform 4 complete rounds and 1 half-round
    for round in range(4):
        plaintext_decimal = round_encrypt(plaintext_decimal, subkeys[round*6:(round+1)*6])
        plaintext_decimal = [plaintext_decimal[1], plaintext_decimal[3], plaintext_decimal[2], plaintext_decimal[0]]  # Swap step 12 and 13

    # Perform the final half-round
    ciphertext_decimal = half_round_encrypt(plaintext_decimal, subkeys[24:28])

    # Convert the ciphertext from decimal to binary
    ciphertext = ''.join([format(x, 'b').zfill(4) for x in ciphertext_decimal])
    return ciphertext

def round_encrypt(block, round_keys):
    if len(block) != 4:
        raise ValueError("Invalid block length")
    x1, x2, x3, x4 = block
    k1, k2, k3, k4, k5, k6 = round_keys

    step1 = mul(x1, k1)
    step2 = add(x2, k2)
    step3 = add(x3, k3)
    step4 = mul(x4, k4)
    step5 = bitwise_xor(step1, step3)
    step6 = bitwise_xor(step2, step4)
    step7 = mul(step5, k5)
    step8 = add(step6, step7)
    step9 = mul(step8, k6)
    step10 = add(step7, step9)
    step11 = bitwise_xor(step1, step9)
    step12 = bitwise_xor(step3, step9)
    step13 = bitwise_xor(step2, step10)
    step14 = bitwise_xor(step4, step10)

    return [step11, step13, step12, step14]

def half_round_encrypt(block, round_keys):
    x1, x2, x3, x4 = block
    k1, k2, k3, k4 = round_keys
    step1 = mul(x1, k1)
    step2 = add(x2, k2)
    step3 = add(x3, k3)
    step4 = mul(x4, k4)
    return [step1, step3, step2, step4]

def mul(a, b):
    return (a * b) % 17

def add(a, b):
    return (a + b) % 16

def bitwise_xor(a, b):
    return a ^ b

# Example usage
key = "11011100011011110011111101011001"
plaintext = input("Enter the plaintext in binary: ")
ciphertext = encrypt(plaintext, key)
print("Ciphertext:", ciphertext)