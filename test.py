import xbmc, xbmcgui, xbmcplugin, xbmcaddon,sys,urllib2,re, time,datetime

def getPrice(url):
  user_agent = 'Mozilla/5 (Solaris 10) Gecko'
  headers = {' User-Agent' : user_agent}
  request = urllib2.Request(url)
  response = urllib2.urlopen(request)
  the_page = response.read()
  print the_page
  match = re.compile('</td><td align="right" class="even " width="20%">(.+?)</td>').findall(the_page)
  return match[0]


count = len(sys.argv) - 1
 
if count > 0:
         hour = datetime.datetime.now().hour
         if hour > 9:
           if hour < 14:
             si = getPrice("http://tw.m.yahoo.com/w/twstock/index_single.php?&stock=4108")
             xbmc.executebuiltin("Notification(%s, %s, %i)" % ("stock", si, 10000))
        #getPrice("http://tw.m.yahoo.com/w/twstock/index_single.php?&stock=4108")
else:
        xbmc.executebuiltin("AlarmClock(test, RunScript(script.test, alarm=true), 10, loop)")

  

  
