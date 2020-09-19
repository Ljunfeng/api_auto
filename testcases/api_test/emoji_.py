
import emoji
# 表情库 https://www.webfx.com/tools/emoji-cheat-sheet/
# 默认的表情可以直接通过表情的字符实现
print(emoji.emojize('Python is :thumbs_up:')) # Python is 👍
# 有些特殊的表情需要指定 use_aliases=True 参数才可以实现
print(emoji.emojize('Sleeping is :zzz:', use_aliases=True)) # Sleeping is 💤

# 同时也支持反向操作
print(emoji.demojize('脑阔疼 🙉')) # 脑阔疼 :hear-no-evil_monkey: