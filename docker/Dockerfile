FROM nvidia/cuda:11.3.1-cudnn8-devel-ubuntu20.04
ENV DEBIAN_FRONTEND "noninteractive"
ENV TZ "America/New_York"

RUN set -x \
  && echo "Preparing system..." \
  && apt-get -y update \
  && apt-get -y install \
    curl \
    git \
    python3-dev \
    python3-pip \
    openmpi-bin \
    default-jdk \
  && rm -rf /var/lib/apt/lists/* \
  && pip3 install --no-cache-dir --upgrade pip

RUN set -x \
  && echo "Installing jupyter kernel..." \
  && pip3 install --no-cache-dir ipykernel \
  && python3 -m ipykernel install

ADD requirements.txt /app/requirements.txt
RUN set -x \
 && echo "Installing python dependencies from requirements.txt..." \
 && pip3 install --no-cache-dir -r /app/requirements.txt \
 && rm /app/requirements.txt

RUN echo "ALL ALL=NOPASSWD: ALL" >> /etc/sudoers

RUN git clone https://github.com/minkyushim/TENET.git 

###############
# env variables
WORKDIR /root
ENV HOME /root
ENV PATH=$PATH:$HOME/.local/bin
EXPOSE 5000 8888 9999

CMD [ "bash" ]

