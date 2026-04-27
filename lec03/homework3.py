def words2characters(words):
    """
    This function converts a list of words into a list of characters.

    @param:
    words - a list of words

    @return:
    characters - a list of characters
    """
    listofcharacters = []
    for word in words:
        for c in str(word):
            listofcharacters.append(c)
    return listofcharacters
