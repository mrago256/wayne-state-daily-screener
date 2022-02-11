import dbus

try:
  interface = "org.freedesktop.Notifications"
  path = "/org/freedesktop/Notifications"
  notification = dbus.SessionBus().get_object(interface, path)
except:
  exit()

notify = dbus.Interface(notification, interface)

def sendNotif(reason):
  if reason == "":
    infoMessage = "An error occurred. Program exiting"

  else:
    infoMessage = reason

  notify.Notify("", 0, "", "AutoScreener", infoMessage, [], {"urgency": 1}, 3000)
