#!/usr/bin/python

import os
import random
import time
import traceback
from concurrent import futures
from config import PORT, MAX_ADS_TO_SERVE

import grpc

from grpc_health.v1 import health_pb2, health_pb2_grpc
import demo_pb2, demo_pb2_grpc

import AdRepository

from logging.config import fileConfig
fileConfig('logging.cfg')

import logging
log = logging.getLogger(__name__)

class AdServiceV2():
    # TODO:
    # Implemet the Ad service business logic
    def GetAds(self, request, context):
        ads = []
        if len(request.context_keys) > 0:
            log.info(f"Received request for context keys { request.context_keys }")
            temp_ads = []
            for context_key in request.context_keys:
                    log.info(f"Retrieving ads for the context key { context_key }")
                    if context_key in AdRepository.ads_by_category:
                        temp_ads.extend(AdRepository.ads_by_category[context_key])
            unique_dict = dict()
            for ad in temp_ads:
                if ad.redirect_url not in unique_dict:
                    unique_dict[ad.redirect_url] = ad
            ads = list(unique_dict.values())
        else:
            log.info(f"Received request with no context keys specified")
            ads = AdRepository.all_ads
        if len(ads) > MAX_ADS_TO_SERVE:
            ads = random.sample(ads, MAX_ADS_TO_SERVE)
        return demo_pb2.AdResponse( ads = ads);

    # Uncomment to enable the HealthChecks for the Ad service
    # Note: These are needed for the liveness and readiness probes
    def Check(self, request, context):
        return health_pb2.HealthCheckResponse(
            status=health_pb2.HealthCheckResponse.SERVING)
    #
    def Watch(self, request, context):
        return health_pb2.HealthCheckResponse(
            status=health_pb2.HealthCheckResponse.UNIMPLEMENTED)


if __name__ == "__main__":
    log.info("initializing adservice-v2")
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=2))
    # Set the server to listen to GRPC services
    demo_pb2_grpc.add_AdServiceServicer_to_server(
        AdServiceV2(), server
    )
    health_pb2_grpc.add_HealthServicer_to_server(
        AdServiceV2(), server
    )
    server.add_insecure_port(f"[::]:{PORT}")
    log.info(f"Starting gRPC server to listen for communications at port { PORT }...")
    server.start()
    log.info('...gRPC server started')
    server.wait_for_termination()
    log.info('Terminating server')
