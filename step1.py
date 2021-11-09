import random
import time

def choose_sentence(vocabulary):
    random_position = random.randint(0, len(vocabulary)-1)
    sentence = vocabulary[random_position]
    return sentence

def translate_sentence_to_underscore(sentence):
    underscore_sentence = []
    for word in sentence:
        underscore_word = len(word) * '_'
        underscore_sentence.append(underscore_word)
    return underscore_sentence

def print_underscore_sentence(underscore_sentence):
    print(underscore_sentence)

def get_player_guess():
    letter = input('Enter your guess: ')
    return letter

def is_guess_correct(letter, sentence, underscore_sentence):
    for word in sentence:
        if str(letter) in word:
            for underscore_word in underscore_sentence:
                if str(letter) in underscore_word:
                    return False
            return True
    return False

def add_score(score):
    score += 5
    return score

def remove_score(score):
    score -= 1
    return score

def fill_letter(letter, sentence, underscore_sentence):
    response_sentence = []
    word_index = 0
    for word in sentence:
        response_word = ''
        underscore_word = underscore_sentence[word_index]
        i = 0
        for character in word:
            if character == letter:
                response_word += str(word[i])
            else:
                response_word += str(underscore_word[i])
            i += 1
        response_sentence.append(response_word)
        word_index += 1
    return response_sentence

def fill_the_letter_in_sentence(letter, sentence, underscore_sentence, score):
     is_correct = is_guess_correct(letter, sentence, underscore_sentence)
     if is_correct == True:
         score = add_score(score)
         underscore_sentence = fill_letter(letter, sentence, underscore_sentence)
     else:
         score = remove_score(score)
     return underscore_sentence, score

def is_game_over(underscore_sentence, sentence):
    if underscore_sentence == sentence:
        return True
    else:
        return False

def print_score(score):
    print(f'Your score is [{score}]')

def get_current_time():
    return time.time()

def bonus_points(game_start_time, game_end_time, score):
    if game_end_time - game_start_time < 30:
        score += 100
    return score

vocabulary = [['get', 'over', 'it'], ['Grace', 'under', 'pressure'], ['go', 'for', 'it'] ['do', 'your', 'best'], ['live', 'your', 'potential'],['manage', 'your', 'resistance'], ['yes', 'you', 'can'], ['this', 'will', 'pass'] ['prioritize', 'all', 'tasks'], ['keep', 'it', 'cool']]
sentence = []
underscore_sentence = []
score = 0

game_start_time = get_current_time()

sentence = choose_sentence(vocabulary)

underscore_sentence = translate_sentence_to_underscore(sentence)

while not is_game_over(underscore_sentence,sentence):
    print_underscore_sentence(underscore_sentence)
    letter = get_player_guess()
    underscore_sentence, score = fill_the_letter_in_sentence(letter, sentence, underscore_sentence, score)

game_end_time = get_current_time()

score = bonus_points(game_start_time, game_end_time, score)

print_score(score)


