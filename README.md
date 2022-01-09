# fxdex
Indexer for fxhash based on dipdup.
This Indexer would not have been possible without DipDup and https://github.com/hicdex/hicdex .

Run ``docker-compose up`` to start the Indexer.
If this is the first run, the indexer will need some time to catch up with the tezos blockchain.
The project will expose a graphql api on port 8080 of the host machine and in the docker container.



