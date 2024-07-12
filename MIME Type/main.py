n = int(input())  # Number of elements which make up the association table.
q = int(input())  # Number Q of file names to be analyzed.
mime_t = {}
for i in range(n):
    # ext: file extension
    # mt: MIME type.
    ext, mt = input().split()
    mime_t[ext.lower()] = mt
for i in range(q):
    fname = input()  # One file name per line.
    
    f_ext = fname.split('.')
    if len(f_ext) > 1 and f_ext[-1].lower() in mime_t:
        print(mime_t[f_ext[-1].lower()])
    else:
        print("UNKNOWN")