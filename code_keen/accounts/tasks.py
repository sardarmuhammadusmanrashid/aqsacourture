from celery import shared_task
import time
from celery.utils.log import get_task_logger
logger = get_task_logger(__name__)

@shared_task
def add(x,y):
    logger.info("taske goes to ques")
    time.sleep(10)
    print(x-y,'==========================')
    return x-y