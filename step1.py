vocabulary = [['get', 'over', 'it'], ['Grace', 'under', 'pressure'], ['go', 'for', 'it']]
sentence = []
underscore_sentence = []
score = 0

def choose_sentence(vocabulary):
    pass

def translate_sentence_to_underscore(sentence):
    pass

def print_underscore_sentence(underscore_sentence):
    pass

def get_player_guess():
    letter = print(input('Enter your guess: '))


def is_guess_correct(letter, sentence):
    pass


def add_score():
    pass


def remove_score():
    pass


def fill_letter(letter, sentence, underscore_sentence):
    pass


def fill_the_letter_in_sentence(letter, sentence, underscore_sentence):
     is_correct = is_guess_correct(letter, sentence)
     if is_correct == True:
         add_score()
         underscore_sentence = fill_letter(letter, sentence, underscore_sentence)
     else:
         remove_score()
     return underscore_sentence

def is_game_over(underscore_sentence, sentence):
    if underscore_sentence == sentence:
        return True
    else:
        return False

def print_score(score):
    pass


sentence = choose_sentence(vocabulary)

underscore_sentence = translate_sentence_to_underscore(sentence)

print_underscore_sentence(underscore_sentence)

letter = get_player_guess()

underscore_sentence = fill_the_letter_in_sentence(letter,sentence, underscore_sentence)



while not is_game_over(underscore_sentence,sentence):
    print_underscore_sentence(underscore_sentence)
    letter = get_player_guess()
    underscore_sentence = fill_the_letter_in_sentence(letter, sentence, underscore_sentence)


print_score(score)



