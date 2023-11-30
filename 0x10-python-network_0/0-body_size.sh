#!/bin/bash
# script that sends requests to a url
curl -sI "$1" | wc -c
