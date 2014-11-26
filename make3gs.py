

# The third person singular verb form in English is distinguished by the suffix -s, which is added to the stem of the infinitive form: run -> runs. A simple set of rules can be given as follows:

#     If the verb ends in y, remove it and add ies
#     If the verb ends in o, ch, s, sh, x or z, add es
#     By default just add s

# Your task in this exercise is to define a function make_3sg_form() which given a verb in infinitive form returns its third person singular form. Test your function with words like try, brush, run and fix. Note however that the rules must be regarded as heuristic, in the sense that you must not expect them to work for all cases. Tip: Check out the string method endswith().
import re

def popp(data, number):
    data = list(data)
    for i in range(number):
        data.pop()
    return ''.join(data)

def is_conso_vowel_conso(data):
    data = list(data)
    if (((data[-3] and data[-1]) not in 'aeiouAEIOU') and (data[-2] in 'aeiouAEIOU')):
        return True
    else:
        return False


def make_3gs_form(verb):
    if verb.endswith('y'):
        verb = popp(verb, 1)
        verb = verb + 'ies'
    elif verb.endswith(('o','s','x','z')):
        verb = verb + 'es'
    elif verb.endswith(('ch','sh')):
        verb = verb + 'es'
    else:
        verb = verb + 's'

    return verb

def make_int_form(verb):
    if verb.endswith('e'):
        if verb == 'lie':
            verb = popp(verb, 2)
            verb = verb + 'y' + 'ing'
        else:
            if verb == ('see' or 'be' or 'flee' or 'knee'):
                verb = verb + 'ing'
            else:
                verb = popp(verb, 1)
                verb = verb + 'ing'

    elif verb.endswith('ie'):
        verb = popp(verb, 2)
        verb = verb + 'y' + 'ing'

    elif is_conso_vowel_conso(verb):
        verb = verb + verb[-1]
        verb = verb + 'ing'

    else:
        verb = verb + 'ing'

    return verb

print(make_int_form('lie'))