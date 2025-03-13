class solution:
    def alternatstrings(word1,word2):
        i,j=0,0
        res =[]
        while i < len(word1) and j <len(word2):
            res.append(word1[i])
            res.append(word2[j])

        res.append(word1[i:])
        res.append(word2[j:])

        return "".join(res)




