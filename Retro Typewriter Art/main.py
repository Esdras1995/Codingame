t = input()
specials = {'sp': ' ', 'bS': '\\', 'sQ': "'", 'nl': '\n'}

nt = ''
for st in t.split(' '):
    inside = False
    for k, sp in specials.items():
        if k in st:
            m = st.replace(k, '') if not k == 'nl' else 1
            nt += int(m)*sp
            inside = True
            break
    
    if not inside:      
        c = st[-1]
        m = st[0:len(st)-1]
        nt += int(m)*c
    
print(nt)