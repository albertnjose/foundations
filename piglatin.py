# Pig latin converter

def pig_trans():
    vowels = ['a', 'e', 'i', 'o', 'u']
    user_word = input('Type any word: ')
    
    if(len(user_word) > 0 and user_word.isalpha()): # checks for nonempty word and
        # has alphabet characters
        lower_word = user_word.lower()
    # if word starts with a vowel append 'ay' otherwise continue to consonants logic
        
        begin_with = lower_word[0]
        if begin_with in (vowels):
            pig_word = lower_word + 'ay'
            print(pig_word)
    # checks for multiple consonants creates prefix    
        else:
            add_prefix = ''
            for x in range(len(lower_word)):
                if lower_word[x] in vowels:
                    break
                else:
                    add_prefix = add_prefix + lower_word[x]
    
            pig_word = lower_word[len(add_prefix):] + add_prefix + 'ay'
            print(pig_word)
    else:
        print('Not a valid word.')
        
pig_trans()    