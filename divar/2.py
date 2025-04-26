def count_sms(message):
    s_count = 0
    sm_count = 0
    sms_count = 0

    for letter in message:
        if letter == "s":
            s_count += 1
            sms_count += sm_count
        elif letter == "m":
            sm_count += s_count

    return sms_count


for _ in range(int(input())):
    message = input()
    result = count_sms(message)
    print(result)
