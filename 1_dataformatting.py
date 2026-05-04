import os 
from library import Call_Put_processing

# Abraham
address= "./call_put_data/"
if os.path.exists(address+"call_usa_options.csv"):
  os.remove(address+"call_usa_options.csv")
if os.path.exists(address+"put_usa_options.csv"):
  os.remove(address+"put_usa_options.csv")
nb_obs = 10000 
processing = Call_Put_processing(address, nb_obs)
processing.load_and_format()
processing.replace_missing()
processing.save(address, "usa_options")

