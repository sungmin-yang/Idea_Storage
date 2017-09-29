# Super Simple Dialogue System
WH_query = ["what", "when", "which", "who", "whose"]
H_query  = ["how", "how long", "how have"]

# sample            : Travel agency domain. #don't need adj, only care about Origin, Destination, round-trip and dates.

# sample           S: Welcome to SUNG MIN Travel agency. What can I help you.
# sample            : I want to go Paris
# sample            : Can I go Paris?
# sample            : Paris
# sample            : I wanna check the price
# sample            : I wanna check the price for Paris
# sample            : I want to travel Paris, can you check the price?
# sample            : Paris price from Gothenburg please.
# sample            : Can you check Paris ticket?
# sample            : Can you check ticket for Paris? #accept
# sample            : Can you check ticket for/to Paris from Gothenburg? #accept
# sample            : Can you check ticket from Gothenburg for/to Paris? #accept
# sample            : Can you check ticket for Gothenburg for Paris? # dont understand
# sample            : Can you check ticket price for Gothenburg to Paris? #accept


# Candidate_city = [city1, city2, city3..., country1, countr2, country3]
# Candidate_date = [Jan, Feb, March, ..., First, Second, Third, ...]

# domain_sensitive_words = ['go', 'price', 'travel', 'trip', 'flight', 'ticket', 'check', 'buy', 'one way', 'round trip', 'class', 'economy', ...]
# scope_word             = ['for', 'from', 'to', 'toward', 'destination', 'depart', 'in', ...]

def intepret(utterance):
    words = utterence.split(' ')
    word.remove(All_adjective)

    for word in words:
        if word in wh_query:
            
