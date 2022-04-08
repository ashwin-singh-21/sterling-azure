import os
import datetime
import schedule
import time

os.environ['TZ'] ='Asia/Kolkata'
time.tzset()

def kite_login():
    try:
        os.system("docker exec -it django1 python3 manage.py resync_creds")
        print("Kite Credentials Refreshed at :",datetime.datetime.now())
    except:
        print("Kite Login Failed!")
        pass

def rm_containers():
    try:
        os.system("docker stop $(docker ps -a -q)")
        print("Stopped all containers at :",datetime.datetime.now())
    except:
        print("Failed!")
        pass

    try:
        os.system("docker rm $(docker ps -a -q)")
        print("Removed all containers at :",datetime.datetime.now())
    except:
        print("Failed!")
        pass

def rm_celery_log():
    try:
        os.system("sudo rm celerybeat-schedule")
        print("Removed celerybeat-schedule at :",datetime.datetime.now())
    except:
        pass

    try:
        os.system("sudo rm celerybeat.pid")
        print("Removed celerybeat.pid at :",datetime.datetime.now())
    except:
        pass

def docker_build():
    try:
        os.system("docker-compose -f docker-compose-deploy.yml up -d --remove-orphans")
        print("Docker built at :",datetime.datetime.now())
    except:
        print("Docker build failed!")
        pass

def docker_restart():
    try:
        os.system("docker-compose -f docker-compose-deploy.yml restart")
        print("Docker restarted at :",datetime.datetime.now())
    except:
        print("Docker restart failed!")
        pass

schedule.every().day.at("06:15").do(kite_login)
schedule.every().day.at("06:20").do(rm_containers)
schedule.every().day.at("06:30").do(rm_celery_log)
schedule.every().day.at("06:35").do(docker_build)
schedule.every().day.at("09:00").do(docker_restart)

while True:
    schedule.run_pending()
    time.sleep(4)