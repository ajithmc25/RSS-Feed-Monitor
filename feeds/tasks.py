from celery import shared_task
from celery.utils.log import get_task_logger


logger = get_task_logger(__name__)


@shared_task
def start_spider():
    logger.info("The sample task just ran.")