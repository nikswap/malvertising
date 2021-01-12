import requests
import socket
import time
import sqlite3
import sys


conn = sqlite3.connect('malvertasingdb.db')

urls = []

schemas = ["http://","https://"]

no_dns = []
forwardings = {}

headers = {}
headers['User-Agent'] = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36'

def domain_in_db(dom):
    c = conn.cursor()
    rows = c.execute('SELECT id FROM domainnames WHERE domain = ?',(dom,)).fetchone()
    if rows:
        return True
    return False

def add_domain_to_db(dom, sta):
    c = conn.cursor()
    rows = c.execute('SELECT id FROM domainnames WHERE domain = ?',(dom,)).fetchone()
    if domain_in_db(dom):
        #print('[+] ALREADY IN DB')
        return
    stmt = 'INSERT INTO domainnames (domain, http_status) VALUES (?,?)'
    c.execute(stmt,(dom,sta))
    conn.commit()

def add_forwardings_for_domain(dom, forw):
    c = conn.cursor()
    rows = c.execute('SELECT id FROM domainnames WHERE domain = ?',(dom,)).fetchone()
    d_id = rows[0]
    stmt = 'INSERT INTO forwards (domainid, forward_to) VALUES (?,?)'
    c.execute(stmt,(d_id,forw))
    conn.commit()


def test_for_malvertersing():
    pass
with open(sys.argv[1]) as f:
    for url in f:
        url = url.strip()
        if domain_in_db(url):
            continue
        for schema in schemas:
            print('[+] CONNECTING TO',schema+url)
            try:
                res = requests.get(schema+url,headers=headers,allow_redirects=False, timeout=5)
                add_domain_to_db(url, res.status_code)
                #print(res.status_code)
                #print(res.text)
                if res.status_code in [301,302]:
                    #if not url in forwardings:
                    #    forwardings[url] = []
                    #forwardings[url].append(res.headers['Location'])
                    add_forwardings_for_domain(url, res.headers['Location'])
                #print(res.headers)
                if res.status_code < 300 and res.status_code > 199:
                    #Search in res.text for urls from lists
                    #Search in body for window.location
                    #Search in body for js files. Download those and search for window.location and known malware urls
                    pass
            except Exception as e:
                print('[+] NO DNS FOR DOMAIN OR SOME OTHER ERROR',e)
                no_dns.append(schema+url)
                add_domain_to_db(url, 'FAILED TO FETCH')
            #time.sleep(1)
