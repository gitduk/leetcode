"""
字符串 S 由小写字母组成。我们要把这个字符串划分为尽可能多的片段，同一个字母只会出现在其中的一个片段。
返回一个表示每个字符串片段的长度的列表。
"""
import queue


def check_index(S, index):
    if index == 0:
        return 0
    index_list = [index]
    for letter in set(S[:index]):
        index = S.rindex(letter)
        index_list.append(index)

    return max(index_list)


def get_result(S):
    index = 0
    short_str_list = []
    letter_rindex = S.rindex(S[0])
    max_index = check_index(S, letter_rindex)
    while len(S) > 0:
        if letter_rindex == 0:
            short_str_list.append(S[:1])
            S = S[1:]
            continue
        if max_index == letter_rindex:
            short_str_list.append(S[:max_index + 1])
            S = S[max_index + 1:]
            if S == "":
                break
            letter_rindex = S.rindex(S[0])
            max_index = check_index(S, letter_rindex)
        elif max_index > letter_rindex:
            letter_rindex = max_index
            max_index = check_index(S, letter_rindex)

    print(short_str_list)
    return short_str_list


if __name__ == '__main__':
    s = "ababcbacadefegdehijhklij"  # OK
    s2 = "qiejxqfnqceocmy"
    s3 = "ababcbacadefegdehijhklij"
    result = get_result(s)
