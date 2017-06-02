FROM ubuntu:16.04
MAINTAINER Mohamed Hashi <maxamedhashi@gmail.com>

RUN apt-get update && apt-get install -y language-pack-en-base
RUN locale-gen en_US.UTF-8 &&\
	export LANG=en_US.UTF-8 &&\
	export LC_ALL=en_US.UTF-8
RUN apt-get install -y -f software-properties-common
RUN LC_ALL=C.UTF-8 add-apt-repository ppa:ondrej/php
RUN apt-get update
RUN apt-get install -y -f sqlite3
RUN apt-get install -y -f apache2
RUN apt-get update && apt-get -y -f install php5.6 libapache2-mod-php5.6 php5.6-sqlite
RUN a2enmod rewrite

EXPOSE 80 443

RUN rm -rf /var/www/html/

COPY apache.conf /etc/apache2/apache2.conf
# ENTRYPOINT ["/bin/bash"]
ENTRYPOINT ["/usr/sbin/apache2ctl", "-D", "FOREGROUND"]