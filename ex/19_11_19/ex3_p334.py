'''
def rank2(scores):
    scores_sorted = sorted(scores,reverse = True)
    results = []
    for n in scores_sorted:
        results.append(
            sum([1 for i in scores if i> n]) + 1
            )
    return results

print(rank2([87,32,75,50,32,75,75]))
'''

scores = [87,32,75,50,32,75,75]

def rank(scores):
    scores_sorted = sorted(scores,reverse = True)
    print(scores_sorted)

    l_rank = 1
    l_final_score = 0
    rank = []
    for ind, score in enumerate(scores_sorted):
        print(ind,score)
        if (score != l_final_score):
            l_rank = ind + 1
        rank.insert(ind,l_rank)
        l_final_score = score
    print(rank)



rank(scores)



