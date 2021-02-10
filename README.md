# etsin-finder-search

This repository contains code for Etsin Finder Search, which is used for dataset searching functionalities in Etsin. This repository has been developed using RabbitMQ and ElasticSearch.

## 1. Development setup prerequisites

1. If not installed, install docker on your computer
    - `docker.com/get-started`
2. If not installed, install docker-compose
    - `docs.docker.com/compose/install`

## 2. Development setup

1. Clone this repository, use either SSH or HTTPS (commands below)
    - `git clone git@github.com:CSCfi/etsin-finder-search.git`
    - `git clone https://github.com/CSCfi/etsin-finder-search.git`
2. Navigate to root of the cloned repository
    - `cd etsin-finder-search`
3. Retrieve app_config
    - `etsin-finder-search/app_config`
4. Run docker-compose up

# Build status

## Test branch
[![Build Status](https://travis-ci.com/CSCfi/etsin-finder-search.svg?branch=test)](https://travis-ci.com/CSCfi/etsin-finder-search)

## Stable branch
[![Build Status](https://travis-ci.com/CSCfi/etsin-finder-search.svg?branch=stable)](https://travis-ci.com/CSCfi/etsin-finder-search)

License
-------
Copyright (c) 2018-2020 Ministry of Education and Culture, Finland

Licensed under [MIT License](LICENSE)
