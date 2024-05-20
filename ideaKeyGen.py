def generate_subkeys(key):
    subkeys = key
    subkeys += key[6:] + key[:6]  # Concatenate the last 26 bits with the first 6 bits
    subkeys += key[12:] + key[:12]
    subkeys += key[18:] + key[:2]

    # Split the concatenated subkeys into 4-bit chunks
    subkeys_list = [int(subkeys[i:i+4], 2) for i in range(0, len(subkeys), 4)]
    return subkeys_list

# Example usage
key = "11011100011011110011111101011001"
subkeys = generate_subkeys(key)
print("Subkeys:", subkeys)
