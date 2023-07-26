# from celery import shared_task
# from celery.utils.log import get_task_logger
# logger = get_task_logger(__name__)
 
# @shared_task(bind=True)
# def test_first(self, data):
#     logger.info("Iv'e added first")
#     return 'done'

# @shared_task()
# def test_first():
#     logger.info("Iv'e added first")
#     return 'done'

# @shared_task()
# def notify():
#     logger.info("duely noted")
#     return 'done'