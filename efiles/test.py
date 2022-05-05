with open('efiles/reviews.txt','r+', encoding = 'utf-8') as filer:

    reviewcount = 0
    counter = 0
    c = 14

    for line in filer:
        #if line[1] == str(c):
        #        print(line[1])
        if line[1:3] == str(c):
            print(line[1:3])