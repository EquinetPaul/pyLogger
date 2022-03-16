from time import strftime

### CONFIG
display_time = True
display_date_time = True

class bc:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

def l(msg, type):
    toDisplay = ""
    typeMsg = ""

    if type == "d":
        typeMsg = bc.OKBLUE
    elif type == "s":
        typeMsg = bc.OKGREEN
    elif type == "s2":
        typeMsg = bc.OKCYAN
    elif type == "w":
        typeMsg = bc.WARNING
    elif type == "e":
        typeMsg = bc.FAIL
    elif type == "t":
        typeMsg = bc.HEADER + bc.BOLD
    else:
        pass
    toDisplay += str(typeMsg)

    if display_date_time:
        time = strftime("%d") + "/" + strftime("%m") + "/" + strftime("%y")
        toDisplay += str(time) + " "

    if display_time:
        time = strftime("%H") + ":" + strftime("%M") + ":" + strftime("%S")
        toDisplay += str(time) + " "

    toDisplay += str(msg) + bc.ENDC

    print(str(toDisplay))
