from win10toast import ToastNotifier

toast = ToastNotifier()

def sendNotif(reason):
  if reason == "":
    infoMessage = "An error occurred. Program exiting"

  else:
    infoMessage = reason

  toast.show_toast("Autoscreener", infoMessage, duration=5)

