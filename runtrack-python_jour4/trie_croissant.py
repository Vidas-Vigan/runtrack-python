def trie_croissant(Liste):
    size = 0
    for x in Liste:
        size += 1
    
    for n in range(1,size):
        position = Liste[n]
        j = n-1
        
        while j>=0 and Liste[j] > position:
            Liste[j+1] = Liste[j]
            j = j-1
        Liste[j+1] = position
    return Liste

print(trie_croissant([8,15,6,39,100,2,37,4]))