def word_count(file_contents):
    words = file_contents.split()
    count_words = len(words)
    return count_words

def count_characters(file_contents):
    character_count = {}
    lower_case = file_contents.lower()
    for character in lower_case:
        if character not in character_count:
            character_count[character] = character_count.get(character, 0) + 1            
        elif character in character_count:
            character_count[character] += 1
    return character_count

def sort_characters(character_count):
        sorted_characters = []
        for character in character_count:
            if character.isalpha():
                count = character_count[character]
                sorted_characters.append({"char": character, "count": count})
            else:
                pass
        sorted_characters.sort(key = lambda x: x['count'], reverse = True)
        return sorted_characters
