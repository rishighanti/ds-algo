def findWords(input_str, dictionary):
    if input_str == "" or len(dictionary) == 0:
        return []

    # counter to store frequency of each letter in the input string.
    input_counter = count_chars(input_str)
    result = []

    # Iterate through the dictionary and check if each word can be formed using the letters in the string.
    for word in dictionary:
        # counter to store frequency of each letter from the dictionary.
        word_counter = count_chars(word)

        # Check if the word can be formed using the letters in the string.
        can_form = True
        for char, count in word_counter.items():
            if char not in input_counter or input_counter[char] < count:
                can_form = False
                break
    
        if can_form:
            result.append(word)

    return result


def count_chars(s):
    char_count = {}
    for char in s:
        char_count[char] = char_count.get(char, 0) + 1

    return char_count


def main():
    input = [
        ["ate", ["ate", "eat", "tea", "dog", "do", "god", "goo", "go", "good"]],
        ["oogd", ["ate", "eat", "tea", "dog", "do", "god", "goo", "go", "good"]],
        ["", []],
        ["", ["enlist", "silent", "inlet", "tinsel", "apple"]],
        ["listen", []],
        ["a", ["a", "b", "c"]],
        ["adc", ["a", "b", "c", "ax", "ac", "d", "b"]],
        ["abc", ["a", "b", "c"]],  
        ["Listen", ["enlist", "silent", "inlet", "tinsel"]],
        ["hello!",  ["hello", "world", "hi"]],
    ]

    for i in input:
        print()
        print("Input: ", i)
        print("Output: ", findWords(i[0], i[1]))
        print()


if __name__ == '__main__':
    main()