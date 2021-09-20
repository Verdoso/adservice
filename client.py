#!/usr/bin/python

import sys
import grpc
from demo_pb2_grpc import AdServiceStub
from demo_pb2 import AdRequest

from logging.config import fileConfig
fileConfig('logging.cfg')

import logging
log = logging.getLogger(__name__)

if __name__ == "__main__":

    channel = grpc.insecure_channel("127.0.0.1:9555")
    client = AdServiceStub(channel)

    request = AdRequest(
        context_keys = ['vintage','gardening', 'vintage']
    )

    response = client.GetAds(request)

    log.info(response)
    log.info("*********************")

    request = AdRequest()

    response = client.GetAds(request)

    log.info(response)
    log.info("*********************")
