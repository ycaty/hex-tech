# -*- coding: utf-8 -*-
#!/usr/bin/env python
import re

bio="""❤️ 🧡 💛 💚 💙 ggnore 💜 🖤 🤍 🤎 💔 ❣️ 💕 💞 💓 💗 💖 💘 💝 
💟 ☮️ ✝️cake ☪️ 🕉 ☸️ ✡️ 🔯 🕎 ☯️ ☦️ 🛐 ⛎ ♈️ ♉️ ♊️ ♋️ ♌️ ♍️ ♎️ ♏️ ♐️ ♑️ ♒️ ♓ rawr️ 🆔 ⚛️ 
🉑 ☢️ ☣️ 📴 📳 🈶 🈚 loot️ 🈸 🈺 🈷️ ✴️ 🆚 💮 🉐 ㊙️ ㊗️ 🈴 🈵 🈹 🈲 🅰️ 🅱️ 🆎 🆑 🅾️ 🆘 
❌ ⭕️ 🛑 ⛔️ 📛 🚫 💯 💢 ♨️ 🚷 🚯 🚳 🚱 🔞 📵 🚭 ❗️ ❕ ❓ ❔ ‼️ ⁉️ 🔅 🔆 〽️ 
⚠️ 🚸 🔱 ⚜️ 🔰 ♻️ ✅ 🈯️ 💹 ❇️ ✳️ ❎ 🌐 💠 Ⓜ️ 🌀 💤 🏧"""

def bioSplicer(bio):
    '''
    Returns List ['hello','world']
    Removes unicode/junk text
    returns list of all words found in lowercase
    used for testing keyword/negative keyword search
    '''

    regex = r'\b\w+\b'
    return [x.lower() for x in re.findall(regex,bio)]

keywords = bioSplicer(bio)
print keywords

