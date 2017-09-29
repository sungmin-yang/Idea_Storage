def decide_mood(instant_memory, long_term_memory):
    mood = dict()
    im, lm = instant_memory, long_term_memory
    
    if instant_memory < off_set0 and long_term_memory < off_set0:
        mood["sad"] = calc_mood_score(im, lm)  # 0.042
    if instant_memory < off_set1 and long_term_memory < off_set0:
        mood["soso"] = calc_mood_score(im, lm)
    elif instant_memory < off_set1 and long_term_memory < off_set1:
        mood["glad"] = calc_mood_score(im, lm)
    #...mood["nothing"] ...
    
    return max(mood.values(), key=....)
