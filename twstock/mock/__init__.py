# -*- coding: utf-8 -*-

import json


TSE_2330_TW = ["""
{"msgArray": [{"ts": "0", "tk0": "2330.tw_tse_20170724_B_9999778918", "tk1":
"2330.tw_tse_20170724_B_9999777950", "tlong": "1500860849000", "f":
"853_1193_972_1209_817_", "ex": "tse", "g": "1221_1530_817_1038_1193_", "d":
"20170724", "it": "12", "b": "214.00_213.50_213.00_212.50_212.00_", "c":
"2330", "mt": "264564", "a": "214.50_215.00_215.50_216.00_216.50_", "n":
"\u53f0\u7a4d\u96fb", "o": "213.50", "l": "213.00", "h": "214.50", "ip": "0",
"i": "24", "w": "193.00", "v": "5094", "u": "235.00", "t": "09:47:29", "s":
"1", "pz": "213.50", "tv": "1", "p": "0", "nf":
"\u53f0\u7063\u7a4d\u9ad4\u96fb\u8def\u88fd\u9020\u80a1\u4efd\u6709\u9650\u516c\u53f8",
"ch": "2330.tw",
"z": "214.50", "y": "214.00", "ps": "1323"}], "userDelay": 5000, "rtmessage":
"OK", "referer": "", "queryTime": {"sysTime": "09:47:30", "sessionLatestTime":
-1, "sysDate": "20170724", "sessionKey": "tse_2330.tw_20170724|",
"sessionFromTime": -1, "stockInfoItem": 2065, "showChart": false,
"sessionStr": "UserSession", "stockInfo": 204322}, "rtcode": "0000"}
""", """
{"msgArray": [{"ts": "0", "tk0": "2330.tw_tse_20170724_B_9999766224", "tk1":
"2330.tw_tse_20170724_B_9999765954", "tlong": "1500861105000", "f":
"1059_1079_1014_1229_907_", "ex": "tse", "g": "1455_1598_797_1019_1134_", "d":
"20170724", "it": "12", "b": "214.00_213.50_213.00_212.50_212.00_", "c":
"2330", "mt": "778472", "a": "214.50_215.00_215.50_216.00_216.50_", "n":
"\u53f0\u7a4d\u96fb", "o": "213.50", "l": "213.00", "h": "214.50", "ip": "0",
"i": "24", "w": "193.00", "v": "5217", "u": "235.00", "t": "09:51:45", "s":
"0", "pz": "213.50", "tv": "1", "p": "0", "nf":
"\u53f0\u7063\u7a4d\u9ad4\u96fb\u8def\u88fd\u9020\u80a1\u4efd\u6709\u9650\u516c\u53f8",
"ch": "2330.tw",
"z": "214.50", "y": "214.00", "ps": "1323"}], "userDelay": 5000, "rtmessage":
"OK", "referer": "", "queryTime": {"sysTime": "09:51:48", "sessionLatestTime":
-1, "sysDate": "20170724", "sessionKey": "tse_2330.tw_20170724|",
"sessionFromTime": -1, "stockInfoItem": 2055, "showChart": false,
"sessionStr": "UserSession", "stockInfo": 130895}, "rtcode": "0000"}
""", """
{"msgArray": [{"ts": "0", "tk0": "2330.tw_tse_20170724_B_9999760446", "tk1":
"2330.tw_tse_20170724_B_9999759382", "tlong": "1500861243000", "f":
"1034_1028_1009_1253_933_", "ex": "tse", "g": "1466_1625_798_987_1117_", "d":
"20170724", "it": "12", "b": "214.00_213.50_213.00_212.50_212.00_", "c":
"2330", "mt": "962863", "a": "214.50_215.00_215.50_216.00_216.50_", "n":
"\u53f0\u7a4d\u96fb", "o": "213.50", "l": "213.00", "h": "214.50", "ip": "0",
"i": "24", "w": "193.00", "v": "5268", "u": "235.00", "t": "09:54:03", "s":
"0", "pz": "213.50", "tv": "3", "p": "0", "nf":
"\u53f0\u7063\u7a4d\u9ad4\u96fb\u8def\u88fd\u9020\u80a1\u4efd\u6709\u9650\u516c\u53f8",
"ch": "2330.tw",
"z": "214.00", "y": "214.00", "ps": "1323"}], "userDelay": 5000, "rtmessage":
"OK", "referer": "", "queryTime": {"sysTime": "09:54:10", "sessionLatestTime":
-1, "sysDate": "20170724", "sessionKey": "tse_2330.tw_20170724|",
"sessionFromTime": -1, "stockInfoItem": 1602, "showChart": false,
"sessionStr": "UserSession", "stockInfo": 119518}, "rtcode": "0000"}
"""]

