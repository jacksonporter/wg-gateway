FROM public.ecr.aws/docker/library/python:3.12-alpine

# # hadolint ignore=DL3008
# RUN apt-get update && apt-get upgrade -y --no-install-recommends \
#     && apt-get install -y --no-install-recommends \
#         wireguard \
#         iproute2 \
#     && apt-get autoremove -y \
#     && apt-get clean -y \
#     && rm -rf /var/lib/apt/lists/*

RUN apk update && apk upgrade \
    && apk add wireguard-tools-wg-quick \
    && apk add iptables

RUN mkdir -p /etc/wireguard/
