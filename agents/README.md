# 1. Ensure venv is installed
$ python3 -m venv .venv

# 2. Setup the environment
$ ./setup.sh\
$ source .venv/bin/activate

# 3. Setup the api key in .env file
$ echo OPENAI_API_KEY=[key] >> .env

# 4. Run test.py to see the mock interaction
$ python3 test.py

# 5. Run chat.py to interact manually
$ python3 chat.py
