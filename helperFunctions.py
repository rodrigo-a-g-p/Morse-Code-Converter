def convert_message_to_morse_code(input_message, input_morse_code_dict):
    # In morse code, after each letter is translated, there is a space between letters
    # Adding a space at the end of each dict value, so there is space after each letter of the morse code translation
    # When a space is inserted by the user in his/her message, the space gets rendered as a " / "
    for dict_key in input_morse_code_dict.keys():
        input_morse_code_dict[dict_key] += ' '

    morse_message = ''
    for char in input_message:
        if char in input_morse_code_dict.keys():
            morse_message += input_morse_code_dict[char]
    return morse_message

