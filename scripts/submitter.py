#!/usr/bin/env python

import argparse
import logging
import redis
import os
import glob
from urlparse import urlparse
from kluge_bs.io.tokenizer_job_pb2 import TokenizerJobMessage

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


def parse_arguments():
    parser = argparse.ArgumentParser(
        description='Add audio files from audio-path to specified work queue')
    parser._optionals.title = "Options"

    parser.add_argument('-r', '--redis-server', help='The Redis instance (hostname:port) to connect to for work.',
                        type=str, required=True)
    parser.add_argument('-src', '--work-queue', help='The queue to add work to',
                        type=str, required=True)
    parser.add_argument('-d', '--audio-path', help='Directory to find audio in (must be mulaw 8bit/8kHz)',
                        type=str, required=True)
    parser.add_argument('-e', '--audio-ext', help='Audio extensions to look for',
                        type=str, default='.ul', required=False)
    return parser.parse_args()


def main():
    args = parse_arguments()

    # Set up connection to Redis
    logger.info('Setting up connection to redis')
    redis_server = urlparse(args.redis_server)
    default_port = redis_server.port if redis_server.port is not None else 6379
    redis_connection = redis.StrictRedis(host=redis_server.hostname, port=default_port, db=0)

    logger.info('Connected to redis')

    files = glob.glob(os.path.join(args.audio_path, '*' + args.audio_ext))
    chunk_count = 0
    for file in files:
        chunk_count += 1

        abs_path = os.path.abspath(file)
        basename = os.path.splitext(os.path.basename(abs_path))[0]
        logger.info("Found %s" % basename)
        audio_bytes = ''
        with open(abs_path, 'rb') as audio_file:
            audio_bytes = audio_file.read()

        job = TokenizerJobMessage()
        job.uid = basename
        job.language = 'english'
        job.chunk = chunk_count
        job.audio_uri = abs_path
        job.raw_audio = audio_bytes
        job.format = TokenizerJobMessage.UL
        job.sample_rate = 8000
        job.sample_size = 8
        logger.info('Submitting job for ' + basename)
        redis_connection.lpush(args.work_queue, job.SerializeToString())


if __name__ == '__main__':
    main()
