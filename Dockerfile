FROM python:3.8-slim-buster as base
RUN python -m pip install --upgrade pip

RUN apt update && apt install -y python3-dev \
                        gcc \
                        libc-dev\
                        git

RUN mkdir /fxhash_indexer/
WORKDIR /fxhash_indexer/

######################
FROM base as requirements
COPY requirements.txt /fxhash_indexer/
RUN pip install -r requirements.txt --no-cache-dir



######################
FROM requirements as sources

COPY dipdup.yml /fxhash_indexer/

RUN mkdir /fxhash_indexer/fxhash_indexer
COPY fxhash_indexer /fxhash_indexer/fxhash_indexer
COPY utils.py /fxhash_indexer/


######################
FROM sources as production
CMD python -m dipdup -c dipdup.yml run
