import xbmc, xbmcgui, xbmcplugin, xbmcaddon,sys,urllib2,re, time,datetime

pluginPath = xbmcaddon.Addon("script.test").getAddonInfo("path")

imagelink_up = os.path.join(pluginPath, "images", "stock_up.png")
imagelink_down = os.path.join(pluginPath, "images", "stock_down.png")
price = 0
percent = 0


def getPrice(url):
  user_agent = 'Mozilla/5 (Solaris 10) Gecko'
  headers = {' User-Agent' : user_agent}
  request = urllib2.Request(url)
  response = urllib2.urlopen(request)
  the_page = response.read()
  #print the_page
  match = re.compile('</td><td align="right" class="even " width="20%">(.+?)</td>').findall(the_page)
  global price
  price = match[0]
  match2 = re.compile('</td><td align="right" class="odd  p" width="20%">(.+?)</td>').findall(the_page)
  global percent
  percent = match2[0]
  return match[0]



count = len(sys.argv) - 1
 
if count > 0:
         hour = datetime.datetime.now().hour
         if hour > 8:
           if hour < 14:
             si = getPrice("http://tw.m.yahoo.com/w/twstock/index_single.php?&stock=4108")
             if "-" in percent:
               xbmc.executebuiltin("Notification(%s, %s, %i, %s)" % ("4108", price+'      '+percent+'%', 10000, imagelink_down))
             else:
               xbmc.executebuiltin("Notifications(%s, %s, %i, %s)" % ("4108", price+'      '+percent+'%', 10000, imagelink_up))
else:
        xbmc.executebuiltin("AlarmClock(test, RunScript(script.test, alarm=true), 1, loop)")

  

  
