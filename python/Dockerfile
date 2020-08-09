# FROM python:3

# WORKDIR /usr/src/app

# COPY requirements.txt ./
# RUN pip install --no-cache-dir -r requirements.txt

# COPY . .

# CMD [ "python", "./your-daemon-or-script.py" ]

FROM python:3

WORKDIR /usr/src/app

# COPY requirements.txt ./
# RUN pip install --no-cache-dir -r requirements.txt

COPY ./katas/highest_scoring_word.py .

CMD [ "highest_scoring_word.py", "-OPTIONAL_FLAG" ]