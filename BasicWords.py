def particles_list() -> list:
    particles = ["は","が","を","に"]#,"と","で","も","から","まで"]
    return particles

def aru_conjugations() -> dict:
    conjs = {
        "ある": ["there is, there are, have", "casual"],
        "ない": ["there is not, there are not, do not have", "casual"],
        "あります": ["there is, there are, have", "teineigo (formal)"],
        "ありません": ["there is not, there are not, do not have", "teineigo (formal)"],
        "あった": ["there was, there were, had", "casual"],
        "ありました": ["there was, there were, had", "teineigo (formal)"],
        "なかった": ["there was not, there were not, did not have", "casual"],
        "ありませんでした": ["there was not, there were not, did not have", "teineigo (formal)"]
    }
    return conjs

def suru_conjugations() -> dict:
    conjs = {
        "する": ["will do", "casual"],
        "します": ["will do", "teineigo (formal)"],
        "しない": ["will not do", "casual"],
        "しません": ["will not do", "teineigo (formal)"],
        "した": ["did", "casual"],
        "しました": ["did", "teineigo (formal)"],
        "しなかった": ["did not do", "casual"],
        "しませんでした": ["did not do", "teineigo (formal)"],
        "している": ["doing", "casual"],
        "しています": ["doing", "teineigo (formal)"],
        "していない": ["have not done/ not doing", "casual"],
        "していません": ["have not done/ not doing", "teineigo (formal)"],
        "してた": ["was doing", "casual"],
        "していました": ["was doing", "teineigo (formal)"],
        "してなかった": ["was not doing", "casual"],
        "していませんでした": ["was not doing", "teineigo (formal)"]
    }
    return conjs

def iku_conjugations() -> dict:
    conjs = {
        "行く": ["will go", "casual"],
        "行きます": ["will go", "teineigo (formal)"],
        "行かない": ["will not go", "casual"],
        "行きません": ["will not go", "teineigo (formal)"],
        "行った": ["went", "casual"],
        "行きました": ["went", "teineigo (formal)"],
        "行かなかった": ["did not go", "casual"],
        "行きませんでした": ["did not go", "teineigo (formal)"],
        "行っている": ["going", "casual"],
        "行っています": ["going", "teineigo (formal)"],
        "行っていない": ["have not gone/ not going", "casual"],
        "行っていません": ["have not gone/ not going", "teineigo (formal)"],
        "行っていた": ["was going", "casual"],
        "行っていました": ["was going", "teineigo (formal)"],
        "行ってなかった": ["was not going", "casual"],
        "行っていませんでした": ["was not going", "teineigo (formal)"]
    }
    return conjs

def iru_conjugations() -> dict:
    conjs = {
        "いる": ["am, is, are", "casual"],
        "いない": ["am not, is not, are not", "casual"],
        "います": ["am, is, are", "teineigo (formal)"],
        "いません": ["am not, is not, are not", "teineigo (formal)"],
        "いった": ["was, were", "casual"],
        "いました": ["was, were", "teineigo (formal)"],
        "いなかった": ["was not, were not", "casual"],
        "いませんでした": ["was not, were not", "teineigo (formal)"]
    }
    return conjs

def verb_conjugations() -> dict:
    conjs = {
        "ました": ["did", "teineigo (formal)"],
        "なかった": ["did not do", "casual"],
        "ませんでした": ["did not do", "teineigo (formal)"],
        "ます": ["will do", "teineigo (formal)"],
        "ない": ["will not do", "casual"],
        "ません": ["will not do", "teineigo (formal)"],
        "た": ["did", "casual"],
        "だ": ["did", "casual"]
    }
    return conjs

def te_conjugations() -> dict:
    conjs = {
        "ました": ["was doing", "teineigo (formal)"],
        "なかった": ["was not doing", "casual"],
        "いませんでした": ["was not doing", "teineigo (formal)"],
        "る": ["doing", "casual"],
        "ます": ["doing", "teineigo (formal)"],
        "ない": ["have not done/ not doing", "casual"],
        "ません": ["have not done/ not doing", "teineigo (formal)"],
        "た": ["was doing", "casual"],
        "だ": ["did", "casual"]
    }
    return conjs

def adverbial_nouns() -> dict:
    adverbial_nouns = {
        "毎日": "everyday",
        "いつも": "always",
        "ときどき": "sometimes",
        "たまに": "occasionally",
        "普通に": "normally",
        "ちょっと": "a little",
        "少し": "a bit",
        "全然": "not at all",
        "かなり": "quite",
        "とても": "very",
        "まったく": "completely",
        "きっと": "surely",
        "もうすぐ": "soon",
        "絶対に": "absolutely",
        "必ず": "certainly",
        "たくさん": "a lot",
        "すぐに": "immediately",
        "まだまだ": "still",
        "だいたい": "mostly"
    }
    return adverbial_nouns

def hiragana() -> list:
    hiragana_list = ['あ', 'い', 'う', 'え', 'お', 'か', 'が', 'き', 'ぎ', 'く', 'ぐ', 'け', 'げ', 'こ', 'ご', 
                     'さ', 'ざ', 'し', 'じ', 'す', 'ず', 'せ', 'ぜ', 'そ', 'ぞ', 'た', 'だ', 'ち', 'ぢ', 'つ', 
                     'づ', 'て', 'で', 'と', 'ど', 'な', 'に', 'ぬ', 'ね', 'の', 'は', 'ば', 'ぱ', 'ひ', 'び', 
                     'ぴ', 'ふ', 'ぶ', 'ぷ', 'へ', 'べ', 'ぺ', 'ほ', 'ぼ', 'ぽ', 'ま', 'み', 'む', 'め', 'も', 
                     'や', 'ゆ', 'よ', 'ら', 'り', 'る', 'れ', 'ろ', 'わ', 'を', 'ん', 'ゃ', 'ゅ', 'ょ', 'っ']
    return hiragana_list

def copulas() -> dict:
    japanese_copulas = {
        "だった": ["was, were", "casual"],
        "でした": ["was, were", "teineigo (formal)"],
        "じゃなかった": ["was not, were not", "casual"],
        "ではありませんでした": ["was not, were not", "teineigo (formal)"],
        "です": ["is, am, are, be", "teineigo (formal)"],
        "だ": ["is, am, are, be", "casual"],
        "じゃない": ["is not, am not, are not, be not", "casual"],
        "ではない": ["is not, am not, are not, be not", "teineigo (formal)"],
        "じゃありません": ["is not, am not, are not, be not", "teineigo (formal)"],
        "ではありません": ["is not, am not, are not, be not", "teineigo (formal)"]
    }
    return japanese_copulas
