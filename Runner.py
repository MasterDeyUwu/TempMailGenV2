import os
import json
import time
from colorama import Fore
from colorama import Style
# ------------------------------------------------------
from Code.Domains import getdomains
from Code.Randommail import randomamil
from Code.Gettoken import getinfo
from Code.getmessage import fetchmessage
from Code.getfullmsg import getfullmsg
# -----------------------------------------------------


def write_json(data):
    with open('Config.json', 'r+') as file:
        file_data = json.load(file)
        file_data.append(data)
        file.seek(0)
        json.dump(file_data, file, indent=4)
# ------------------------------------------------------


def tempgenemail(domain_json, co):
    os.system("cls")
    if co == 0:
        print(f"{Fore.GREEN} [!] Account Created {Style.RESET_ALL} \n")
    data = randomamil(
        domain_json["DOMAIN"][co]["domain"], domain_json["DOMAIN"][co]["service"])
    token_json = getinfo(data["Credentials"][0]["Mail"],
                         data["Credentials"][0]["Pass"], data["service"])
    if data["service"] == "tm":
        write_json({
            "Mail": data["Credentials"][0]["Mail"].lower(),
            "Password": data["Credentials"][0]["Pass"].lower(),
            "Service": data["service"].lower()
        })
        print(
            f"{Fore.GREEN} [!] Saved Credentials To Config.json {Style.RESET_ALL}")
    print(f"{Fore.GREEN} [!] Token Fetched {Style.RESET_ALL}")
    x = True
    while x:
        answer = input("\033[94mWant To Fetch Email ? Y/N : \033[0m")
        if answer.lower() == "y":
            os.system("cls")
            id = fetchmessage(json.loads(token_json)["token"], data["service"])
            while id == "None Email Found":
                print(f"{Fore.RED}[!]None Email Found {Style.RESET_ALL}")
                time.sleep(1)
                id = fetchmessage(json.loads(token_json)[
                                  "token"], data["service"])
                if id != "None Email Found":
                    break
            getfullmsg(id, json.loads(token_json)
                       ["token"], data["service"])
            time.sleep(1.5)
            tempgenemail(domain_json, 0)
        else:
            tempgenemail(domain_json, 0)

# ------------------------------------------------------
