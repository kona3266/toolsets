#!/usr/bin/env python
import logging
logging.basicConfig(format="[%(asctime)s]%(levelname)-5s %(message)s (%(filename)s:%(lineno)d)",
        datefmt="%Y-%m-%d %H:%M:%S",
        level=logging.INFO)

logger = logging.getLogger('main')
logger.setLevel(logging.DEBUG)

