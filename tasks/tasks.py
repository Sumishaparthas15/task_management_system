from celery import shared_task
from django.core.mail import send_mail

@shared_task
def send_task_assignment_email(manager_email, to_email, task_title):
    subject = "New Task Assigned"
    message = f"You have been assigned a new task: {task_title}"
    send_mail(subject, message, manager_email, [to_email])  # Use manager's email