TWSE_2330_TW_201505_RESPONSE = ['''
{"stat":"OK","date":"20150501","title":
"104年05月 2330 台積電           各日成交資訊","fields":["日期","成交股數",
"成交金額","開盤價","最高價","最低價","收盤價","漲跌價差","成交筆數"],"data":
[["104/05/04","30,868,640","4,548,281,580","148.50","148.50","146.00","147.50",
"+0.50","8,598"],["104/05/05","27,789,400","4,083,589,300","147.50","148.00",
"146.00","147.00","-0.50","6,502"],["104/05/06","18,824,208","2,765,471,076",
"145.50","148.00","145.50","147.50","+0.50","6,477"],["104/05/07","21,908,150",
"3,209,664,442","146.00","147.50","146.00","146.50","-1.00","5,816"],
["104/05/08","20,035,646","2,938,305,595","146.00","147.50","146.00","146.50",
" 0.00","7,730"],["104/05/11","20,402,529","3,020,441,292","149.00","149.00",
"147.00","148.50","+2.00","6,385"],["104/05/12","24,956,498","3,687,151,073",
"147.00","148.50","147.00","147.50","-1.00","6,593"],["104/05/13","19,437,537",
"2,880,697,082","147.50","149.00","147.00","148.00","+0.50","5,694"],
["104/05/14","39,888,654","5,860,602,872","148.00","148.50","146.00","146.00",
"-2.00","12,300"],["104/05/15","24,831,890","3,627,515,848","147.00","147.00",
"145.00","146.50","+0.50","8,186"],["104/05/18","26,212,375","3,823,751,806",
"147.00","147.00","145.00","146.50"," 0.00","7,178"],["104/05/19","26,321,396",
"3,852,118,475","145.50","147.50","145.00","146.50"," 0.00","9,418"],
["104/05/20","26,984,912","3,949,956,564","146.50","147.00","146.00","146.50",
" 0.00","10,516"],["104/05/21","41,286,686","5,995,895,156","146.00","146.50",
"144.50","145.50","-1.00","12,871"],["104/05/22","22,103,852","3,229,666,392",
"146.00","147.00","145.00","145.50"," 0.00","6,813"],["104/05/25","16,323,218",
"2,396,692,046","146.50","147.50","145.50","147.50","+2.00","5,998"],
["104/05/26","16,069,726","2,368,218,823","148.50","148.50","146.50","146.50",
"-1.00","6,148"],["104/05/27","24,257,941","3,536,266,849","145.50","147.00",
"145.00","145.00","-1.50","6,869"],["104/05/28","36,704,395","5,388,568,653",
"147.00","147.50","146.00","147.00","+2.00","10,259"],["104/05/29","61,983,862",
"9,053,910,953","147.00","147.50","145.50","146.00","-1.00","8,252"]],"notes":[
"符號說明:+/-/X表示漲/跌/不比價",
"當日統計資訊含一般、零股、盤後定價、鉅額交易，不含拍賣、標購。"]}
''']

