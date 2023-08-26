with open(file="./Input/Names/invited_names.txt") as names:
    all_names = names.readlines()

for each_name in range(len(all_names)):
    all_names[each_name] = all_names[each_name].strip()
    with open("./Input/Letters/starting_letter.txt") as read_letter:
        contents = read_letter.read()
    with open(f"./Output/ReadyToSend/letter_to_{all_names[each_name]}.txt", mode="w") as write_letter:
        write_letter.write(contents.replace("[name]", all_names[each_name]))
