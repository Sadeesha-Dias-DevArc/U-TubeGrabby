import ttkbootstrap
from ttkbootstrap.toast import ToastNotification

def displayToastNotifications(notificcation_title, notification_message, status):
    toast = ToastNotification(
        title = notificcation_title,
        message = notification_message,
        alert = True,
        duration = 7000,
        bootstyle = status,
        position = (-620, -250, 'se')
    )
    toast.show_toast()
