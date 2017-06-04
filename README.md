# Stacks-bootstrap

This project contains scripts to bootstrap the stacks project. 

## Dependencies

You need [docker](https://docs.docker.com/engine/installation/) and php2.6+.

## What it does

It automates spinning up an instance of the stacks project. 
All the steps in described in https://github.com/stacks/stacks-website/ are included. 
The tex compiling part is done inside a docker image containing texlive 2015.
An image with apache2 and php runs the website part.

So after the project is bootstrapped, there are two docker images running:
sadar/stacks-texlive and sadar/stacks-php. The tex part of the stacks project is mounted into stacks-texlive and the website part is mounted into stacks-php. 

## How to use it
Run boostrap.sh
