intext = input()

new_text = ''
for c in [',', '.', '?', '!', ';']:
    
    if c not in intext:
        continue
    
    new_text = ''
    text = intext.split(c)
    for i, word in enumerate(text):
        word = word.strip()
        if c == '.':
            word = word.capitalize()
        
        if word:
            new_text += word+(c+' ' if i < len(text)-1 else '')
            intext = new_text.strip()



print(intext)