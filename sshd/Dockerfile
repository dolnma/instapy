FROM ubuntu:16.04

RUN apt-get update && apt-get upgrade -y
RUN apt-get update && apt-get install -y openssh-server
RUN apt-get install -y mc
RUN apt-get install -y python3-pip
RUN apt-get install -y unzip xvfb libxi6 libgconf-2-4
RUN apt-get install -y chromium-browser
RUN pip3 install instapy

# RUN mkdir /var/run/sshd
RUN mkdir /var/bot1
RUN mkdir /var/bot2
RUN mkdir /var/run/sshd
RUN echo 'root:alfa123' | chpasswd
RUN sed -i 's/PermitRootLogin prohibit-password/PermitRootLogin yes/' /etc/ssh/sshd_config

# SSH login fix. Otherwise user is kicked off after login
RUN sed 's@session\s*required\s*pam_loginuid.so@session optional pam_loginuid.so@g' -i /etc/pam.d/sshd

ENV NOTVISIBLE "in users profile"
RUN echo "export VISIBLE=now" >> /etc/profile

CMD cd ../var/bot1
CMD python3 dollysdev.py

EXPOSE 22
CMD ["/usr/sbin/sshd", "-D"]
