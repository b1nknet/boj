case = int(input())

for _ in range(case):
    word_dict = {}
    dict_idx = 1

    while True:
        try:
            sentence = input().split()
            if not sentence:
                break

            words = set(sentence)
            for idx, word in enumerate(sentence):
                if word in word_dict:
                    sentence[idx] = word_dict[word]
                else:
                    word_dict[word] = str(dict_idx)
                    dict_idx += 1

            print(" ".join(sentence))
        except EOFError:
            break
    print()