import random

### Components ###

padding = ['Our aim is to',  'Our goal is to', 'Our mission is to', 'We', 'We seek to', 'We strive to']

verb_tups = [('achiev','e','ing', '+'),
('advanc', 'e', 'ing', '+'),
('amplify', '', 'ing', '+'),
('communicat', 'e', 'ing'),
('connect', '', 'ing', '+'),
('creat', 'e', 'ing', '+'),
('deliver', '', 'ing', '+'),
('design', '', 'ing', '+'),
('disseminat', 'e', 'ing', '+'),
# ('eliminat', 'e', 'ing', '-'),
('elucidat','e','ing','+'),
('energiz','e','ing', '+'),
('engag', 'e', 'ing', '+'),
('enrich', '', 'ing', '+'),
('expand', '', 'ing', '+'),
('foster','','ing', '+'),
('identify','','ing', '+'),
('improv','e','ing', '+'),
('innovat','e','ing', '+'),
# ('overcom', 'e', 'ing', '-'),
('promot','e','ing', '+'),
('redesign','','ing','+'),
('rethink','','ing','+'),
# ('reduc', 'e', 'ing', '-'),
# ('remov', 'e', 'ing', '-'),
('serv', 'e', 'ing', '+'),
('support','','ing', '+')]

adjs = ['academic', 'ambitious', 'bleeding-edge', 'collaborative', 'community', 'culturally-informed', 'cutting-edge', 'diverse', 'educational', 'entrepreneurial', 'environmentally-friendly', 'ethical', 'forward-thinking', 'fresh', 'global', 'globally-respected', 'high-impact', 'highly-regarded', 'innovative', 'interdisciplinary', 'international', 'lasting' 'local', 'low-cost', 'multicultural', 'outstanding', 'preeminent', 'scholarly', 'socially-conscious', 'sustainable', 'top-ranked', 'unique', 'world-changing', 'world-renowned']

nouns = ['capacity', 'challenges', 'collaboration', 'concepts', 'design', 'diversity', 'excellence', 'faculty', 'ideas', 'information', 'knowledge', 'leadership', 'needs', 'opportunities', 'people', 'perspectives', 'practice', 'research', 'resources', 'results', 'scholarship', 'solutions', 'spaces', 'students', 'teaching', 'technology', 'training', 'understanding', 'values', 'vision']

### Function Definition ###

def generate_mission():
    v1 = random.choice(verb_tups) # first verb
    a1 = random.choice(adjs) # first adjective
    n1 = random.choice(nouns) # first noun

    r = random.randint(0,4) # use randint to determine structure

    target = random.choice(padding) + ' ' + v1[0] + v1[1] + ' ' + a1 + ' ' + n1

    if r == 1: # "Do A by doing B" construction
        verb_tups.remove(v1) # remove first verb from the list for now
        v2 = random.choice(verb_tups) # pick a second verb
        adjs.remove(a1) # remove first adj from the list for now
        a2 = random.choice(adjs) # pick a second adj
        nouns.remove(n1) # remove first noun from the list for now
        n2 = random.choice(nouns) # pick a second noun

        target = target + ' by ' + v2[0] + v2[2] + ' ' + a2 + ' ' + n2 + '.'

        # put everything removed back in the lists!
        verb_tups.append(v1)
        adjs.append(a1)
        nouns.append(n1)

    elif r == 2: # "X, Y, and Z" construction
        verb_tups.remove(v1)
        v2 = random.choice(verb_tups)
        verb_tups.remove(v2)
        v3 = random.choice(verb_tups)

        adjs.remove(a1)
        a2 = random.choice(adjs)
        adjs.remove(a2)
        a3 = random.choice(adjs)

        nouns.remove(n1)
        n2 = random.choice(nouns)
        nouns.remove(n2)
        n3 = random.choice(nouns)

        target = target + ', ' + v2[0] + v2[1] + ' ' + a2 + ' ' + n2 + ', and ' + v3[0] + v3[1] + ' ' + a3 + ' ' + n3 + '.'

        # reset lists
        verb_tups.append(v1)
        verb_tups.append(v2)
        adjs.append(a1)
        adjs.append(a2)
        nouns.append(n1)
        nouns.append(n2)

    elif r == 3:
        verb_tups.remove(v1)
        v2 = random.choice(verb_tups)
        adjs.remove(a1)
        a2 = random.choice(adjs)
        nouns.remove(n1)
        n2 = random.choice(nouns)

        target = target + ' while we ' + v2[0] + v2[1] + ' ' + a2 + ' ' + n2 + '.'

        verb_tups.append(v1)
        adjs.append(a1)
        nouns.append(n1)

    elif r == 4:
        adjs.remove(a1)
        a2 = random.choice(adjs)
        nouns.remove(n1)
        n2 = random.choice(nouns)

        target = target + ' for ' + a2 + ' ' + n2 + '.'

        adjs.append(a1)
        nouns.append(n1)

    else:
        target = target + "."

    return target
