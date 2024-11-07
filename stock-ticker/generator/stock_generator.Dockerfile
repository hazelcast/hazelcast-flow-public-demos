FROM docker.io/python:3.13-slim

RUN useradd sam -m

USER sam

WORKDIR /home/sam

COPY stock_generator.requirements.txt requirements.txt
RUN pip install --user --no-cache-dir --no-warn-script-location -r requirements.txt

COPY start.sh .
COPY stock_generator.py .

# Make sure shell scripts have Unix line endings
RUN \
   tr -d '\015' <start.sh >start.sh.LF &&\
   mv start.sh.LF start.sh

ENTRYPOINT ["sh", "/home/sam/start.sh"]
CMD ["python3", "-u", "/home/sam/stock_generator.py"]
