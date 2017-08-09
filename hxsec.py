#! /usr/bin/env python
#coding=utf-8

import requests, json

database = ["06_cn_mumayi_jd_com",
"1010wan_beihaiw_duowan",
"12306_cn",
"131_xiu_tianya",
"17173_com",
"212300_cxhr_zhaopin_com",
"212300_cxhr_zhaopin_copy",
"24buy_cd",
"51cto_com_new",
"51job_com",
"52pk_com",
"55_la",
"766_tuan800_wanmei_37",
"7k7k_com",
"admin5_apphan_07073_soyun",
"aipai_com",
"all_hack_website",
"av_creditcard_com_cn",
"ccidnet_lashou_com",
"cnnb_mop_qinbao_jiapin_qd315",
"cnzz_com",
"co188_com",
"csdn_net",
"damai_cn",
"dangdang_com",
"dodonew_com",
"gfan_com",
"hiapk_com",
"houdao_com",
"ipart_cn",
"jxjatv_073yx_moko_treo8_paojiao",
"jxrsrc_zhenai",
"kaixin001_com-ispeak_com",
"mail_126_com",
"mail_163_com",
"mail_qq_sina",
"mail_qq_sohu",
"pconline_com_cn",
"pingan_com",
"qiannao_dedecms_baofeng",
"qq_old_password",
"radius-qingdaonews_com",
"renren_com",
"seowhy_shooter-tatazu_book118_cs",
"sorry_unknown",
"sorry_unknown2",
"tgbus_com",
"tpy100_com-jia_com",
"uuu9_com",
"weibo_com",
"xda_comicdd_game",
"xiaohua_other",
"xiaomi_com"
]


class HxSec():
    def __init__(self):
        self.s = requests.session()
        r = self.s.get('http://cha.hxsec.com/')
    
    def searchsafe(self, url, payload, headers):
        for i in range(0, 10):
            try:
                r = self.s.post(url, data = payload, headers = headers)
                info = r.content
                return info
            
            except Exception as e:
                print e, payload
        return None
        
    '''
    type: 1 名字邮箱, 2 名字, 3 邮箱
    method: 1 模糊, 2 精确
    返回元组或者None
    '''
    def search1(self, type, method, key, table):
        url = 'http://cha.hxsec.com/ajax.php?act=select'
        headers = {'X-Requested-With': 'XMLHttpRequest'}
        payload = {'select_act':type,
                'match_act':method,
                'key':key,
                'table':table
                }      
        info = self.searchsafe(url, payload, headers)        
        p = info.find('addRow(')
        if p == -1:
            return None
        
        # 可能多行addRow(
        info = info[p:]
        info = info.split('addRow(')
        if len(info) <= 1:
            return None
        
        k1 = []
        for i in range(1, len(info)):
            info1 = info[i]
            info1 = info1[:-2]
            info1 = info1.split(',')
            k = []
            for i in info1:
                k.append(i[1:-1])
            k1.append(k)
        return k1
        
    def search(self, type, method, key):
        r1 = []
        for i in database:
            r = self.search1(type, method, key, i)
            if r != None:
                for r0 in r:
                    r1.append(r0)
        return r1
        
if __name__ == '__main__':
    hs = HxSec()        
    r = hs.search(1, 2, 'fish13')
    print r