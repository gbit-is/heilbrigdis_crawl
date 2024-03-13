import requests
import os
import time


base_dir = os.path.abspath(os.path.join(os.path.dirname( __file__ ), os.pardir ))

out_dir = os.path.join(base_dir,"tmp", "starfsleyfi")

# ef farið er á url-ið, þá eru 125 síður .....
page_count = 125


def get_page(page_number):
    url = "https://webdom.reykjavik.is/GoPro/starfsleyfi_UHS.nsf/Starfsleyfi.xsp?$$ajaxid=view%3A_id1%3AviewPanel1_OUTER_TABLE"

    payload = 'view%3A_id1%3AsrcNafn=&view%3A_id1%3AsrcKennitala=&view%3A_id1%3AsearchHeimilsfang=&view%3A_id1%3AsrcPostnumer=&%24%24viewid=!5xads6ke1b4rcy50vzoca5u3d!&%24%24xspsubmitid=view%3A_id1%3AviewPanel1%3Apager1__Group__lnk__{PAGE_NUMBER}&%24%24xspexecid=view%3A_id1%3AviewPanel1%3Apager1&%24%24xspsubmitvalue=&%24%24xspsubmitscroll=0%7C0&view%3A_id1=view%3A_id1'

    headers = {
  'Accept': '*/*',
  'Accept-Language': 'en-GB,en;q=0.9,en-US;q=0.8,is;q=0.7',
  'Connection': 'keep-alive',
  'Content-Type': 'application/x-www-form-urlencoded',
  'Cookie': 'nmstat=17c5533c-bf4f-cbfd-4591-84e8bcf8d032; SessionID=F8A7E889D9BA0E7555406246BC7460CC64999D06; SessionID=26DF3F97D869D8FB9E8309217C19DABC6CF35E81',
  'Origin': 'https://webdom.reykjavik.is',
  'Referer': 'https://webdom.reykjavik.is/GoPro/starfsleyfi_UHS.nsf/Starfsleyfi.xsp',
  'Sec-Fetch-Dest': 'empty',
  'Sec-Fetch-Mode': 'cors',
  'Sec-Fetch-Site': 'same-origin',
  'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36',
  'X-Requested-With': 'XMLHttpRequest',
  'sec-ch-ua': '"Chromium";v="122", "Not(A:Brand";v="24", "Google Chrome";v="122"',
  'sec-ch-ua-mobile': '?0',
  'sec-ch-ua-platform': '"macOS"'
    }


    headers["Cookie"] = 'nmstat=17c5533c-bf4f-cbfd-4591-84e8bcf8d032; SessionID=F8A7E889D9BA0E7555406246BC7460CC64999D06'

    payload = payload.replace("{PAGE_NUMBER}",str(page_number))

    response = requests.request("POST", url, headers=headers, data=payload)

    return response.text



for i in range(0,page_count):


    msg = str(i) + "/" + str(page_count)
    print(msg)
    #out_file = out_dir + str(i) + ".html" 
    file_name = str(i) + ".html"
    out_file = os.path.join(out_dir, file_name)

    f = open(out_file,"w")
    data = get_page(i)
    f.write(data)
    f.close()

    time.sleep(1)
