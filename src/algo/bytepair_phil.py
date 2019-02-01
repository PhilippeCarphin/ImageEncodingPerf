
def byte_pair_encode(input_string):
    current_object = { "bytes":list(map(ord, input_string)), "replacements":[]}

    while True:
        pair = get_most_frequent_pair(current_object["bytes"])
        if pair[1] == 1:
            break
        unused_chars = get_unused_chars(current_object["bytes"])
        if not unused_chars:
            break
        replacement_char = unused_chars.pop()

        next_message = replace_pair(current_object["bytes"], pair[0], replacement_char)
        new_replacements = current_object["replacements"] + [(pair[0], replacement_char)]
        current_object = { "bytes": next_message, "replacements":new_replacements}

    return { "bytes": next_message, "replacements":new_replacements}



def byte_pair_decode(coded_message_object):
    bytes = coded_message_object["bytes"]
    repls = coded_message_object["replacements"]
    for rep in reversed(coded_message_object["replacements"]):
        bytes = un_replace_pair(bytes, rep)

    return bytes


def un_replace_pair(bytes, replacement):
    output = [] 
    length = len(bytes)
    i = 0
    while i < length:
        c = bytes[i]
        p = tuple(bytes[i:i+2])

        if c == replacement[1]:
            output += list(replacement[0])
            i += 1
        else:
            output.append(c)
            i += 1
    return output



def test_byte_pair_encode():
    with open("./small_text.txt") as input_file:
        file_content = input_file.read()
        print(file_content)
        print(type(file_content))

def get_pair_frequencies(string):
    pair_frequencies = {}
    for i in range(len(string) - 2):

        pair = tuple(string[i:i+2])

        if pair in pair_frequencies:
            pair_frequencies[pair] += 1
        else:
            pair_frequencies[pair] = 1

    return pair_frequencies

def test_get_pair_frequencies():
    pair_frequencies = get_pair_frequencies(test_string)
    print(pair_frequencies)


def get_most_frequent_pair(string):
    pair_frequencies = get_pair_frequencies(string)

    max_freq = 0
    most_frequent = None

    for p in pair_frequencies:
        freq = pair_frequencies[p]
        if freq > max_freq:
            most_frequent = p
            max_freq = freq
    return (most_frequent, max_freq)

def test_get_most_frequent_pair():
    mfp = get_most_frequent_pair(test_string)
    print(get_pair_frequencies(test_string))
    print("most frequent pair " + str(mfp))

def do_first_pass(string):
    pair = get_most_frequent_pair(string)
    replacement_char = get_unused_chars(string).pop()
    return (replace_pair(string, pair, replacement_char), [(pair, replacement_char)])

def get_unused_chars(string):
    possible_chars = set(range(256))
    used_chars = set(string)
    return possible_chars - used_chars

def test_get_unused_chars():
    print(get_unused_chars([81,83,82]))

def replace_pair(string, pair, replacement):
    output = [] 
    length = len(string)
    i = 0
    while i < length:
        c = string[i]
        p = tuple(string[i:i+2])

        # print("replacement : ".format(replacement))
        if p == pair:
            output.append(replacement)
            i += 2
        else:
            output.append(c)
            i += 1
    return output

def test_replace_pair():
    print(test_string)
    print(replace_pair(test_string, (65,83), 8))

if __name__ == "__main__":
    test_string = "ASDASDASKSA:DSKDASDFHFDLJLSGDNCMS<DVB:JK:J"
    # print(test_string)

    cmo = byte_pair_encode(test_string)
    decoded = byte_pair_decode(cmo)
    print(decoded)
    decoded_string = ''.join(list(map(chr, decoded)))
    print(decoded_string)

    print(test_string == decoded_string)
    # print(test_string)
    # test_get_most_frequent_pair()
    # test_byte_pair_encode():
    # test_get_pair_frequencies():
    # test_get_byte_set():
    # test_get_most_frequent_pair():
    #test_get_unused_chars()
    #test_replace_pair()
    # print(do_first_pass(test_string))



