Provisioning a new site
=======================

## Required packages:

* nginx
* Python 3
* Git
* pip
* virtualenv

eg, on ubuntu:

	sudo apt-get install nginx git python3 python3-pip
	sudo pip3 install virtualenv

## nginx Virtual Host Config

* see nginx.template.conf
* replace SITENAME with, eg, staging.christianprior.com

## Upstart Job

* see gunicorn-upstart.template.conf
* replace SITENAME with , eg, staging.christianprior.com

## Folder Structure:
Assume we have a user (eg chris) account at /home/chris

* /home/chris
  * sites
    * SITENAME
      * database
      * source
      * static
      * virtualenv
