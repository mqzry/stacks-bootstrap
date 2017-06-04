# Stacks-bootstrap

This project contains scripts to bootstrap the stacks project. 

## Dependencies

You need [docker](https://docs.docker.com/engine/installation/) and php2.6+.

## What it does

It automates spinning up an instance of the stacks project. 
All the steps in described in https://github.com/stacks/stacks-website/ are included. 
The tex compiling part is done inside a docker image containing texlive 2015.
An image with apache2 and php runs the website part.

## How to use it
Run boostrap.sh
