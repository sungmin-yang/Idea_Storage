EXISTING = True

def perceive(vision, sound, touch, smell, taste):
	Instant_Situation    = {vision: [], # <--- by computational vision
				sound: [],  # <--- by Sounds recognizer
				touch: [],  # <--- by wind, touch_haptic, etc
				smell: [],  # <--- by chemistrical equipments
				taste: []}  # <--- by same as smell
	
	Apperance 		 = see_some_(vision) 	# pattern, brightness, animals, rains, smog...
	Noise 	  		 = hear_some_(sound) 	# Car, Music, crying, construction site...
	Physical_Feeling 	 = feel_some_(touch) 	# pain, temperature, humid_levl...
	Scent			 = smell_some_(scent)	# perfume, poop, food, pollunated air... 
	Tasty			 = taste_some_(flavour)	# water, food, gum, juice...
	
	if Appearance is EXISTING :
		Instant_Situation['vision'].append(Appearance)
	if Noise is EXISTING :
		Instant_Situation['sound'].append(Noise)
	if Physical_Feeling is EXISTING :
		Instant_Situation['touch'].append(Physical_Feeling)
	if Scent is EXISTING :
		Instant_Situation['smell'].append(Scent)
	if Tasty is EXISTING :
		Instant_Situation['taste'].append(Tasty)
	
	return Instant_Situation

def consider(reality):
	(money, health, relationship, job, future, general) = reality
	Long_Term_Situation    = {	money: [],
				   	health: [],
				   	relationship: [],  
				   	job: [],
				   	future: [],
					general: []}
	Finance 		 = think_of_(money) 	# pattern, brightness, animals, rains, smog...
	Healthy 	  	 = think_of_(health) 	# Car, Music, crying, construction site...
	Relationship		 = think_of_(relationship) 	# pain, temperature, humid_levl...
	Career			 = think_of_(job)	# perfume, poop, food, pollunated air... 
	Future			 = think_of_(future)	# water, food, gum, juice...
	Etc 			 = think_of_(general)	# water, food, gum, juice...

	if Finance is EXISTING:
		Long_Term_Situation['money'].append(Finance)
	if Healthy is EXISTING:
		Long_Term_Situation['health'].append(Healthy)
	if Relationship is EXISTING:
		Long_Term_Situation['relationship'].append(Relationship)
		#...
		
	return Long_Term_Situation



def realize(problems):
	DANGER = None
	(money, health, relationship, job, future, general) = problems
	
	Long_Term_Situation    = {	money: [],
				   	health: [],
				   	relationship: [],  
				   	job: [],
				   	future: [],
						general: []}
	
	Finance 		 = lack_of_(money) 	# pattern, brightness, animals, rains, smog...
	Healthy 	  	 = not_physically_(health) 	# Car, Music, crying, construction site...
	Relationship		 = worry_about_(relationship) 	# pain, temperature, humid_levl...
	Career			 = fear_to_lose_(job)	# perfume, poop, food, pollunated air... 
	Future			 = not_sure_about_(future)	# water, food, gum, juice...
	Etc 			 = any_problem_in_(general)	# water, food, gum, juice...
	#DANGER will be changed to True/False inside of above 6 func.
	
	
	if Finance is in DANGER :
		Long_Term_Situation['money'].append(Finance)
	if Healthy is in DANGER :
		Long_Term_Situation['health'].append(Healthy)
	if Relationship is in DANGER :
		Long_Term_Situation['relationship'].append(Relationship)
		#...
		
		
	return Long_Term_Situation



def detect_dangerous(Situation):
	if Situation is in DANGEROUS_SITUATIONS:
		return detect_dangerous_(Situation)
	else :
		return None

