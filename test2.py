import os

import requests


def load_token():
    """读取 token.txt"""
    if not os.path.exists("token.txt"):
        raise FileNotFoundError(f"❌ 未找到 {"token.txt"} 文件！请在同目录下创建，并写入 token。")
    with open("token.txt", "r", encoding="utf-8") as f:
        token = f.read().strip()
    if not token:
        raise ValueError("❌ token.txt 为空！")
    return token


token = load_token()


def like():
    headers = {
        'User-Agent': 'Mozilla/5.0 (Linux; Android 15; 24115RA8EC Build/AQ3A.240912.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/140.0.7339.207 Mobile Safari/537.36 NietaApp',
        'Accept': 'application/json, text/plain, */*',
        'Content-Type': 'application/json',
        'x-platform': 'nieta-app/android',
        'sec-ch-ua-platform': '"Android"',
        'sec-ch-ua': '"Chromium";v="140", "Not=A?Brand";v="24", "Android WebView";v="140"',
        'x-token': token,
        'x-teen-mode': '0',
        'sec-ch-ua-mobile': '?1',
        'x-channel-from': 'none',
        'x-abtest': 'abtest_ad_optimize_08-14=1;abtest_llm-v2_08-16=1;abtest_newbie_0920=1;abtest_typeahead_0924=1;abtest_ad_0927=1;abtest_inspiration_0927=1;abtest_ad_in_generate_1009=1;abtest_hidden_tabbar_1015=1;abtest_manga_10-22=1;abtest_recommendation_10-23=2;abtest_recommendation_personal_10-31=2;abtest_recsys_recommend_score_20251014=1;abtest_recsys_hash_tag_show_flag=1;abtest_recsys_new_personal_flag=1;abtest_recsys_new_personal_08-11=2;abtest_lowap_11-25=2;abtest_store_11-25=2;abtest_same_style_12-12=1;abtest_newbie_feed_12-30=1;abtest_generate_video_25-01-07=1;abtest_inspiration_recommend_25-02-20=2;abtest_generate_mkiii=1;abtest_rewarded_ad_suyi_25-02-26=1;abtest_create_sheet_25-03-07=2;abtest_use_adv_translator_default_25-03-14=2;abtest_generate_mkiii_layout_25-03-18=2;abtest_nienie_tab_25-03-19=1;abtest_ai-activity-25_03_27=2;abtest_nienie_recommend-25_04_08=2;abtest_advanced_translator_25_04_18=1;abtest_onboarding_character_user_25-04-21=2;abtest_onboarding-skip-disable-05-06=1;abtest_yinge_goods=1;abtest_verse_custom_editing_25-06-20=2;abtest_verse_custom_editing_25-08-14=1;abtest_nienie_new_user_feed-25_08_19=1;abtest_character_chat_08_22=2;abtest_limit_collection_card_aspect=2;abtest_community_style_0929=1;abtest_promotion_199=2;abtest_new_user_cta_status_20251106=2;abtest_nienie_feed_cta_style-25_11_06=2',
        'traceparent': '00-e9872f5786ed48fdbf08fe78b4d07a2e-6ea91983b2ca90f4-00',
        'x-nieta-app-version': '5.18.0',
        'tracestate': 'rum=v2&browser&gdua4ta81m@4143031597ade16&c1d31f22291845adac8e3d961517959f&uid_sjda003pqkfzrics',
        'b3': 'e9872f5786ed48fdbf08fe78b4d07a2e-6ea91983b2ca90f4-0',
        'origin': 'https://app.nieta.art',
        'x-requested-with': 'art.nieta.app',
        'sec-fetch-site': 'cross-site',
        'sec-fetch-mode': 'cors',
        'sec-fetch-dest': 'empty',
        'referer': 'https://app.nieta.art/',
        'accept-language': 'zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7',
        'priority': 'u=1, i',
    }

    json_data = {
        'uuid': '33df9341-4a7e-4e94-a01d-73b2939c1ca7',
    }

    response = requests.put('https://api.talesofai.cn/v1/assignment/complete-assignment-action', headers=headers,
                            json=json_data)
    print(response.text)
