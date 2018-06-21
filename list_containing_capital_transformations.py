def random_list_element_change_into_list(unsplited_list):
    import random
    element = random.choice(unsplited_list)
    splited_list_element = element.split(' | ', )
    splited_list_element[1] = splited_list_element[1][:-1].upper()
    return splited_list_element

def change_capital_word_into_capital_hidden_template(capital):
    capital_hidden_template=[]
    for char in capital:
        capital_hidden_template.append(" " + char + "  ")
    return capital_hidden_template

def delete_spaces_in_capital_hidden(capital, capital_hidden):
    x = " "
    if x in capital and x not in capital_hidden:
        j = 0
        for char in capital:
            if char == " ":
                capital_hidden[j] = "    "
            j += 1