OTC_6223_TW = ["""
{"msgArray":[{"ts":"0","fv":"7","tk0":"6223.tw_otc_20190111_B_9999689491","tk1":
"6223.tw_otc_20190111_B_9999678121","oa":"61.70","ob":"61.20","tlong":
"1547188200000","ot":"14:30:00","f":"1_37_9_14_49_","ex":"otc","g":
"1_5_3_14_10_","ov":"1035","d":"20190111","it":"12","b":
"61.00_60.90_60.80_60.70_60.60_","c":"6223","mt":"000000","a":
"61.10_61.20_61.30_61.40_61.50_","n":"旺矽","o":"61.00","l":"59.70","oz":
"61.20","h":"62.30","ip":"0","i":"24","w":"54.20","v":"3084","u":"66.20","t":
"13:30:00","s":"175","pz":"61.20","tv":"175","p":"0","nf":"旺矽科技股份有限公司",
"ch":"6223.tw","z":"61.10","y":"60.20","ps":"173"}],"userDelay":5000,
"rtmessage":"OK","referer":"","queryTime":{"sysTime":"02:01:44",
"sessionLatestTime":-1,"sysDate":"20190113","sessionFromTime":-1,
"stockInfoItem":391,"showChart":false,"sessionStr":"UserSession","stockInfo":
63747},"rtcode":"0000"}
"""]
TPEX_6223_TW_201505_RESPONSE = ['''
{"stkNo":"6223","stkName":"\u65fa\u77fd","showListPriceNote":false,
"showListPriceLink":false,"reportDate":"104\/5","iTotalRecords":20,"aaData":
[["104\/05\/04","374","34,462","93.00","93.00","91.30","91.40","-0.60","323"],
["104\/05\/05","474","43,721","91.50","93.20","91.20","91.80","0.40","368"],
["104\/05\/06","468","42,967","91.50","93.20","90.40","91.80","0.00","401"],
["104\/05\/07","1,257","117,125","91.80","94.10","91.80","93.50","1.70","820"],
["104\/05\/08","1,079","99,439","93.50","93.90","90.30","91.00","-2.50","804"],
["104\/05\/11","3,400","294,740","92.40","92.80","84.70","84.70","-6.30",
"2,031"],["104\/05\/12","3,424","280,856","83.70","84.80","78.80","84.00",
"-0.70","2,484"],["104\/05\/13","1,078","91,625","84.00","86.40","82.50",
"85.80","1.80","808"],["104\/05\/14","1,433","125,392","88.70","88.70","86.50",
"87.10","1.30","1,065"],["104\/05\/15","891","76,478","86.50","86.60","85.00",
"86.10","-1.00","632"],["104\/05\/18","1,202","100,938","86.10","86.10","83.00",
"83.90","-2.20","913"],["104\/05\/19","1,008","85,342","83.50","85.50","83.40",
"84.50","0.60","850"],["104\/05\/20","999","86,379","85.30","87.10","84.70",
"86.70","2.20","731"],["104\/05\/21","488","42,151","86.40","86.90","85.60",
"86.30","-0.40","335"],["104\/05\/22","706","60,965","86.20","87.40","85.70",
"86.00","-0.30","496"],["104\/05\/25","231","19,948","85.90","86.90","85.70",
"86.20","0.20","179"],["104\/05\/26","1,890","169,432","87.00","91.90","86.30",
"91.10","4.90","1,406"],["104\/05\/27","782","70,881","90.70","91.60","89.50",
"90.90","-0.20","585"],["104\/05\/28","1,214","112,992","91.20","94.40","91.20",
"91.70","0.80","870"],["104\/05\/29","583","53,033","92.00","92.60","90.40",
"90.40","-1.30","415"]]}
''']


