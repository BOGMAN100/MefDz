string = 'мама мыла раму'
print(sorted(string.split(), key=lambda word: (len(word), word.lower())))

string = 'Яндекс использует Python во многих проектах'
print(sorted(string.split(), key=lambda word: (len(word), word.lower())))