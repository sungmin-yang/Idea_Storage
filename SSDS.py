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

# domain["price"]           = ['price', 'how much', 'cost']
# domain["available"]       = ['free', 'available', 'possible']

idiom = ["Can you", "You gotta", ...]

#Defining incremental information function : set everything with None at first.
def check(domian, city_from=None, city_to=None, date1=None, date2=None, info=None):
    data     = search(city_from=None, city_to=None, date1=None, date2=None, info=None) #from somewhere.
    
    price, available, weather, temperature, ... = data
    
    if   domain=="price"       : return price
    elif domain=="available"   : return available
    elif domain=="temperature" : return temperature
    else : raise ValueError()

def search(city_from=None, city_to=None, date1=None, date2=None, info=None):
    cf, ct, d1, d2 = city_from, city_to, date1, date2
    
    #Go to recursive, deeper with extracted information.
    if cf or ct or d1 or d2 : return check(info=Extract_manually(utterence))
    else:
        #if there is no Start, Destination info.
        if not cf and not ct :
            make_it_utterenace(idiom[random.randint]+"[Can you] tell me where to, or where from?")
        else:
            if not d1 and not d2:
                make_it_utterenace(idiom[random.randint]+"[You gotta] tell me when you want to go. or arrive")
            else:
                return get_info(cf, ct, d1, d2)
                #get_info returns price, available, weather, temperature...

def get_info(cf, ct, d1, d2):
    price       = get_price_api(cf, ct, d1, d2)
    available   = check_free_seat(cf, ct, d1, d2)
    #temperature = @TODO

def reprompt():
    reprompt_list = ["what did you say", "Can you tell me once again", "Pardon?",]
    return random.randint(0, len(reprompt_list))
        
def intepret(utterance):
    words = utterence.split(' ')
    words.remove(All_adjective)
    
    #Here, need to use "scope_word" for find relation between two city (if there are two cities given)
    given_city = list()
    for word in words:
        for city_ in city:
            if word==city_ : given_city.append(city_)
    
    #scope, order is matter, "for" would indicate both, "to" tells destination, "from" gives origin...
    #TODO, make city order by scope.
    
    
    for word in words:
        if word in domain_sensitive_words:
            if   word in domain["price"]:
                return check("price", city_from=None, city_to=None, date1=None, date2=None)
            elif word in domain["available"]:
                return check("available", city_from=None, city_to=None, date1=None, date2=None)
            #elif...
            else :
                return reprompt()
