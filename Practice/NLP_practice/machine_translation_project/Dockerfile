FROM tensorflow/tensorflow:latest-gpu-jupyter

RUN groupadd --gid 5000 zele95 \
    && useradd --home-dir /home/zele95 --create-home --uid 5000 \
    --gid 5000 --shell /bin/sh --skel /dev/null zele95

ENV SHELL /bin/bash