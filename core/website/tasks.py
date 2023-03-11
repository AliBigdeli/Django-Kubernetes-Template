from random import randint
from celery import shared_task



@shared_task(name="do_periodic_task")
def PeriodicTask():
    print("Periodic Task Triggered")
    SingleTask.delay(randint(1,10),randint(1,10))
    

@shared_task(name="do_single_task")
def SingleTask(a: int, b: int):
    print("Single Task Triggered")
    return a + b
