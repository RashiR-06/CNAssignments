def send():
    data = input("Enter 4-bit data: ")

    d4, d3, d2, d1 = map(int, data)

    p1 = d1 ^ d2 ^ d4
    p2 = d1 ^ d3 ^ d4
    p4 = d2 ^ d3 ^ d4
   
    code = f"{d4}{d3}{d2}{p4}{d1}{p2}{p1}"

    print("Generated Hamming Code:", code)

def receive():
    code = input("Enter received 7-bit code: ")

    bits = list(map(int, code))

    d4 = bits[0]
    d3 = bits[1]
    d2 = bits[2]
    p4 = bits[3]
    d1 = bits[4]
    p2 = bits[5]
    p1 = bits[6]
   
    s1 = p1 ^ d1 ^ d2 ^ d4
    s2 = p2 ^ d1 ^ d3 ^ d4
    s4 = p4 ^ d2 ^ d3 ^ d4

    error_position = s4 * 4 + s2 * 2 + s1

    if error_position == 0:
        print("No error detected.")
    else:
        print("Error at position:", error_position)

        index = 7 - error_position

        if bits[index] == 0:
            bits[index] = 1
        else:
            bits[index] = 0

        print("Error corrected.")

    corrected = "".join(map(str, bits))
    print("Corrected Code:", corrected)
send()
receive()
