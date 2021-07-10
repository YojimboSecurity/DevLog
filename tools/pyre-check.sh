#!/bin/bash

pipenv run pyre init
# pipenv run pyre analyze
pipenv run pyre check
# pipenv run pyre infer