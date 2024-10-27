def encode_message(message: str):
    sanitized_message = ''.join(filter(lambda x : x != ' ', message)).lower()
    n = len(sanitized_message)
    sum = 0

    for i in range(n):
        sum += (ord(sanitized_message[i]) - ord('a')) * (pow(26, n - i - 1))

    return sum 
