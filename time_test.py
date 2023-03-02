import time;
import datetime

def main():

    now = datetime.datetime.now()

    t1 = now.time()
    d1 = now.date()
    print(t1)
    print(d1)
    print(now)
    t2 = datetime.time(hour=7, minute=30)

    t3 = datetime.date.today()


    dt1 = datetime.datetime.combine(d1, t2)
    print(dt1)

    tdelta_1 = datetime.timedelta(hours=5, minutes=35)
    dt2 = dt1 + tdelta_1

    exit(0)

if __name__ == '__main__':
    main()
