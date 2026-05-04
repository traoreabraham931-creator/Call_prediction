from library import Call_Put_processing

address= "/Users/abrahamtraore/Desktop/Python_upskill/Options_strike_prediction/Programmes/call_put_data/"
nb_obs = 10000 # The model is trained on 10 thousand observations
processing = Call_Put_processing(address, nb_obs)
processing.load_and_format()
processing.replace_missing()
processing.save(address, "usa_options")