TSE_2330_AND_OTC_6223_TW = ['''
{"msgArray":[{"ts":"0","fv":"21","tk0":"2330.tw_tse_20190111_B_9999136028",
"tk1":"2330.tw_tse_20190111_B_9999114496","oa":"220.00","ob":"219.50","tlong":
"1547188200000","ot":"14:30:00","f":"707_2688_1465_1224_301_","ex":"tse","g":
"35_239_812_728_816_","ov":"26288","d":"20190111","it":"12","b":
"220.00_219.50_219.00_218.50_218.00_","c":"2330","mt":"000000","a":
"220.50_221.00_221.50_222.00_222.50_","n":"台積電","o":"219.00","l":"218.00",
"oz":"220.00","h":"220.50","ip":"0","i":"24","w":"194.50","v":"28055","u":
"237.50","t":"13:30:00","s":"4390","pz":"220.50","tv":"4390","p":"0","nf":
"台灣積體電路製造股份有限公司","ch":"2330.tw","z":"220.50","y":"216.00","ps":
"4390"},{"ts":"0","fv":"7","tk0":"6223.tw_otc_20190111_B_9999689491","tk1":
"6223.tw_otc_20190111_B_9999678121","oa":"61.70","ob":"61.20","tlong":
"1547188200000","ot":"14:30:00","f":"1_37_9_14_49_","ex":"otc","g":
"1_5_3_14_10_","ov":"1035","d":"20190111","it":"12","b":
"61.00_60.90_60.80_60.70_60.60_","c":"6223","mt":"000000","a":
"61.10_61.20_61.30_61.40_61.50_","n":"旺矽","o":"61.00","l":"59.70","oz":
"61.20","h":"62.30","ip":"0","i":"24","w":"54.20","v":"3084","u":"66.20","t":
"13:30:00","s":"175","pz":"61.20","tv":"175","p":"0","nf":"旺矽科技股份有限公司",
"ch":"6223.tw","z":"61.10","y":"60.20","ps":"173"}],"userDelay":5000,
"rtmessage":"OK","referer":"","queryTime":{"sysTime":"11:22:16",
"sessionLatestTime":-1,"sysDate":"20190113","sessionFromTime":-1,
"stockInfoItem":1773,"showChart":false,"sessionStr":"UserSession","stockInfo":
189997},"rtcode":"0000"}
''']

ERROR_CODE_TW = ["""
{"stkNo":"Error_Code","stkName":"","showListPriceNote":false,
"showListPriceLink":false,"reportDate":"107\/11","iTotalRecords":0,"aaData":[]}
"""]

WITHOUT_MSG_ARRAY_TW = ["""
{"userDelay":5000,
"rtmessage":"OK","referer":"","queryTime":{"sysTime":"02:01:44",
"sessionLatestTime":-1,"sysDate":"20190113","sessionFromTime":-1,
"stockInfoItem":391,"showChart":false,"sessionStr":"UserSession","stockInfo":
63747},"rtcode":"0000"}
"""]

EMPTY_MSG_ARRAY_TW = ["""
{"msgArray":[],"userDelay":5000,
"rtmessage":"OK","referer":"","queryTime":{"sysTime":"02:01:44",
"sessionLatestTime":-1,"sysDate":"20190113","sessionFromTime":-1,
"stockInfoItem":391,"showChart":false,"sessionStr":"UserSession","stockInfo":
63747},"rtcode":"0000"}
"""]


stock_list = {
    '2330': TSE_2330_TW,
    '6223': OTC_6223_TW,
    '2330_6223': TSE_2330_AND_OTC_6223_TW,
    'error_code': ERROR_CODE_TW,
    'without_msg_array': WITHOUT_MSG_ARRAY_TW,
    'empty_msg_array': EMPTY_MSG_ARRAY_TW,
}
stock_response_list = {
    '2330': TWSE_2330_TW_201505_RESPONSE,
    '6223': TPEX_6223_TW_201505_RESPONSE,
}


def get_stock_info(stock_id, index=0):
    return json.loads(stock_list[stock_id][index])


def get_stocks_info(stocks):
    data = json.loads(stock_list['2330'][0])
    for _ in range(len(stocks)):
        data['msgArray'].append(data['msgArray'][0])
    return data


def get(stocks):
    if isinstance(stocks, list):
        return get_stocks_info(stocks)
    return get_stock_info(stocks)


def get_stock_response(stock_id):
    return json.loads(stock_response_list[stock_id])

