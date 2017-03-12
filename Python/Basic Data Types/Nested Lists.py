if __name__ == '__main__':
    score_name = {}
    scores = set()
    for _ in range(int(input())):
        name = input()
        score = float(input())
        if str(score) in score_name:
            score_name[str(score)].append(name)
        else :
            score_name[str(score)] = [name]
        scores.add(score)
    mi = min(scores)
    scores.remove(mi)
    for i in sorted(score_name[str(min(scores))]):
        print(i)