# Credits to @davidteather for tiktok-api
# https://github.com/davidteather/tiktok-api

# Ref https://www.youtube.com/watch?v=zwLmLfVI-VQ&t=117s to pass captcha

import json
import os
import random
import string

import pandas as pd
from TikTokApi import TikTokApi

verifyFp = 'verify_kqw0ttrs_wK2PnXNV_NVdf_4NDO_9906_1IfVeQG13jQg'
did = ''.join(random.choice(string.digits) for num in range(19))

api = TikTokApi.get_instance(custom_verifyFp=verifyFp,
                             use_test_endpoints=True,
                             custom_did=did)

n_videos = 2000
# username = 'username'
# user_videos = api.byUsername(username, count=n_videos)
hashtag = 'thepenthouse3'
hashtag_posts = api.by_hashtag(hashtag=hashtag, count=n_videos, offset=0)

hashtag_posts_df = pd.DataFrame(hashtag_posts)
final_df = hashtag_posts_df[[
    'id', 'desc', 'createTime', 'video', 'author', 'music', 'challenges',
    'stats', 'duetInfo', 'originalItem', 'officalItem', 'textExtra', 'secret',
    'forFriend', 'digged', 'itemCommentStatus', 'showNotPass', 'vl1',
    'itemMute', 'authorStats', 'privateItem', 'duetEnabled', 'stitchEnabled',
    'shareEnabled', 'isAd', 'stickersOnItem', 'warnInfo', 'effectStickers'
]]

# final_df = pd.json_normalize(final_df, errors='ignore', sep='_')
json_struct = json.loads(final_df.to_json(orient="records"))
df_flat = pd.json_normalize(json_struct, sep='_')  #use pd.io.json

output_path = 'search_output'
if not os.path.exists(output_path):
    os.makedirs(output_path)

print(len(df_flat))
df_flat.to_json(os.path.join(output_path, '#{}_posts.json'.format(hashtag)),
                orient='records')
df_flat.to_excel(os.path.join(output_path, '#{}_posts.xlsx'.format(hashtag)),
                 index=False)

# def simple_dict(tiktok_dict):
#     to_return = {}
#     to_return['user_name'] = tiktok_dict['author']['uniqueId']
#     to_return['user_id'] = tiktok_dict['author']['id']
#     to_return['video_id'] = tiktok_dict['id']
#     to_return['video_desc'] = tiktok_dict['desc']
#     to_return['video_time'] = tiktok_dict['createTime']
#     to_return['video_length'] = tiktok_dict['video']['duration']
#     to_return['video_link'] = 'https://www.tiktok.com/@{}/video/{}?lang=en'.format(to_return['user_name'], to_return['video_id'])
#     to_return['num_of_likes'] = tiktok_dict['stats']['diggCount']
#     to_return['num_of_shares'] = tiktok_dict['stats']['shareCount']
#     to_return['num_of_comments'] = tiktok_dict['stats']['commentCount']
#     to_return['num_of_plays'] = tiktok_dict['stats']['playCount']
#     return to_return

# n_videos = 2000
# liked_videos = api.userLikedbyUsername(username, count=n_videos)
# liked_videos = [simple_dict(v) for v in liked_videos]

# liked_videos_df = pd.DataFrame(liked_videos)
# liked_videos_df.to_csv('{}_liked_videos.csv'.format(username), index=False)

# user_videos = [simple_dict(v) for v in user_videos]
# user_videos_df = pd.DataFrame(user_videos)
# user_videos_df.to_csv('{}_videos.csv'.format(username),index=False)
