import os
import time
# -----------------------------------------------------
from Code.Domains import getdomains
from Runner import tempgenemail
# ----------------------------------------------------


def loginmailgen():
    os.system("cls")
    print("""\033[94m
███████╗███╗░░░███╗░█████╗░██╗██╗░░░░░  ░██████╗░███████╗███╗░░██╗
██╔════╝████╗░████║██╔══██╗██║██║░░░░░  ██╔════╝░██╔════╝████╗░██║
█████╗░░██╔████╔██║███████║██║██║░░░░░  ██║░░██╗░█████╗░░██╔██╗██║
██╔══╝░░██║╚██╔╝██║██╔══██║██║██║░░░░░  ██║░░╚██╗██╔══╝░░██║╚████║
███████╗██║░╚═╝░██║██║░░██║██║███████╗  ╚██████╔╝███████╗██║░╚███║
╚══════╝╚═╝░░░░░╚═╝╚═╝░░╚═╝╚═╝╚══════╝  ░╚═════╝░╚══════╝╚═╝░░╚══╝ V2 updated by Dey1337\n\n\033[00m""")
    print("\033[95mLoading Email Gen.. \n ------------------------------------------------------------------\033[00m")


def createrandommail():
    domain_json = getdomains()
    domain_2 = domain_json["DOMAIN"][1]["domain"]
    tempgenemail(domain_json, 1)


if __name__ == "__main__":
    loginmailgen()
    time.sleep(1.5)
    createrandommail()