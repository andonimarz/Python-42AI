kata = {
'Python': 'Guido van Rossum',
'Ruby': 'Yukihiro Matsumoto',
'PHP': 'Rasmus Lerdorf',
}

for item, value in kata.items():
    print("{0} was created by {1}".format(item, value))
