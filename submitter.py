#!/usr/bin/env python

import argparse
import logging
import redis
import os
import glob
from urlparse import urlparse
from pycube.io.tokenizer_job_pb2 import TokenizerJobMessage

logger = logging.getLogger(__name__)


def parse_arguments():
    parser = argparse.ArgumentParser(
        description='Add audio files from audio-path to specified work queue')
    parser._optionals.title = "Options"

    parser.add_argument('-r', '--redis-server', help='The Redis instance to connect to for work.',
                        type=str, required=True)
    parser.add_argument('-src', '--work-queue', help='The queue to add work to',
                        type=str, required=True)
    parser.add_argument('-p', '--audio-path', help='Directory to find audio in',
                        type=str, required=True)
    return parser.parse_args()


def main():
    args = parse_arguments()

    # Set up connection to Redis
    rs = urlparse(args.redis_server)
    port = 6379
    if rs.port is not None:
        port = rs.port
    r = redis.StrictRedis(host=rs.hostname, port=port, db=0)
    logger.info('Connected to redis')

    files = glob.glob(os.path.join(args.audio_path, '*.sph'))
    for file in files:
        abs_path = os.path.abspath(file)
        basename = os.path.splitext(os.path.basename(abs_path))[0]
        job = TokenizerJobMessage()
        job.uid = basename
        job.audio_uri = abs_path
        logger.info('Submitting job for ' + basename)
        r.lpush(args.work_queue, job.SerializeToString())


if __name__ == '__main__':
    main()
