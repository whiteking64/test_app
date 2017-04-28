
import browser

import sys
sys.path.insert(0,"http://127.0.0.1:5000/static/modules/wikipedia")
print (sys.path)

import wikipedia, tqdm, nltk

import json, math, re, time, urllib.parse, urllib.request
import numpy as np

from modules.sklearn.feature_extraction.text import TfidfVectorizer
from modules.sklearn.metrics.pairwise import cosine_similarity
from collections import Counter




"""
def Hello(ev):
    kw_ja = browser.document["kw_ja"].value
    kw_en = browser.document["kw_en"].value
    # Output
    res_elt_1 = browser.document["result1"]
    res_elt_1.text = kw_ja
    res_elt_2 = browser.document["result2"]
    res_elt_2.text = kw_en

sub_elt = browser.document["submit_button"]
sub_elt.bind("click", Hello)
"""
########################################################################


#実行時間の計測
start = time.time()

def Hello(ev):
    kw_ja = browser.document["kw_ja"].value
    kw_en = browser.document["kw_en"].value
    # Output
    res_elt_1 = browser.document["result1"]
    res_elt_1.text = kw_ja
    res_elt_2 = browser.document["result2"]
    res_elt_2.text = search(kw_en)
    
    """
	#キーワードの設定
	KW_ja = "ラクダ"
	KW = "camel"
	"""
def search(kw_en):
	#英語のwikipedia
	#題名とその内容を分離したリストを取得
	wikipedia.set_lang("en")
	KW = wikipedia.page(kw_en)
	#a = KW.content

	wiki_result = KW.content
	return wiki_result



elapsed_time = time.time() - start
print ("elapsed_time:{0}".format(elapsed_time))






