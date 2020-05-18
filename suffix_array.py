from sys import stdin as si
from functools import cmp_to_key as ctk


class SuffixStruct(object):
    index = 0
    rank1 = 0
    rank2 = 0


def suffix_array_n2logn(A):
    # if binary search is used for searching the suffix, overall time-complexity will be n^2logn
    return [(rank, suffix) for suffix, rank in sorted([(A[i:], i) for i in range(len(A))])]


def compare(a, b):
    if a.rank1 != b.rank1:
        return a.rank1 - b.rank1
    else:
        return a.rank2 - b.rank2


def suffix_struct_value(s):
    return s.index, s.rank1, s.rank2

def suffix_array_nlogn2(A):
    l = len(A)
    suffix_array = []  # array of suffix struct

    # create index and add rank1 and rank2 in suffix_struct
    for i in range(l):
        st = SuffixStruct()
        st.index = i
        st.rank1 = ord(A[i]) - ord('a')
        st.rank2 = -1 if i+1 >= l else ord(A[i+1]) - ord('a')
        suffix_array.append(st)

    suffix_array.sort(key=ctk(compare))

    # holds original index, test it with print command in line
    index = [0]*l
    k = 4
    while k < 2*l:
        current_rank = 0
        prev_rank = suffix_array[0].rank1  # only used for comparison, below for loop is executed from 1 to l
        suffix_array[0].rank1 = current_rank
        index[suffix_array[0].index] = 0
        # print([suffix_struct_value(s) for s in suffix_array])
        for j in range(1, l):
            if suffix_array[j].rank1 != prev_rank or suffix_array[j].rank2 != suffix_array[j-1].rank2:
                current_rank += 1
            prev_rank = suffix_array[j].rank1
            suffix_array[j].rank1 = current_rank
            index[suffix_array[j].index] = j

        # print (index)
        # Update rank2, pick values of rank1 from the indexes
        for j in range(l):
            next_index = suffix_array[j].index + k//2
            # print(next_index)
            suffix_array[j].rank2 = suffix_array[index[next_index]].rank1 if next_index < l else -1

        suffix_array.sort(key=ctk(compare))

        k *= 2

    suffix_arr = [suffix.index for suffix in suffix_array]

    return suffix_arr


if __name__ == "__main__":
    for i in range(int(si.readline().strip())):
        print(suffix_array_nlogn2(si.readline().strip()))

"""
references:
https://www.geeksforgeeks.org/suffix-array-set-2-a-nlognlogn-algorithm/
https://ide.geeksforgeeks.org/b7OX24R0gE
https://discuss.codechef.com/t/a-tutorial-on-suffix-arrays/2950
Practice Problems

    Uva 760 - DNA Sequencing
    Uva 1223 - Editor
    Codechef - Tandem
    Codechef - Substrings and Repetitions
    Codechef - Entangled Strings
    Codeforces - Martian Strings
    Codeforces - Little Elephant and Strings
    SPOJ - Ada and Terramorphing
    SPOJ - Ada and Substring
    UVA - 1227 - The longest constant gene
    SPOJ - Longest Common Substring
    UVA 11512 - GATTACA
    LA 7502 - Suffixes and Palindromes
    GYM - Por Costel and the Censorship Committee
    UVA 1254 - Top 10
    UVA 12191 - File Recover
    UVA 12206 - Stammering Aliens
    Codechef - Jarvis and LCP
    LA 3943 - Liking's Letter
    UVA 11107 - Life Forms
    UVA 12974 - Exquisite Strings
    UVA 10526 - Intellectual Property
    UVA 12338 - Anti-Rhyme Pairs
    DevSkills Reconstructing Blue Print of Life
    UVA 12191 - File Recover
    SPOJ - Suffix Array
    LA 4513 - Stammering Aliens
    SPOJ - LCS2
    Codeforces - Fake News (hard)
    SPOJ - Longest Commong Substring
    SPOJ - Lexicographical Substring Search
    Codeforces - Forbidden Indices
    Codeforces - Tricky and Clever Password
    LA 6856 - Circle of digits
"""
