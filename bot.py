#importing telegram bot
import botogram
# importing nse from nse tools
from nsetools import Nse
#from datetime import datetime
import datetime, time
#importing scheduler
import schedule
# creating a Nse object
def job():
    nse = Nse()
    bnf = nse.get_index_quote("nifty bank")
    nifty = nse.get_index_quote("nifty 50")
    vix = nse.get_index_quote("INDIA VIX")
    time3 = time.strftime('%d-%b-%Y %H:%M %p', time.localtime())
    end1=("Data collected on : " + time3)
    end2=("Join: "Your channel info...")
    chan = botogram.channel("1st channel name", "bot key for 1st channel")
    chan2 = botogram.channel("2nd channel name", "Keyfor 2nd channel")
    chan.send("= = = = = = = = = = =" + '\n' +  (bnf['name']) + '\n' + "Last Price : " + str(bnf['lastPrice'])+ '\n' +  "Change in Points : " + str(bnf['change'])+'\n'  + "Change in percentage  : " + str(bnf['pChange'])+' %' + '\n' +"= = = = = = = = = = =" + '\n' + (nifty['name']) + '\n' + "Last Price : " + str(nifty['lastPrice']) + '\n' +  "Change in Points : " + str(nifty['change']) + '\n' +  "Change in percentage : " + str(nifty['pChange'])+'%' + '\n' + "= = = = = = = = = = =" + '\n' + (vix['name']) + '\n' + "Last Price : " + str(vix['lastPrice']) + '\n' +  "Change in Points : " + str(vix['change']) + '\n' +  "Change in percentage : " + str(vix['pChange'])+'%' + '\n' + "= = = = = = = = = = =" + '\n' + str(end1) + '\n' +str(end2))
    chan2.send("= = = = = = = = = = =" + '\n' +  (bnf['name']) + '\n' + "Last Price : " + str(bnf['lastPrice'])+ '\n' +  "Change in Points : " + str(bnf['change'])+'\n'  + "Change in percentage  : " + str(bnf['pChange'])+' %' + '\n' +"= = = = = = = = = = =" + '\n' + (nifty['name']) + '\n' + "Last Price : " + str(nifty['lastPrice']) + '\n' +  "Change in Points : " + str(nifty['change']) + '\n' +  "Change in percentage : " + str(nifty['pChange'])+'%' + '\n' + "= = = = = = = = = = =" + '\n' + (vix['name']) + '\n' + "Last Price : " + str(vix['lastPrice']) + '\n' +  "Change in Points : " + str(vix['change']) + '\n' +  "Change in percentage : " + str(vix['pChange'])+'%' + '\n' + "= = = = = = = = = = =" + '\n' + str(end1) + '\n' +str(end2))

def job2():
    time3 = time.strftime('%d-%b-%Y %H:%M %p', time.localtime())
    end1=("Data collected on : " + time3)
#time2 = time.strftime('%d-%b-%Y %H:%M:%S %p', time.localtime())
    print("I am running" + str(end1))

def control_job():
    #run between Mon. to Fri. and 09 ~ 16 hour/day
    tnow = datetime.datetime.now()
    hh = tnow.strftime('%H')   #hour like '09'
    wk = tnow.isoweekday() #Mon =1
    if (('08'<hh<'16') and (1 <=wk <=5)):
        job()

schedule.every(30).minutes.do(control_job)

#schedule.every(15).minutes.until("15:35").do(job2)
#schedule.every().hour.do(job2)
#schedule.every().day.at("16:23").do(job2)

while 1:
    schedule.run_pending()
    time.sleep(1)
