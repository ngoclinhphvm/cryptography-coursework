from algorithms.ecc.ecc import generate_keypair, encrypt, decrypt, is_on_curve

if __name__ == "__main__":
    # curve = (0, 7, 8779) # a, b , p
    curve = (1, 1, 14734520141266665763)
    a, b, p = curve
    P = (72, 611)
    # Generate keypair
    private_key, public_key = generate_keypair(P, curve)
    print(f"Private key: {private_key}")
    print(f"Public key: {public_key}")

    # Find generator point
    print(f"Generator P: {P}")
    print(f"Generator on curve: {is_on_curve(P, curve)}")

    message =  (3683630035316666441, 5525445052974999660) # This point should lie on the curve
    print(f"\nOriginal message: {message}")
    
    # Encrypt and decrypt
    cipher = encrypt(message, public_key)
    print(f"Encrypted: {cipher}")

    plain = decrypt(cipher, private_key)
    print(f"Decrypted: {plain}")

    # Check success
    print(f"Success: {message == plain}")

    # Verify all points are on curve
    # print("\nVerification:")
    # print(f"Message on curve: {is_on_curve(message, curve)}")
    # print(f"c1 on curve: {is_on_curve(cipher[0], curve)}")
    # print(f"c2 on curve: {is_on_curve(cipher[1], curve)}")
    # print(f"Decrypted on curve: {is_on_curve(plain, curve)}")
