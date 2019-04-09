import logging

import dramatiq

logger = logging.getLogger(__name__)


def register_actors():

    @dramatiq.actor
    def hello_world():
        logger.info("hello world!")
