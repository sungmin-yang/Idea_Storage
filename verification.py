class personal_data(*args):
  face = get_Info(from_server, "face")
  finger_print = get_Info(from_server, "finger_print")
  voice =  get_Info(from_server, "voice")
  sigaature =  get_Info(from_server, "signature")
  
Alice = personal_data(personal_info + ID + pwd + Face + Finger_print)

def face(frames, Alice):
  extract_feature(frames, "face", Alice) # traditional feature + CNN, etc.
  feature_match_check(frames, "face", Alice)
  return Boolean

def finger_print(image, Alice):
  finger_feature_generator()
  finger_feature_match_check()
  return Boolean
  
def signature(frames, Alice):
  behavior1_speed_checker()
  behavior2_stopMoment_checker()
  behavior3_etc_checker()
  error_range_adjust() # individual has different error, must be customized.
  return Boolean

def voice(sound, Alice):
  # not only voice, one secret sentence must be selected individually.
  # sentence is also a key password. e.g., "the brown fox doodle inside is only matter" <- unique sentence.
  extract_feature(sound, Alice)
  compare_feature(sound, Alice)
  return Boolean

def ask_5_question(Alice):
  # question must be not related to politics or sensitive one.
  # e.g., which animal I like -> lion
  # e.g., which sport I like -> badminton
  # e.g., grandma first name and last.
  # e.g., memorable year -> 2001
  answers = select_random_5(Alice.previous_answers)
  questions = generate_answer_question(answers)
  result = []
  for q in questions:
    usr_in = input()
  if result is perfect:
    return Boolean
  else: report_server() #/ call police.
    

Witness_Jack = personal_data(personal_info + ID + pwd + Face + Finger_print)
def witness(face_input, signature_input, voice_input, Witness_Jack):
  report_to(law_firm)
  return Fail/Success
  
def get_docsign(type_of_contract):
  retrieve_from_DocSign()
  reuturn contract_docs

def report_to_government():
  
  return None
