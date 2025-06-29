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
        character = ""
        count = 0
        sorted_characters = {"character": [character], "count": [count]}
        for character in character_count:
            if character not in sorted_characters:
                sorted_characters[character] = sorted_characters.get(character,0) + 1
                sorted_characters[count] += 1
            elif character in sorted_characters:
                sorted_characters[count] += 1
        return sorted_characters
