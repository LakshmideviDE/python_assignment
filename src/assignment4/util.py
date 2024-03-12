def merge_the_tools(string, k):
    for i in range(0, len(string), k):
        unique_chars = set()
        result = ""
        for char in string[i:i+k]:
            if char not in unique_chars:
                result += char
                unique_chars.add(char)
        print(result)
