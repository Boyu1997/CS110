from ACMachine import ACMachine

ac = ACMachine()
ac.extend(["The", "han", "and", "pork", "port", "pot", "ha", "e"]).construct().search("The pot had a handle.")
print('\nTRANSITIONS', ac.transitions, '\nFAILS: ', ac.fails, '\nEDGES: ', ac.edges, '\nOUTPUT: ', ac.output)
