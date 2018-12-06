FROM centos:7
MAINTAINER subflux@gmail.com

USER root
# Create app dist folder in our container
RUN mkdir /opt/primes/
COPY primes.py /opt/primes/
COPY requirements.txt /opt/primes/
RUN adduser primes \
 && chown primes:primes /opt/primes/primes.py
# Would normally install virtualenv, but Docker provides that isolation
RUN yum -y install epel-release  \
 && yum -y install python-pip \
 && pip install -r /opt/primes/requirements.txt \
 && chmod 755 /opt/primes/primes.py
USER primes
ENTRYPOINT ["/opt/primes/primes.py"]
CMD [""]
