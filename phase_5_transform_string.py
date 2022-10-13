string = "isrveawhobpnutfg"

for i in 'abcdefghijklmnopqrstuvwxyz':
    if string[ord(i) & 0xf] in 'giants':
        print(f"{string[ord(i) & 0xf]}", i)
