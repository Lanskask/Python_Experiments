import logging

logger = logging.getLogger()
logger.debug('often makes a very good meal of %s', 'visiting tourists')
# logger.log('often makes a very good meal of %s', 'visiting tourists')
logger.info('often makes a very good meal of %s', 'visiting tourists')
# logger.warn('often makes a very good meal of %s', 'visiting tourists')
print(2)

LOGGER = logging.getLogger(__name__)


def test_log1():
    logger.info('logger.info')
    logger.info('logger.debug')


def test_eggs():
    LOGGER.info('eggs info')
    LOGGER.warning('eggs warning')
    LOGGER.error('eggs error')
    LOGGER.critical('eggs critical')
    assert True
