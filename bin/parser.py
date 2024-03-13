from bs4 import BeautifulSoup
from lxml import html

import json
import os


def pprint(msg):
    try:
        print(json.dumps(msg,indent=2))
    except:
        print(msg)



base_dir = os.path.abspath(os.path.join(os.path.dirname( __file__ ), os.pardir ))

report_dir = os.path.join(base_dir,"tmp", "results")
output_file = os.path.join(base_dir,"data","results.json")


month_names = [ "janúar","febrúar","mars","apríl","maí","júní","júlí","ágúst","september","október","nóvember","desember"]
months = { }

c = 1

for m in month_names:
    months[m] = c
    c += 1



def find_info(content):


    report = { }
    report["date"] = { }

    soup = BeautifulSoup(content,features="lxml")

    mydivs = soup.findAll('div')

    #mydivs = soup.find_all("div", {"class": "card-has-review"})
    all_cards = soup.find_all("div", {"class": "card mb-4"})
    if len(all_cards) == 0 :
        all_cards = soup.find_all("div", {"class": "card mb-4 card-has-review"})

    try:
        name_div = all_cards[0]
    except:
        dead_kt = soup.find_all("p", {"class": "card-text"})
        dead_kt = dead_kt[0].text.strip()
        if dead_kt == "Engar stofnanir fundust":
            return None

    name_field = name_div.find_all("h5")
    name_raw = name_field[0].text
    name_raw = name_raw.split(" (")

    name = name_raw[0].strip()
    kt = name_raw[1].replace(")","")


    location_div = name_div.find_all("h6")
    location_orig = location_div[0].text

    location_raw = location_orig.split(",")


    
    report["establishment"] = { }
    report["establishment"]["name"] = name
    report["establishment"]["kennitala"] = kt
    report["establishment"]["location"] = { }
    report["establishment"]["location"]["original"] = location_orig
    report["establishment"]["location"]["address"] = location_raw[0]
    try:
        report["establishment"]["location"]["zip"] = location_raw[1].split(" ")[0]
    except:
        if len(location_raw) == 0:
            if "reyk" in location_raw[0].lower():
                location_tmp = location_raw[0].split(" ")
                try:
                    x = int(location_tmp[0])
                    report["establishment"]["location"]["zip"] = location_tmp[0]
                except:
                    print("asdf")
    try:
        report["establishment"]["location"]["city"] = location_raw[1].split(" ")[1]
    except:
        report["establishment"]["location"]["city"] = "not set"







    review_divs = soup.find_all("div", {"class": "card-has-review"})

    if len(review_divs) == 0:
        report["has_data"] = False
        report["date"]["found"] = False

        return report



    
    review_data = review_divs[0]

    review_date_div = review_data.find_all("div", { "class" : "card-footer"})
    review_date_lines = review_date_div[0].text.split("\n")

    report["date"] = {}
    report["date"]["found"] = False
    for line in review_date_lines:
        if "eftirlit" in line:
            date_raw = line.split(":")[1].replace(".","").strip().split(" ")

            dom = date_raw[0]
            mon = months[date_raw[1]]
            year = date_raw[2]

            ts = year + "/" + str(mon).zfill(2) + "/" + dom.zfill(2)

            report["date"]["found"] = True
            report["date"]["orig"] = line
            report["date"]["datestamp"] = ts
            report["date"]["year"] = year
            report["date"]["month"] = mon
            report["date"]["day"] = dom

            break
            
    overall_review = review_data.find_all("div", { "class" : "col-4"})[0].find_all("span")[0].text

    report["score"] = {}
    report["score"]["overall"] = int(overall_review)

    cat_review = review_data.find_all("div", { "class" : "card-footer"})

    cats  = cat_review[1].find_all("dt")
    revs  = cat_review[1].find_all("dd")

    c = 0
    m = 4

    while c < m:

        cat_name = cats[c].text.strip()
        cat_rev = revs[c].text.strip()


        cat_name = cat_name.replace("æ","ae")
        if cat_rev == "Á ekki við":
            cat_rev = "A ekki vid"
        elif cat_rev == "Ekki skoðað":
            cat_rev = "Ekki skodad"



        report["score"][cat_name] = cat_rev

        c += 1


            
    report["has_data"] = True


    return report

    




files = os.listdir(report_dir)



coll = { }
success_count = 0
fail_count = 0
dead_kt_count = 0
failed_files = [ ]
for file in files:



    full_path = os.path.join(report_dir,file)
    f = open(full_path,"r").read()
    r = find_info(f)
    #kt = r["establishment"]["kennitala"].replace("-","").strip()
    #coll[kt] = r


    try:
        f = open(full_path,"r").read()
        r = find_info(f)

        if r is not None:

            kt = r["establishment"]["kennitala"].replace("-","").strip()
            coll[kt] = r
            success_count += 1
        else:
            dead_kt_count += 1
    except:
        fail_count += 1
        failed_files.append(file)


lval = 30
print("Success:".ljust(lval) + str(success_count))
print("Fail:".ljust(lval) + str(fail_count))
print("Dead kt:".ljust(lval) + str(dead_kt_count))
if len(failed_files) > 0:
    print("Files that failed are:")
    for failed_file in failed_files:
        print(failed_file)

F = open(output_file,"w")
F.write(json.dumps(coll,indent=1))

print("Results writen to: " + output_file)
