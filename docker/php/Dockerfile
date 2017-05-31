FROM sadar/stacks-texlive:1.1.0

RUN apt-get update && apt-get install -y language-pack-en-base
RUN locale-gen en_US.UTF-8 &&\
	export LANG=en_US.UTF-8 &&\
	export LC_ALL=en_US.UTF-8
RUN apt-get install -y -f software-properties-common
RUN LC_ALL=C.UTF-8 add-apt-repository ppa:ondrej/php
RUN apt-get update && apt-get install -y -f apache2 php5.6 libapache2-mod-php php5-sqlite sqlite3 libsqlite3-dev

EXPOSE 80 443

VOLUME ["/var/www"]
ENTRYPOINT ["/bin/bash"]
#ENTRYPOINT ["/usr/sbin/apache2ctl", "-D", "FOREGROUND"]