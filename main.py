import math, queue
from collections import Counter

####### Problem 3 #######

test_cases = [('book', 'back'), ('kookaburra', 'kookybird'), ('elephant', 'relevant'), ('AAAGAATTCA', 'AAATCA')]
alignments = [('b--ook', 'bac--k'), ('kook-ab-urr-a', 'kooky-bi-r-d-'), ('relev--ant','-ele-phant'), ('AAAGAATTCA', 'AAA---T-CA')]

def MED(S, T):
    # TO DO - modify to account for insertions, deletions and substitutions
    if (S == ""):
        return (len(T))
    elif (T == ""):
        return (len(S))
    else:
        if (S[0] == T[0]):
            return (MED(S[1:], T[1:]))
        else:
            return (1 + min(MED(S, T[1:]), MED(S[1:], T)))


def fast_MED(S, T, MED={}):
        if (S, T) in MED:
        return MED[(S, T)]

    if T == "":
        return len(S)
    if S == "":
        return len(T)

    elif S[0] == T[0]:
        MED[(S, T)] = fast_MED(S[1:], T[1:], MED)
    else:
        MED[(S, T)] = 1 + min(fast_MED(S, T[1:], MED), fast_MED(S[1:], T, MED))

    return MED[(S, T)]

def fast_align_MED(S, T, MED={}):
    # TODO - keep track of alignment
    if (S, T) in MED:
        return MED[(S, T)]

    elif T == "":
        MED[(S, T)] = (S, "-" * len(S))
    elif S == "":
        MED[(S, T)] = ("-" * len(T), T)

    elif S[0] == T[0]:
        align_S, align_T = fast_align_MED(S[1:], T[1:], MED)
        MED[(S, T)] = (S[0] + align_S, T[0] + align_T)
    else:
        ins_S, ins_T = fast_align_MED(S, T[1:], MED)
        del_S, del_T = fast_align_MED(S[1:], T, MED)

        ins_C = 1 + len(ins_S)
        del_C = 1 + len(del_S)

        if ins_C <= del_C:
            MED[(S, T)] = ("-" + ins_S, T[0] + ins_T)
        else:
            MED[(S, T)] = (S[0] + del_S, "-" + del_T)

    return MED[(S, T)]
