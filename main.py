import discord
import os
import time
import random
import math
import requests
from bs4 import BeautifulSoup
from keep_alive import keep_alive
from datetime import datetime
#imports


makingRole = 0
roleMaker = ""
roleName = ""
naming = 1
colouring = 1
roleChannel = ""


class MyClient(discord.Client):
    async def on_message(self, message):

      if message.author == self.user:
            return


      def truncate(number, decimals=0):
          """
          Returns a value truncated to a specific number of decimal places.
          """
          if not isinstance(decimals, int):
              raise TypeError("decimal places must be an integer.")
          elif decimals < 0:
              raise ValueError("decimal places has to be 0 or more.")
          elif decimals == 0:
              return math.trunc(number)

          factor = 10.0 ** decimals
          return math.trunc(number * factor) / factor

      def tongueTied(msgType):
          if loseYou > 4:
              inDegrees = msgType[(loseYou-4):(loseYou)]
              comeBackAround = inDegrees.find(" ")
              myWayAgain = inDegrees[comeBackAround+1:len(inDegrees)]
          else: 
              comeBackAround = msgType.find(" ")
              myWayAgain = msgType[comeBackAround+1:loseYou]
          
          return myWayAgain

      chatOne = client.get_channel(895825645358157834)

      timeChannel = client.get_channel(723445064558182420)

      if ("!roll call") in message.content.lower() and message.author.mention == "<@!491338790745669671>":
        time.sleep(1.1)
        await message.channel.send("**[vent creature noises]**")
      
      if message.content.lower().startswith("//all repeat after me: "):
          REPTmsg = message.content.replace("//all repeat after me: ","")
          time.sleep(0.5)

          await message.channel.send(REPTmsg)

      tock = time.ctime()

      
 
      birthToday = 0 
      arrival = ""

      if message.content.startswith("the witching hour is upon us") and message.channel == timeChannel:
          await timeChannel.send("**[vent creature noises!]**")
          time.sleep(2)
          
          if "Jan" in tock:
            if tock[8] == '3' and tock[9] == '0':
              #ru
              arrival = "<@502838295898750976>"
          
          if "Feb" in tock:
           if tock[8] == ' ' and tock[9] == '8':
              #roslee
              arrival = "<@294866381613170688>"

          if "Mar" in tock:
           if tock[8] == ' ' and tock[9] == '9':
              #hydria
              arrival = "<@214537651766820865>"
              
          
          if "Apr" in tock:
             if tock[8] == ' ' and tock[9] == '2':
              #darki willow
              arrival = "<@305380347338686465>` and `<@483679611545452545>"
             if tock[8] == '1' and tock[9] == '9':
              #dino
              arrival = "<@564816611148824577>"
          
          if "May" in tock:
            if tock[8] == ' ' and tock[9] == '4':
              #angel
              arrival = "<@287300871799439362>"
            if tock[8] == '1' and tock[9] == '1':
              #zino
              arrival = "<@184151441185701888>"
            if tock[8] == '1' and tock[9] == '5':
              #leo
              arrival = "<@244443769544507393>"
             
          
          if "Jun" in tock:
            yep = "yep"
           
          
          if "Jul" in tock:
            yep = "yep"
            
          
          if "Aug" in tock:
            if tock[8] == '2' and tock[9] == '7':
              #marion ashe
              arrival = "<@386572771066642432>"
            
          
          if "Sep" in tock:
            if tock[8] == ' ' and tock[9] == '9':
              #gucci
              arrival = "<@498990171392573440>"
            if tock[8] == '3' and tock[9] == '0':
              #sol
              arrival = "<@357358356400308224>"
              
          
          if "Oct" in tock:
            if tock[8] == '1' and tock[9] == '8':
              #archer
              arrival = "<@425732044211879936>"

 
              
            
          
          if "Nov" in tock:
            if tock[8] == '1' and tock[9] == '0':
              #chee
              arrival = "<@337298998354247680>"

            if tock[8] == '1' and tock[9] == '1':
              #bernz
              arrival = "<@236646068673052676>"

            if tock[8] == '1' and tock[9] == '6':
              #you, dumbass
              arrival = "<@491338790745669671>"

            if tock[8] == '1' and tock[9] == '8':
              #meek
              arrival = "<@466721297901289472>"
 

            
          if "Dec" in tock:
            if tock[8] == '2' and tock[9] == '5':
              #chrimmis
              await chatOne.send("**[christmassy vent creature noises]**\n`TRANSLATION: Merry Christmas to all Christmas-celebrators!`") 

          if arrival != "":    
            await chatOne.send("**[birthday vent creature noises]**\n`TRANSLATION: Somewhere it is " + tock[4:10] + "! So Happy Birthday `"+ arrival +"`!`") 

      


      ### timestamp shit starts here ###
            #if you want comments, check claybot!!!!!
      def dateTry(msgType):
        if (":") in msgType:

          try: #china date
            laBelle = (datetime.strptime(str(msgType), '%Y-%m-%d %H:%M').strftime('%s'))
          except:
            try: #most places date
             laBelle = (datetime.strptime(str(msgType), '%d-%m-%Y %H:%M').strftime('%s'))
            except: #american date
              laBelle = (datetime.strptime(str(msgType), '%m-%d-%Y %H:%M').strftime('%s'))
        else:

          try: #china date
            laBelle = (datetime.strptime(str(msgType), '%Y-%m-%d').strftime('%s'))
          except:
            try: #most places date
             laBelle = (datetime.strptime(str(msgType), '%d-%m-%Y').strftime('%s'))
            except: #american date
              laBelle = (datetime.strptime(str(msgType), '%m-%d-%Y').strftime('%s'))
        laBelle = float(laBelle)
          
        return laBelle 
      
      msgStamp = message.content.lower().replace(" year","year")
      msgStamp = msgStamp.replace(" month","month")
      msgStamp = msgStamp.replace(" day","day")
      msgStamp = msgStamp.replace(" hour","hour")
      msgStamp = msgStamp.replace(" min","min")  
      msgStamp = msgStamp.replace("plus","+")
      msgStamp = msgStamp.replace(" +","+")
      msgStamp = msgStamp.replace("/","-")
      msgStamp = msgStamp.replace("\\","-")
      msgStamp = msgStamp.replace("utc","gmt")
      msgStamp = msgStamp.replace("gmt-","-")
      msgStamp = msgStamp.replace("gmt+","+")
      #^ these three lines are leo-proofing 
      if ("copy") in msgStamp:
            copy = 1
            msgStamp= msgStamp.replace("copy","")
      else:
            copy = 0
      msgStamp = msgStamp.replace(".30",".5")
      msgStamp = msgStamp.replace(".45",".75")
      #bc the hours are * w their timezone thing so 30 mins needs to be 1/2
      msgStamp = msgStamp.replace("  "," ")
      msgStamp = msgStamp.replace("   "," ")
      #keep these last 

      if ("$timestamp") in msgStamp or ("$guide") in msgStamp:
        embed=discord.Embed(title="✨POTES' FUNKY TIMESTAMP MACHINE✨", description="a guide!!\n ​", color=0xff7870)
        embed.add_field(name="**TIMESTAMPS**", value="The timestamp function creates a time that automatically translates between different timezones! Useful for arranging events for people in different timezones!  the function uses this format: **'timestamp: DD-MM-YYYY HH:MM (TZ)''**\n Timezones can be done in their letter code (NZDT) or offset from gmt (+13)!\n `timestamp: 31/12/1999 14:32 (GMT)`\n ​", inline=False)
        embed.add_field(name="**TIMESTAMP EXTRAS**", value="If you add **[R]** to the end of your timestamp message, the timestamp will take the format of an active countdown!\n Add **[F]** and it'll be a longer format!\n Add **[U]** and it'll tell you how many seconds it's been since 1970 (aka epoch format)\n `timestamp: 31/12/1999 14:32 (GMT) [R]`\n ​", inline=False)
        embed.add_field(name="**COPYING**", value="If you add 'copy' to the message after timestamp, the bot will give you the plaintext timestamp, so you can copy/paste it easily!\n `timestamp: copy 31/12/1999 14:32 (GMT)`\n ​", inline=False)
        embed.add_field(name="**WHAT TIME IS IT IN X TIMEZONE?**", value="**'timestamp: now (TZ)'** will show you (in text-format) what time it currently is in that timezone!\n `timestamp: now (NZST)`\n ​", inline=False)
        embed.add_field(name="**TIMEBETWEEN**", value="Works out the difference between two times, separate by a #!\n `timebetween:  26/07/1768 # 21/12/2012`\n `timebetween:  26/07/1768 # now`\n ​", inline=False)
        embed.add_field(name="**TIMESTAMP PLUS**", value="Timestamp plus allows you to see what the datetime will be x time from now will be!\n `timestamp plus: 5 days 6 hours 8 minutes`\n ​", inline=False)
        embed.set_footer(text="the things in boxes are examples")
        await message.channel.send(embed=embed)
   

   
      if msgStamp.startswith("timestamp+:"):          
          bustle = 0

          if ("year") in msgStamp:
            loseYou  = msgStamp.find("year")            
            bustle = bustle + float(tongueTied(msgStamp)) * 3.154e+7

          if ("month") in msgStamp:
            loseYou  = msgStamp.find("month")            
            bustle = bustle + float(tongueTied(msgStamp)) * 2.628e+6      
         
          if ("day") in msgStamp:
            loseYou  = msgStamp.find("day")            
            bustle = bustle + float(tongueTied(msgStamp)) * 86400

          if ("hour") in msgStamp:
            loseYou  = msgStamp.find("hour")            
            bustle = bustle + float(tongueTied(msgStamp)) * 3600
            
          if ("min") in msgStamp:
            loseYou  = msgStamp.find("min")            
            bustle = bustle + float(tongueTied(msgStamp)) * 60          
          
          laBelle = int(time.time() + bustle)
          await message.channel.send("<t:"+str(laBelle)+":f>")


      
      if msgStamp.startswith("timestamp: "): 
          msgStamp = msgStamp.replace("timestamp: ","")
          mafs = 1
          timezone = 0   
          tZed = ""
          seeTime = 0
          stampType = ":f>"
          
          try: #this is the general try
            if ("[") in msgStamp and ("]") in msgStamp:
              frontBr  = msgStamp.find("[")
              backBr = msgStamp.find("]") 
              if ("f") in msgStamp[frontBr+1:backBr]:
                stampType = ":F>"
              elif ("r") in msgStamp[frontBr+1:backBr]:
                stampType = ":R>"
              elif ("u") in msgStamp[frontBr+1:backBr]:
                stampType = ""
              msgStamp = msgStamp[0:frontBr-1]
              
            if ("(") in msgStamp and (")") in msgStamp:
              frontBr  = msgStamp.find("(")
              backBr = msgStamp.find(")") 
              if msgStamp[backBr-1].isdigit():
                if msgStamp[frontBr+1] =="+" or msgStamp[frontBr+1] =="-":
                  if msgStamp[frontBr+1] =="+":
                    mafs = -1
                  timezone = tZed = msgStamp[frontBr+2:backBr]
                else:
                  timezone = tZed = msgStamp[frontBr+1:backBr]
                
              else:
                #OKAY SO THIS IS WHERE THE CASES WOULD GO. whenever u decide to make them    
                tZed = (msgStamp[frontBr+1:backBr]).upper()
                if tZed == "IDLW":                  
                  timezone = 12
                elif tZed == "SST":                 
                  timezone = 11
                elif tZed == "HST":                  
                  timezone = 10
                elif tZed == "HDT" or tZed == "AKST":                
                  timezone = 9
                elif tZed == "AKDT" or tZed == "PST":                  
                  timezone = 8
                elif tZed == "MST" or tZed == "PDT":                  
                  timezone = 7
                elif tZed == "MDT" or tZed == "CST":                  
                  timezone = 6
                elif tZed == "CDT" or tZed == "EST":                  
                  timezone = 5
                elif tZed == "AST" or tZed == "EDT":                  
                  timezone = 4
                elif tZed == "ADT" or tZed == "EDT":                  
                  timezone = 3
                elif tZed == "NST":                 
                  timezone = 3.5
                elif tZed == "NDT":                  
                  timezone = 2.5
                elif tZed == "GMT" or tZed == "WET"or tZed == "UTC":
                  #NO NEED FOR MAFS WHEN ITS DEFAULT 1
                  timezone = 0
                elif tZed == "BST" or tZed == "WEST" or tZed == "CET" or tZed == "IST" or tZed == "MET" or tZed == "WAT":
                  mafs = -1
                  timezone = 1
                elif tZed == "CEST" or tZed == "MEST" or tZed == "CAT" or tZed == "EET" or tZed == "SAST":
                  mafs = -1
                  timezone = 2
                elif tZed == "EEST" or tZed == "WET"or tZed == "EAT"or tZed == "MSK":
                  mafs = -1
                  timezone = 3
                elif tZed == "PKT":
                  mafs = -1
                  timezone = 5
                elif tZed == "IST":
                  mafs = -1
                  timezone = 5.5
                elif tZed == "WIB":
                  mafs = -1
                  timezone = 7
                elif tZed == "AWST"or tZed == "HKT"or tZed == "WITA":
                  mafs = -1
                  timezone = 8
                elif tZed == "KST"or tZed == "WIT":
                  mafs = -1
                  timezone = 9
                elif tZed == "ACST":
                  mafs = -1
                  timezone = 9.5
                elif tZed == "ACDT":
                  mafs = -1
                  timezone = 10.5
                elif tZed == "AEST"or tZed == "CHST":
                  mafs = -1
                  timezone = 10
                elif tZed == "AEDT":
                  mafs = -1
                  timezone = 11
                elif tZed == "NZST":
                  mafs = -1
                  timezone = 12
                elif tZed == "NZDT":
                  mafs = -1
                  timezone = 13       

                else:
                  await message.channel.send("***[confused vent creature noises]***\n `TRANSLATION: Friend, I cannot find this timezone!`")
                  return             
              msgStamp = msgStamp[0:frontBr-1]
            
            timzer =  mafs * (3600 *float(timezone))
            
            if ("now") in msgStamp:
              laBelle = int(time.time())
              print("mafs = " +str(mafs))
              print(time.ctime())
              if tZed != "":
                seeTime = 1
                timzer = -timzer
              else:
                seeTime = 0
            else:
              laBelle = dateTry(msgStamp)
              
            laBelle = int(laBelle + timzer)
            print(time.ctime(laBelle))
            print(laBelle)

            if seeTime == 0:
              if copy == 1:
                await message.channel.send("\<t:"+str(laBelle)+stampType+ " \n(Preview: <t:"+str(laBelle)+stampType+")")
              else:
                await message.channel.send("<t:"+str(laBelle)+stampType)
            else:
              await message.channel.send(time.ctime(laBelle)[0:])
          except: #this is the general except
            await message.channel.send("***[confused vent creature noises]***\n`TRANSLATION: Friend, I cannot fit this time in my mouth! Make it a different shape (ie 31-12-1982 14:30 (GMT)`")
            #await message.channel.send("Timestamp error! Make sure format is correct (DD-MM-YYYY HH:MM (TZ) -- ie `31-12-1982 14:30 (GMT)`")

      
      if msgStamp.startswith("timebetween: ") and (" # ") in msgStamp: 
        msgStamp = msgStamp.replace("timebetween: ","")
        hash  = msgStamp.find(" # ")
        timeOne = msgStamp[0:hash]
        timeTwo = msgStamp[hash+3:len(msgStamp)]
        
        if ("now") in timeOne:
          epochOne = int(time.time())
        else:
          epochOne = dateTry(timeOne)
        
        if ("now") in timeTwo:
          epochTwo = int(time.time())
        else:
          epochTwo = dateTry(timeTwo)

        if epochOne >= epochTwo:
          epoque = epochOne - epochTwo
        else:
          epoque =  epochTwo - epochOne

        laBelleEpoch = [epoque,0]

        def divideEp(by):
          if by <= laBelleEpoch[0]:
            divver = int(laBelleEpoch[0] / by)
            laBelleEpoch[0] = laBelleEpoch[0] - (by * divver)
          else:
            divver = 0
          
          return [laBelleEpoch[0], divver]

        laBelleEpoch = divideEp(3.154e+7)
        years = str(laBelleEpoch[1]) + " years, "
        
        laBelleEpoch = divideEp(2.628e+6)
        months = str(laBelleEpoch[1]) + " months, "        

        laBelleEpoch = divideEp(604800)
        weeks = str(laBelleEpoch[1]) + " weeks, "

        laBelleEpoch = divideEp(86400)
        days = str(laBelleEpoch[1]) + " days, "

        laBelleEpoch = divideEp(3600)
        hours = str(laBelleEpoch[1]) + " hours, "

        laBelleEpoch = divideEp(60)
        mins = "and " + str(laBelleEpoch[1]) + " minutes."

        timeSince = ""
        timeList = [years, months, weeks, days, hours, mins]
        
        for i in timeList:
          if i.startswith("0") or i.startswith("and 0"):
            i = ""
          else: 
            timeSince = timeSince + i

        

        if timeSince == "":
          timeSince = " minutes."
        elif timeSince[len(timeSince)-1]== " ":
          timeSince = timeSince[0:len(timeSince)-2] + "."
        
              

        await message.channel.send(timeSince)
                
         
     
      
      ### conversions start here ###
      msgImperial = message.content.lower().replace('"',"inch")
      msgImperial = msgImperial.replace("'","ft")
      msgImperial = msgImperial.replace("cm","centimetre")
      msgImperial = msgImperial.replace("meter","metre")
      msgImperial = msgImperial.replace("metres","metre")
      msgImperial = msgImperial.replace(" metre","metre")
      msgImperial = msgImperial.replace("m","metre")     
      msgImperial = msgImperial.replace("inches","inch")
      msgImperial = msgImperial.replace("”","inch")
      msgImperial = msgImperial.replace("’","ft")
      msgImperial = msgImperial.replace("“","inch")
      msgImperial = msgImperial.replace("foot","ft")
      msgImperial = msgImperial.replace("feet","ft")
      msgImperial = msgImperial.replace("km","kilometre")
      msgImperial = msgImperial.replace("kilometer","kilometre")     
      msgImperial = msgImperial.replace(" metre ","metre")
      msgImperial = msgImperial.replace(" ft","ft")
      msgImperial = msgImperial.replace(" inch","inch")
      msgImperial = msgImperial.replace(" centimetre","centimetre")
      msgImperial = msgImperial.replace(" kilometre","kilometre")
      msgImperial = msgImperial.replace("metreile","mile")
      msgImperial = msgImperial.replace(" mile","mile")
      msgImperial = msgImperial.replace("ft","ft ")
      msgImperial = msgImperial.replace("metreetre","metre")
      
      msgImperial = msgImperial.replace("metre.","metre ")
      msgImperial = msgImperial.replace("metre!","metre ")
      msgImperial = msgImperial.replace("metre,","metre ")
      msgImperial = msgImperial.replace("metre:","metre ")
      msgImperial = msgImperial.replace("(","")
      msgImperial = msgImperial.replace(")","")
      
      
    
      if ("ft") in msgImperial:
        loseYou  = msgImperial.find("ft")
        x = msgImperial.count("ft")
        counted = 0
        minusLength = msgImperial
        
        
        while counted <= x:
          if minusLength[loseYou-1].isdigit():
            meety = 1           
          else: 
            meety = 0
            minusLength = minusLength[loseYou+3:len(minusLength)]
            loseYou  = minusLength.find("ft")
          counted = counted + 1
        
        #finds the loc of the start of ft
        if meety == 1:
          myWayAgain = tongueTied(minusLength)
          
        if ("inch") in msgImperial:
          loseYou  = msgImperial.find("inch")
          x = msgImperial.count("inch")
          counted = 0
          minusLength = msgImperial
          
          while counted <= x:
            if minusLength[loseYou-1].isdigit():
              meety = 1           
            else: 
              meety = 0
              minusLength = minusLength[loseYou+1:len(msgImperial)]
              loseYou  = minusLength.find("inch")
            counted = counted +1

          if meety == 1:
            inchWay = tongueTied(minusLength)
            myWayAgain = float(myWayAgain) + (float(inchWay)/12)
        
        #in back into decimal, add to ft so minimal ifs and maths 
        seeMe = (float(myWayAgain)) / 3.281

        ifYouPlease = round(seeMe,2)
        myWayAgain = round(float(myWayAgain),2)
        await message.channel.send("*("+ str(myWayAgain)+"ft is " + str(ifYouPlease)+ "m)*")

      elif ("inch") in msgImperial:
          loseYou  = msgImperial.find("inch")
          x = msgImperial.count("inch")
          counted = 0
          minusLength = msgImperial
          
          while counted <= x:
            if minusLength[loseYou-1].isdigit():
              meety = 1           
            else: 
              meety = 0
              minusLength = minusLength[loseYou+1:len(msgImperial)]
              loseYou  = minusLength.find("inch")
            counted = counted +1

          if meety == 1: 
            inchWay = tongueTied(msgImperial)
            seeMe = (float(inchWay)) * 2.54
            ifYouPlease = round(seeMe,2)    
            await message.channel.send("*("+ str(inchWay)+" inches is " + str(ifYouPlease)+ "cm)*")
      
      if ("mile") in msgImperial:
        loseYou  = msgImperial.find("mile")

        myWayAgain = tongueTied(msgImperial)

        seeMe = (float(myWayAgain)) * 1.609
        ifYouPlease = round(seeMe,2)
        await message.channel.send("*("+ str(myWayAgain)+" miles is " + str(ifYouPlease)+"km)*")
      
      
      if ("centimetre") in msgImperial:
        loseYou  = msgImperial.find("centimetre")

        myWayAgain = tongueTied(msgImperial)

        seeMe = (float(myWayAgain)) /2.54
        ifYouPlease = round(seeMe,2)
        
        await message.channel.send("*("+ str(myWayAgain)+"cm is " + str(ifYouPlease)+" inches)*")
      
      elif ("kilometre") in msgImperial:
        loseYou  = msgImperial.find("kilometre")

        myWayAgain = tongueTied(msgImperial)

        seeMe = (float(myWayAgain)) /1.609
        ifYouPlease = round(seeMe,2)
        
        await message.channel.send("*("+ str(myWayAgain)+"km is " + str(ifYouPlease)+" miles)*")

      
      elif ("metre ") in msgImperial or msgImperial.endswith("metre"):
        loseYou  = msgImperial.find("metre")
        
        x = msgImperial.count("metre")
        counted = 0
        minusMetre = msgImperial
        
        while counted <= x:
          if minusMetre[loseYou-1].isdigit():
            meety = 1
          else: 
            meety = 0
            minusMetre = minusMetre[loseYou+1:len(msgImperial)]
            loseYou  = minusMetre.find("metre")
          counted = counted +1
        
        if meety == 1:
          myWayAgain = tongueTied(minusMetre)
  
          seeMe = (float(myWayAgain)) * 3.281
          ifYouPlease = int((seeMe - int(seeMe)) *12)
          
          await message.channel.send("*("+ str(myWayAgain)+"m is " + str(int(seeMe))+ "'"+ str(ifYouPlease)+"”)*")

    #temp convert
      msgDEG = message.content.lower().replace("°","*")
      msgDEG = msgDEG.replace(" degrees ","*")

        
      if ("*f") in msgDEG:          
          loseYou  = msgDEG.find("*f")
          myWayAgain = tongueTied(msgDEG)
          seeMe = (int(myWayAgain)-32)/1.8
          ifYouPlease = round(seeMe)
          await message.channel.send("*("+ str(myWayAgain)+"°F is " + str(ifYouPlease)+ "°C.)*")
        


      if ("*c") in msgDEG:
          loseYou  = msgDEG.find("*c")
          myWayAgain = tongueTied(msgDEG)
          seeMe = (int(myWayAgain)*1.8)+32
          ifYouPlease = round(seeMe)
          await message.channel.send("*("+ str(myWayAgain)+"°C is " + str(ifYouPlease)+ "°F.)*")
      
      

      ### actual message stuff ###

      
      VENTmsg = message.content.lower().replace(',', '')
      VENTmsg = VENTmsg.replace('*', '')
      VENTmsg = VENTmsg.replace('~', '')
      VENTmsg = VENTmsg.replace('`', '')
      VENTmsg = VENTmsg.replace('|', '')
      VENTmsg = VENTmsg.replace('.', '')
      VENTmsg = VENTmsg.replace('_', '')
      VENTmsg = VENTmsg.replace(' ', '')
      VENTmsg = VENTmsg.replace("i'm", "im")
      VENTmsg = VENTmsg.replace("iam", "im")
      VENTmsg = VENTmsg.replace("'", "")
      VENTmsg = VENTmsg.replace("you", "u")
      VENTmsg = VENTmsg.replace("canyougive", "give")
      VENTmsg = VENTmsg.replace("thanku", "thanks")
      VENTmsg = VENTmsg.replace("!", "")
      VENTmsg = VENTmsg.replace("thankssomuch", "thanks")
      VENTmsg = VENTmsg.replace('iwill', 'ill')
      VENTmsg = VENTmsg.replace("image", "img")
      VENTmsg = VENTmsg.replace("meekwhen", "")
      VENTmsg = VENTmsg.replace("just", "")
      VENTmsg = VENTmsg.replace("venty", "vent")
      VENTmsg = VENTmsg.replace("theventcreature", "uvent")
      VENTmsg = VENTmsg.replace("ventcreature", "vent")
      VENTmsg = VENTmsg.replace("ueue", "soung")



      LOVmsg = VENTmsg.replace("we", "i")
      LOVmsg = LOVmsg.replace("andappreciate ", "")
      LOVmsg = LOVmsg.replace("andrespects", "")
      LOVmsg = LOVmsg.replace(":", "")

      LOVmsg = LOVmsg.replace("lvoe", "lov")
      LOVmsg = LOVmsg.replace("love", "lov")
      LOVmsg = LOVmsg.replace("lvoe", "lov")
      LOVmsg = LOVmsg.replace("vole", "lov")
      LOVmsg = LOVmsg.replace("vole", "lov")
      LOVmsg = LOVmsg.replace("olve", "lov")
      LOVmsg = LOVmsg.replace("vloe", "lov")
      LOVmsg = LOVmsg.replace("vloe", "lov")
      LOVmsg = LOVmsg.replace("lveo", "lov")
      LOVmsg = LOVmsg.replace("elov", "lov")
      LOVmsg = LOVmsg.replace("vleo", "lov")
      LOVmsg = LOVmsg.replace("levo", "lov")
      LOVmsg = LOVmsg.replace("ovel", "lov")
      LOVmsg = LOVmsg.replace("live", "lov")
      LOVmsg = LOVmsg.replace("loive", "lov")
      LOVmsg = LOVmsg.replace("lovdd", "lovd")
      LOVmsg = LOVmsg.replace("loev", "lovd")
      LOVmsg = LOVmsg.replace("ily", "ilovu")
      LOVmsg = LOVmsg.replace("okay", "ok")
      LOVmsg = LOVmsg.replace("alright", "ok")
      LOVmsg = LOVmsg.replace("are", "r")
      LOVmsg = LOVmsg.replace("good", "ok")
      LOVmsg = LOVmsg.replace("gud", "ok")
      



      if ("lovuvent") in LOVmsg or ("ventilovu") in LOVmsg or (
          "ilovvent") in LOVmsg or ("ventruawrthatilovu") in LOVmsg:
        time.sleep(0.3)
        await message.channel.send("***[loving vent creature noises]***\n`TRANSLATION: I love you too, Friend!`")

      elif ("lovutoovent") in LOVmsg or ("lovu2vent") in LOVmsg:
        time.sleep(0.3)
        await message.channel.send('***[loving vent creature noises]***\n`TRANSLATION: happy face!`')
      
      if ("thanksvent") in LOVmsg:
        time.sleep(0.3)
        await message.channel.send("***[happy vent creature noises]***\n`TRANSLATION: You're welcome, Friend!`")

      if ("howtallisapomeranian") in VENTmsg:
        time.sleep(0.3)
        await message.channel.send("***[intelligent vent creature noises]***\n`TRANSLATION: 12 minutes!`")


      ### DIRECTORY ###
      
      if (">>directory") in VENTmsg or (">>imgdirectory") in VENTmsg:
        await message.channel.send("- affleck\n- angstclub\n- arlix sign\n- bowden\n- but meek can\n- cringe robber/ 999\n- good for her\n- good for him\n- good for them\n- fluff attempted\n- hit da bricks\n- hold on cat\n-i am the cool\n- i just think they're neat\n- i love arm\n- lesbianism\n- meekotes v zino\n- pepe silvia\n- short kings only \n- twitter guy\n-ueueue\n- well actually\n- YOU\n- zinomeek")

      if (">>holdon") in VENTmsg:
        time.sleep(0.3)
        await message.channel.send("https://cdn.discordapp.com/attachments/895827132486418493/1057799605703692350/EUfn1vEWkAAQm9o.png") 

      if (">>lesbianism") in VENTmsg:
        time.sleep(0.3)
        await message.channel.send("https://cdn.discordapp.com/attachments/895827143399968849/1186091685290188850/Screenshot_2023-12-17-18-44-38-748.jpg") 

      if (">>soung") in VENTmsg or (">>soundofcrying") in VENTmsg :
        time.sleep(0.3)
        await message.channel.send("https://cdn.discordapp.com/attachments/895826521208541224/1010588089661542432/Tumblr_l_196848676007764.png") 

      if (">>imthecool") in VENTmsg or (">>leoisthecool") in VENTmsg:
        time.sleep(0.3)
        await message.channel.send("https://media.discordapp.net/attachments/895826521208541224/1004510975996723311/IMG_8139.png")
        

      if (">>arlixsign") in VENTmsg:
        time.sleep(0.3)
        await message.channel.send("https://cdn.discordapp.com/attachments/494943280522461185/998652801636892702/image0.jpg")

      if (">>meekotesvzino") in VENTmsg:
        time.sleep(0.3)
        await message.channel.send("https://cdn.discordapp.com/attachments/895827563451150367/998653119082811532/IMG_7757.jpg")
      
      if (">>exhibita") in VENTmsg:
        time.sleep(0.3)
        await message.channel.send("https://tenor.com/view/arno-dorian-gif-5557877")

      if (">>butshecan") in VENTmsg or (">>butmeekcan") in VENTmsg:
        time.sleep(0.3)
        await message.channel.send("https://cdn.discordapp.com/attachments/895827122453643344/994950786473791528/IMG_9709.jpg")

      if (">>shortkingsonly") in VENTmsg:
        time.sleep(0.3)
        await message.channel.send("https://media.discordapp.net/attachments/897490320319717396/980206504462418001/unknown.png")

      if (">>ripzino") in VENTmsg:
        time.sleep(0.3)
        await message.channel.send("https://cdn.discordapp.com/attachments/494943280522461185/963011406922395678/unknown.png")

      if (">>ripmeek") in VENTmsg:
        time.sleep(0.3)
        await message.channel.send("https://cdn.discordapp.com/attachments/494943280522461185/963013012577480744/unknown.png")
      
        

      if (">>twitterguy") in VENTmsg or (">>everygoddamnday") in VENTmsg or (">>thatguy") in VENTmsg:
        time.sleep(0.3)
        await message.channel.send("https://cdn.discordapp.com/attachments/895827563451150367/944004111723028570/ENYBh2yXsAIioOr.png")

      if (">>angstclub") in VENTmsg or (">>theangstclub") in VENTmsg:
        time.sleep(0.3)
        await message.channel.send("https://cdn.discordapp.com/attachments/494943280522461185/906223641736384552/angst_club.gif")
      
      if (">>bowden") in VENTmsg:
        time.sleep(0.3)
        await message.channel.send("https://cdn.discordapp.com/attachments/895827711958847538/909736932131618836/IMG_6608.jpg")

      if (">>fluffattempted") in VENTmsg:
        time.sleep(0.3)
        await message.channel.send("https://cdn.discordapp.com/attachments/895826521208541224/949648543713468476/0FBC3C92-BA4C-4317-9593-F58E0824F7AF.png")
      
      if (">>hitdabricks") in VENTmsg:
        time.sleep(0.3)
        await message.channel.send("https://cdn.discordapp.com/attachments/494943280522461185/932704509308854272/D5_JBL0X4AANg10.png")
      

      if (">>hydrianoise") in VENTmsg:
        time.sleep(0.3)
        await message.channel.send("https://cdn.discordapp.com/attachments/895827711958847538/917212791893557278/video0_5.mov")

      if (">>afflock") in VENTmsg or (">>affleck") in VENTmsg or (">>benaf") in VENTmsg:
        time.sleep(0.3)
        if ("466721297901289472") in message.author.mention: 
          await message.channel.send("https://cdn.discordapp.com/attachments/895827563451150367/941395388542378004/Sherlock_Affleck.jpg")
        else:
          await message.channel.send("https://cdn.discordapp.com/attachments/494943280522461185/998880958252072960/unknown.png")

      
      if (">>ithinktheyreneat") in VENTmsg:
        time.sleep(0.3)
        await message.channel.send("https://cdn.discordapp.com/attachments/895827143399968849/927922667007406161/572.png")

      if (">>pepesilvia") in VENTmsg or (">>pepesilva") in VENTmsg:
        time.sleep(0.3)
        if ("466721297901289472") in message.author.mention: 
          await message.channel.send("https://cdn.discordapp.com/attachments/786059077205098527/939164947965964388/IMG_7989.png")
        else:
          await message.channel.send("https://cdn.discordapp.com/attachments/494943280522461185/941396494974603274/tumblr_o16n2kBlpX1ta3qyvo1_1280.png")
          
        
      
      if (">>ilovearm") in VENTmsg:
        time.sleep(0.3)
        await message.channel.send("https://cdn.discordapp.com/attachments/494943280522461185/921840933476114492/i_love_arm.png")
      
      if (">>goodforher") in VENTmsg:
        time.sleep(0.3)
        await message.channel.send("https://tenor.com/view/good-for-her-arrested-development-lucille-gif-13775712")
      
      if (">>goodforhim") in VENTmsg:
        time.sleep(0.3)
        await message.channel.send("https://media.discordapp.net/attachments/519968301561151500/853317115922350120/good_for_him.gif")
      
      if (">>goodforthem") in VENTmsg:
        time.sleep(0.3)
        await message.channel.send("https://media.discordapp.net/attachments/519968301561151500/853318456781832192/good_for_them.gif")
      
      if (">>999") in VENTmsg or (">>cringerobber") in VENTmsg or (">>sirthisrobberiscringe") in VENTmsg:
        time.sleep(0.3)
        await message.channel.send("https://cdn.discordapp.com/attachments/895827041704869919/937468349259059220/burglary-crime-culprit-victim-security-disguised-burglar-breaking-apartment-office-women-calling-police-33399556.png")
      
      if (">>u") in VENTmsg:
        time.sleep(0.3)
        await message.channel.send("https://cdn.discordapp.com/attachments/895825645358157834/916513062981357588/tumblr_d1c8c94f307d6e04075f3ec5c5d9cb4b_0edc10e1_12801.jpg")

      if (">>wellactually") in VENTmsg:
        time.sleep(0.3)
        await message.channel.send("https://cdn.discordapp.com/attachments/895825655751647252/919066478127509596/well_actually.gif")
        
      
      if (">>zinomeek") in VENTmsg:
        time.sleep(0.3)
        await message.channel.send("https://cdn.discordapp.com/attachments/895825655751647252/925894168147034112/FEFB7051-6DB4-4EA5-A498-B06D38124E47.jpg")

      #ao3 bot
      if ("https://archiveofourown.org/works/") in message.content.lower():

          linkPos  = message.content.lower().find("https://archiveofourown.org/works/")
          
          newLine = message.content.lower()[linkPos:len(message.content)]
          
          if " " in newLine: 
           endPos = newLine.find(" ") + linkPos
          else:
            endPos = len(message.content)
            print(endPos)
            
            
          url = message.content.lower()[linkPos:endPos]
          print(url)
          
          #url='https://archiveofourown.org/works/36124516/chapters/90050128'
          resp=requests.get(url)
          soup=BeautifulSoup(resp.text,'html.parser')


          

          def archiveLimb(limb):
            l=soup.find("dd",{"class":limb})
            
            theKing = ""
            count = 0
            for i in l.findAll("a"):
              if count > 0: 
                theKing = theKing + (", "+(i.text))
              else: 
                theKing = theKing + ((i.text))
              count = count + 1
            return theKing
              
            #return(l.text)"""
            

          def archiveBoth(start,limb):
            l=soup.find(start,{"class":limb}) 
            return(l.text)

          def archiveMod(start,limb):
            l=soup.find(start,{"class":limb}) 
            z=l.find("blockquote",{"class":"userstuff"}) 
            return(z.text)


          #http_respone 200 means OK status
          print(resp.status_code)

          
          try: 
    

            author = "By " + archiveBoth("h3","byline heading")
            author = ' '.join(author.splitlines())
            embed=discord.Embed(title=archiveBoth("h2","title heading"), url=url, description=(author), color=0xff2424)
            embed.set_thumbnail( url="https://archiveofourown.org/images/ao3_logos/logo.png")
            embed.set_author(name=("Archive Of Our Own"),       icon_url="https://archiveofourown.org/images/ao3_logos/logo.png")
            embed.add_field(name="Rating:", value=(archiveLimb("rating tags")), inline=True)
            embed.add_field(name="Warning:", value=(archiveLimb("warning tags")), inline=True)
            try: 
              embed.add_field(name="Categories:", value=(archiveLimb("category tags")), inline=True)
            except:
              x = "y"
            embed.add_field(name="Fandoms:", value=(archiveLimb("fandom tags")), inline=False)
            try: 
              embed.add_field(name="Relationships:", value=(archiveLimb("relationship tags"))[0:1023], inline=False)
            except:
              x = "y"
            embed.add_field(name="Characters:", value=(archiveLimb("character tags"))[0:1023], inline=False)
            embed.add_field(name="Additional tags:", value=(archiveLimb("freeform tags"))[0:1023], inline=False)
            try: 
              embed.add_field(name="Summary:", value=(archiveMod("div","summary module"))[0:1023], inline=False)
            except:
              x = "y"
            try: 
               embed.add_field(name="Series:", value=(archiveLimb("series")), inline=False)
            except:
              x = "y"
            
            embed.set_footer(text="Words: " + archiveBoth("dd","words") + " | Chapters: "+ archiveBoth("dd","chapters")+ " | Published: "+ archiveBoth("dd","published"))
            
            
            

            await message.channel.send(embed=embed)
          
        

          except:
            await message.channel.send("***[confused vent creature noises]***\n `TRANSLATION: Friend, this link smells funny!`")
      


      




    async def on_ready(game): #status
        watching = discord.Activity(name='over the Ventlings', type=discord.ActivityType.watching)
        playing = discord.Activity(name='with the Ventlings', type=discord.ActivityType.playing)
        activities = [watching,playing]
        await client.change_presence(activity=activities[random.randint(0,len(activities)-1)])

    async def on_member_join(client, member):

        willkommen = client.get_channel(895828976411496449) 
        time.sleep(0.7)
        await willkommen.send("***[unintelligible vent creature noises]***\n `TRANSLATION: Welcome to the server, friend `" +  member.mention + "`!`\n `Feel free to (re)introduce yourself in `<#895826388500742205>`!`")
        time.sleep(0.5)
        await willkommen.send("***[more unintelligible vent creature noises]***\n `TRANSLATION: I hope you have an [UNTRANSLATABLE] time here!`")


    
    async def on_member_remove(client, member):
      modAlert = client.get_channel(897494012460662835)
      willkommen = client.get_channel(895828976411496449)  
      await willkommen.send("***[sad vent creature noises]***\n`TRANSLATION: " + member.display_name + " left the server.`")

    async def on_message_delete(self, message):
      msgLogs = client.get_channel(939895627649810443)

      embed=discord.Embed(color=0xff2424)
      embed.set_author(name=(message.author.nick + " ("+ str(message.author) + ")"), url=message.author.avatar_url, icon_url=message.author.avatar_url)
      embed.add_field(name="deleted message", value=("“"+ message.content + "”" ), inline=False)
      embed.add_field(name="msg created", value=message.created_at, inline=True)
      embed.add_field(name="channel", value=message.channel, inline=True)
      embed.set_footer(text="message deleted, "+ time.ctime())

      await msgLogs.send(embed=embed)
    
    async def on_raw_message_delete(self, payload):
      msgLogs = client.get_channel(939895627649810443)
      await msgLogs.send("message deleted in #" + (str(client.get_channel(939895627649810443))))

    async def on_message_edit(self, before, after):
      msgLogs = client.get_channel(939895627649810443)

      embed=discord.Embed(color=0xffc170)
      embed.set_author(name=(before.author.nick + " ("+ str(before.author) + ")"), url=before.author.avatar_url, icon_url=before.author.avatar_url)

      embed.add_field(name="old content", value=("“"+ before.content + "”"), inline=False)
      embed.add_field(name="new content", value=("“"+ after.content + "”"), inline=False)
      embed.add_field(name="channel", value=before.channel, inline=True)
      embed.set_footer(text="message edited, "+ time.ctime())
      await msgLogs.send(embed=embed)


    async def on_raw_reaction_add(self, payload):
        pronGet = 896070828758798426 

        colGet = 896116304099037204

        fanGet = 927887561827967068

        etcGet = 927889594660315136

        heckGet = 928315410707779634

        twiGet = 1

        guild = client.get_guild(payload.guild_id)
        user = guild.get_member(payload.user_id)


        if payload.emoji.name == "📌":

            channel = client.get_channel(payload.channel_id)

            message = await channel.fetch_message(payload.message_id)
            reaction = discord.utils.get(message.reactions, emoji=payload.emoji.name)
            if reaction and reaction.count > 4:
                await message.pin()
        
        if str(payload.emoji) == "🤷" and payload.message_id == twiGet:
          added = discord.utils.get(guild.roles, name="girl what is twilight")
          if added not in user.roles:
            await user.add_roles(added)
      
        if str(payload.emoji) == "✨" and payload.message_id == pronGet:
          shePR = discord.utils.get(guild.roles, name="she/her")
          if shePR not in user.roles:
            await user.add_roles(shePR)
        
        if str(payload.emoji) == "⭐" and payload.message_id == pronGet:
          hePR = discord.utils.get(guild.roles, name="he/him")
          if hePR not in user.roles:
            await user.add_roles(hePR)
        
        if str(payload.emoji) == "🌠" and payload.message_id == pronGet:
          theyPR = discord.utils.get(guild.roles, name="they/them")
          if theyPR not in user.roles:
            await user.add_roles(theyPR)
        
        if str(payload.emoji) == "🌃" and payload.message_id == pronGet:
          added = discord.utils.get(guild.roles, name="ask my pronouns")
          if added not in user.roles:
            await user.add_roles(added)



        if str(payload.emoji) == "🔴" and payload.message_id == colGet:
          added = discord.utils.get(guild.roles, name="red")
          if added not in user.roles:
            await user.add_roles(added)
        
        if str(payload.emoji) == "💗" and payload.message_id == colGet:
          added = discord.utils.get(guild.roles, name="pink")
          if added not in user.roles:
            await user.add_roles(added)
        
        if str(payload.emoji) == "🟣" and payload.message_id == colGet:
          added = discord.utils.get(guild.roles, name="purple")
          if added not in user.roles:
            await user.add_roles(added)
        
        if str(payload.emoji) == "🔵" and payload.message_id == colGet:
          added = discord.utils.get(guild.roles, name="blue")
          if added not in user.roles:
            await user.add_roles(added)
        
        if str(payload.emoji) == "🔷" and payload.message_id == colGet:
          added = discord.utils.get(guild.roles, name="cyan")
          if added not in user.roles:
            await user.add_roles(added)
        
        if str(payload.emoji) == "💙" and payload.message_id == colGet:
          added = discord.utils.get(guild.roles, name="turquoise")
          if added not in user.roles:
            await user.add_roles(added)
        
        if str(payload.emoji) == "🟢" and payload.message_id == colGet:
          added = discord.utils.get(guild.roles, name="green")
          if added not in user.roles:
            await user.add_roles(added)
        
        if str(payload.emoji) == "🟡" and payload.message_id == colGet:
          added = discord.utils.get(guild.roles, name="yellow")
          if added not in user.roles:
            await user.add_roles(added)
        
        if str(payload.emoji) == "🟠" and payload.message_id == colGet:
          added = discord.utils.get(guild.roles, name="orange")
          if added not in user.roles:
            await user.add_roles(added)

        #/// fandom

        if str(payload.emoji) == "<:lawyergay:913495439754555462>" and payload.message_id == fanGet:
          added = discord.utils.get(guild.roles, name="LGBTQ+ lawyers")
          if added not in user.roles:
            await user.add_roles(added)
        
        if str(payload.emoji) == "🥚" and payload.message_id == fanGet:
          added = discord.utils.get(guild.roles, name="patholovers (mental illness)")
          if added not in user.roles:
            await user.add_roles(added)
        
        if str(payload.emoji) == "🐺" and payload.message_id == fanGet:
          added = discord.utils.get(guild.roles, name="roach stans (witcher role)")
          if added not in user.roles:
            await user.add_roles(added)
        
        if str(payload.emoji) == "🎭" and payload.message_id == fanGet:
          added = discord.utils.get(guild.roles, name="theatre kid")
          if added not in user.roles:
            await user.add_roles(added)
        
        if str(payload.emoji) == "🙌" and payload.message_id == fanGet:
          added = discord.utils.get(guild.roles, name="bad bitches (altmalmar stans)")
          if added not in user.roles:
            await user.add_roles(added)
        
        if str(payload.emoji) == "💨" and payload.message_id == fanGet:
          added = discord.utils.get(guild.roles, name="bendy bois 🌊🌍🔥💨")
          if added not in user.roles:
            await user.add_roles(added)
        
        if str(payload.emoji) == "🐦" and payload.message_id == fanGet:
          added = discord.utils.get(guild.roles, name="Grishaverse Gregs")
          if added not in user.roles:
            await user.add_roles(added)
        
        if str(payload.emoji) == "<:catblushwithLOVE:906966410956247040>" and payload.message_id == fanGet:
          added = discord.utils.get(guild.roles, name="debsmobd pimg <3 <3 <3")
          if added not in user.roles:
            await user.add_roles(added)
        
        if str(payload.emoji) == "💀" and payload.message_id == fanGet:
          added = discord.utils.get(guild.roles, name="dishonourable dosjmpreds")
          if added not in user.roles:
            await user.add_roles(added)

        if str(payload.emoji) == "🥔" and payload.message_id == fanGet:
          added = discord.utils.get(guild.roles, name="APERTURE TEST SUBJECTS")
          if added not in user.roles:
            await user.add_roles(added)

        if str(payload.emoji) == "🗺️" and payload.message_id == fanGet:
          added = discord.utils.get(guild.roles, name="Nathan Break Stans")
          if added not in user.roles:
            await user.add_roles(added)

        if str(payload.emoji) == "🦖" and payload.message_id == fanGet:
          added = discord.utils.get(guild.roles, name="Paleo Pals")
          if added not in user.roles:
            await user.add_roles(added)  

        if str(payload.emoji) == "😻" and payload.message_id == fanGet:
          added = discord.utils.get(guild.roles, name="catto ping 😻")
          if added not in user.roles:
            await user.add_roles(added) 

        if str(payload.emoji) == "⭐" and payload.message_id == fanGet:
          added = discord.utils.get(guild.roles, name="scruffy looking nerf-herders")
          if added not in user.roles:
            await user.add_roles(added) 

        if str(payload.emoji) == "🥷" and payload.message_id == fanGet:
          added = discord.utils.get(guild.roles, name="naruhoes")
          if added not in user.roles:
            await user.add_roles(added) 

        if str(payload.emoji) == "🎲" and payload.message_id == fanGet:
          added = discord.utils.get(guild.roles, name="critical critters")
          if added not in user.roles:
            await user.add_roles(added) 

        if str(payload.emoji) == "📐" and payload.message_id == fanGet:
          added = discord.utils.get(guild.roles, name="korok killers")
          if added not in user.roles:
            await user.add_roles(added) 

        if str(payload.emoji) == "🥜" and payload.message_id == fanGet:
          added = discord.utils.get(guild.roles, name="anya's bravest peanuts (sxf)")
          if added not in user.roles:
            await user.add_roles(added) 

        if str(payload.emoji) == "🌊" and payload.message_id == fanGet:
          added = discord.utils.get(guild.roles, name="mouselympians (pjo)")
          if added not in user.roles:
            await user.add_roles(added) 

            

        #/// etc
        
        if str(payload.emoji) == "⚔️" and payload.message_id == etcGet:
          added = discord.utils.get(guild.roles, name="Phoebus Ping")
          if added not in user.roles:
            await user.add_roles(added)
        
        if str(payload.emoji) == "🧙‍♂️" and payload.message_id == etcGet:
          added = discord.utils.get(guild.roles, name="potes' other blue oc (lys) ping")
          if added not in user.roles:
            await user.add_roles(added)
        
        if str(payload.emoji) == "<:gayfear:896443932517474334>" and payload.message_id == etcGet:
          added = discord.utils.get(guild.roles, name="Vengeance AU ping <3")
          if added not in user.roles:
            await user.add_roles(added)
        
        if str(payload.emoji) == "🕰️" and payload.message_id == etcGet:
          added = discord.utils.get(guild.roles, name="Elsie ping")
          if added not in user.roles:
            await user.add_roles(added)
        
        if str(payload.emoji) == "<:samehat:915712015941640292>" and payload.message_id == etcGet:
          added = discord.utils.get(guild.roles, name="into the arnoheckerverse")
          if added not in user.roles:
            await user.add_roles(added)

        if str(payload.emoji) == "🤠" and payload.message_id == etcGet:
          added = discord.utils.get(guild.roles, name="Cowedboys Ping")
          if added not in user.roles:
            await user.add_roles(added)

            
        
        #/// hecker

        if str(payload.emoji) == "😭" and payload.message_id == heckGet:
          added = discord.utils.get(guild.roles, name="arnoheckers")
          if added not in user.roles:
            await user.add_roles(added)

        if str(payload.emoji) == "<:knife_against_pick_one:901143716855697479>" and payload.message_id == heckGet:
          added = discord.utils.get(guild.roles, name="jacobheckers")
          if added not in user.roles:
            await user.add_roles(added)
        
       






        
        

    
    async def on_raw_reaction_remove(self, payload):
        pronGet = 896070828758798426 

        colGet = 896116304099037204
        
        fanGet = 927887561827967068

        etcGet = 927889594660315136

        heckGet = 928315410707779634

        guild = client.get_guild(payload.guild_id)
        user = guild.get_member(payload.user_id)

        if payload.emoji.name == "📌":

            channel = client.get_channel(payload.channel_id)

            message = await channel.fetch_message(payload.message_id)
            reaction = discord.utils.get(message.reactions, emoji=payload.emoji.name)
            if reaction and reaction.count <= 4:
                await message.unpin()


        if str(payload.emoji) == "✨" and payload.message_id == pronGet:
          shePR = discord.utils.get(guild.roles, name="she/her")
          if shePR in user.roles:
            await user.remove_roles(shePR)
        
        if str(payload.emoji) == "⭐" and payload.message_id == pronGet:
          hePR = discord.utils.get(guild.roles, name="he/him")
          if hePR in user.roles:
            await user.remove_roles(hePR)
        
        if str(payload.emoji) == "🌠" and payload.message_id == pronGet:
          theyPR = discord.utils.get(guild.roles, name="they/them")
          if theyPR in user.roles:
            await user.remove_roles(theyPR)
        
        if str(payload.emoji) == "🌃" and payload.message_id == pronGet:
          added = discord.utils.get(guild.roles, name="ask my pronouns")
          if added in user.roles:
            await user.remove_roles(added)


            
        
        if str(payload.emoji) == "🔴" and payload.message_id == colGet:
          added = discord.utils.get(guild.roles, name="red")
          if added in user.roles:
            await user.remove_roles(added)
        
        if str(payload.emoji) == "💗" and payload.message_id == colGet:
          added = discord.utils.get(guild.roles, name="pink")
          if added in user.roles:
            await user.remove_roles(added)
        
        if str(payload.emoji) == "🟣" and payload.message_id == colGet:
          added = discord.utils.get(guild.roles, name="purple")
          if added in user.roles:
            await user.remove_roles(added)
        
        if str(payload.emoji) == "🔵" and payload.message_id == colGet:
          added = discord.utils.get(guild.roles, name="blue")
          if added in user.roles:
            await user.remove_roles(added)
        
        if str(payload.emoji) == "🔷" and payload.message_id == colGet:
          added = discord.utils.get(guild.roles, name="cyan")
          if added in user.roles:
            await user.remove_roles(added)
        
        if str(payload.emoji) == "💙" and payload.message_id == colGet:
          added = discord.utils.get(guild.roles, name="turquoise")
          if added in user.roles:
            await user.remove_roles(added)
        
        if str(payload.emoji) == "🟢" and payload.message_id == colGet:
          added = discord.utils.get(guild.roles, name="green")
          if added in user.roles:
            await user.remove_roles(added)
        
        if str(payload.emoji) == "🟡" and payload.message_id == colGet:
          added = discord.utils.get(guild.roles, name="yellow")
          if added in user.roles:
            await user.remove_roles(added)
        
        if str(payload.emoji) == "🟠" and payload.message_id == colGet:
          added = discord.utils.get(guild.roles, name="orange")
          if added in user.roles:
            await user.remove_roles(added)
      
        #/// fandom

        if str(payload.emoji) == "<:lawyergay:913495439754555462>" and payload.message_id == fanGet:
          added = discord.utils.get(guild.roles, name="LGBTQ+ lawyers")
          if added in user.roles:
            await user.remove_roles(added)
        
        if str(payload.emoji) == "🥚" and payload.message_id == fanGet:
          added = discord.utils.get(guild.roles, name="patholovers (mental illness)")
          if added in user.roles:
            await user.remove_roles(added)
        
        if str(payload.emoji) == "🐺" and payload.message_id == fanGet:
          added = discord.utils.get(guild.roles, name="roach stans (witcher role)")
          if added in user.roles:
            await user.remove_roles(added)
        
        if str(payload.emoji) == "🎭" and payload.message_id == fanGet:
          added = discord.utils.get(guild.roles, name="theatre kid")
          if added in user.roles:
            await user.remove_roles(added)
        
        if str(payload.emoji) == "🙌" and payload.message_id == fanGet:
          added = discord.utils.get(guild.roles, name="bad bitches (altmalmar stans)")
          if added in user.roles:
            await user.remove_roles(added)
        
        if str(payload.emoji) == "💨" and payload.message_id == fanGet:
          added = discord.utils.get(guild.roles, name="bendy bois 🌊🌍🔥💨")
          if added in user.roles:
            await user.remove_roles(added)
        
        if str(payload.emoji) == "🐦" and payload.message_id == fanGet:
          added = discord.utils.get(guild.roles, name="Grishaverse Gregs")
          if added in user.roles:
            await user.remove_roles(added)
        
        if str(payload.emoji) == "<:catblushwithLOVE:906966410956247040>" and payload.message_id == fanGet:
          added = discord.utils.get(guild.roles, name="debsmobd pimg <3 <3 <3")
          if added in user.roles:
            await user.remove_roles(added)

        if str(payload.emoji) == "💀" and payload.message_id == fanGet:
          added = discord.utils.get(guild.roles, name="dishonourable dosjmpreds")
          if added in user.roles:
            await user.remove_roles(added)

        if str(payload.emoji) == "🥔" and payload.message_id == fanGet:
          added = discord.utils.get(guild.roles, name="APERTURE TEST SUBJECTS")
          if added in user.roles:
            await user.remove_roles(added)

        if str(payload.emoji) == "🗺️" and payload.message_id == fanGet:
          added = discord.utils.get(guild.roles, name="Nathan Break Stans")
          if added in user.roles:
            await user.remove_roles(added)

        if str(payload.emoji) == "🦖" and payload.message_id == fanGet:
          added = discord.utils.get(guild.roles, name="Paleo Pals")
          if added in user.roles:
            await user.remove_roles(added) 
        
        if str(payload.emoji) == "😻" and payload.message_id == fanGet:
          added = discord.utils.get(guild.roles, name="catto ping 😻")
          if added in user.roles:
            await user.remove_roles(added) 

        if str(payload.emoji) == "⭐" and payload.message_id == fanGet:
          added = discord.utils.get(guild.roles, name="scruffy looking nerf-herders")
          if added in user.roles:
            await user.remove_roles(added) 

        if str(payload.emoji) == "🥷" and payload.message_id == fanGet:
          added = discord.utils.get(guild.roles, name="naruhoes")
          if added in user.roles:
            await user.remove_roles(added) 

        if str(payload.emoji) == "🎲" and payload.message_id == fanGet:
          added = discord.utils.get(guild.roles, name="critical critters")
          if added in user.roles:
            await user.remove_roles(added) 

        if str(payload.emoji) == "📐" and payload.message_id == fanGet:
          added = discord.utils.get(guild.roles, name="korok killers")
          if added in user.roles:
            await user.remove_roles(added) 

        if str(payload.emoji) == "🥜" and payload.message_id == fanGet:
          added = discord.utils.get(guild.roles, name="anya's bravest peanuts (sxf)")
          if added in user.roles:
            await user.remove_roles(added) 

        if str(payload.emoji) == "🌊" and payload.message_id == fanGet:
          added = discord.utils.get(guild.roles, name="mouselympians (pjo)")
          if added in user.roles:
            await user.remove_roles(added) 
            
        #/// etc
        
        if str(payload.emoji) == "⚔️" and payload.message_id == etcGet:
          added = discord.utils.get(guild.roles, name="Phoebus Ping")
          if added in user.roles:
            await user.remove_roles(added)
        
        if str(payload.emoji) == "🧙‍♂️" and payload.message_id == etcGet:
          added = discord.utils.get(guild.roles, name="potes' other blue oc (lys) ping")
          if added in user.roles:
            await user.remove_roles(added)
        
        if str(payload.emoji) == "<:gayfear:896443932517474334>" and payload.message_id == etcGet:
          added = discord.utils.get(guild.roles, name="Vengeance AU ping <3")
          if added in user.roles:
            await user.remove_roles(added)
        
        if str(payload.emoji) == "🕰️" and payload.message_id == etcGet:
          added = discord.utils.get(guild.roles, name="Elsie ping")
          if added in user.roles:
            await user.remove_roles(added)
        
        if str(payload.emoji) == "<:samehat:915712015941640292>" and payload.message_id == etcGet:
          added = discord.utils.get(guild.roles, name="into the arnoheckerverse")
          if added in user.roles:
            await user.remove_roles(added)
        
        if str(payload.emoji) == "🤠" and payload.message_id == etcGet:
          added = discord.utils.get(guild.roles, name="Cowedboys Ping")
          if added in user.roles:
            await user.remove_roles(added)
            
        #/// hecker

        if str(payload.emoji) == "😭" and payload.message_id == heckGet:
          added = discord.utils.get(guild.roles, name="arnoheckers")
          if added in user.roles:
            await user.remove_roles(added)

        if str(payload.emoji) == "<:knife_against_pick_one:901143716855697479>" and payload.message_id == heckGet:
          added = discord.utils.get(guild.roles, name="jacobheckers")
          if added in user.roles:
            await user.remove_roles(added)

        



keep_alive()
client = MyClient()
token = os.environ.get("SUPER_SECRET_BOT_TOKEN")
client.run(token)