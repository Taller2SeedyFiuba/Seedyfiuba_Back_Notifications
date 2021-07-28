import os
config = os.environ.copy()

for [k, v] in config.items():
  print(f"{k} : {v}")


print(f"PORT = {config['PORT']}")
