#-*- coding:utf-8 -*-
def yn(question):
    ans = ""
    while ans not in ["y","n"]:
        ans=input(question + " (Y/N)").lower().strip()
    if ans=="y": return True
    else: return False
hiragana = [
    ["あ","い","う","え","お"],
    ["か","き","く","け","こ"],
    ["さ","し","す","せ","そ"],
    ["た","ち","つ","て","と"],
    ["な","に","ぬ","ね","の"],
    ["は","ひ","ふ","へ","ほ"],
    ["ま","み","む","め","も"],
    ["や","","ゆ","","よ"],
    ["ら","り","る","れ","ろ"],
    ["わ","","","","を"],["","","ん","",""], #unused, anyways.
    ["が","ぎ","ぐ","げ","ご"],
    ["ざ","じ","ず","ぜ","ぞ"],
    ["だ","ぢ","づ","で","ど"],
    ["ば","び","ぶ","べ","ぼ"],
    ["ぱ","ぴ","ぷ","ぺ","ぽ"]
    ]
def hiragana_loc(kana):
    for i in range(0,len(hiragana)):
        for j in range(0,len(hiragana[i])):
            if hiragana[i][j] == kana: return (i,j)
    return (-1,-1)
exception_godan = [
    "あせる","いる","いじる","うらぎる","える","おちいる","かえる","かぎる","かげる","きる","かじる","きしる","ぎゅうじる",
    "ける","さえぎる","しる","しげる","しめる","しゃべる","すべる","せる","ちる","ちぎる","てる","ねる","にぎる","ねじる","はいる",
    "はしる","ひねる","へる","まいる","まじる","まぜる","みなぎる","むしる","もじる","よみがえる"
] #Looks like ichidan, but actually godan. (Perhaps, because of homophones.)

def chkKana(word):
    for char in word:
        if hiragana_loc(char) == (-1,-1):
            print("Your input includes a character which is not hiragana. A problem may occur due to this.")
            return
def verb_group(verb):
    #NOT A VERB = -1
    #五段 0 OK
    #一段 1 OK
    #カ変 2
    #サ変 3
    #サ変 w/ずる 4 (follows サ変's conjugation, but requires extra implementaion.)

    x, y = hiragana_loc(verb[-2]) #index of the second last hiragana.

    #Check whether it is a verb.
    lastcharx, lastchary = hiragana_loc(verb[-1])
    if lastchary != 2:
        return -1

    #一段
    if y in [1,3] and verb[-1] == "る":
        if verb in exception_godan:
            if yn(verb + " seems to a Godan(五段) verb, but you might've meant an Ichidan(一段) verb which is its homophone. Are you sure that you have meant a Godan verb?"):
                return 0
        return 1

    #カ変
    if verb=="くる": return 2

    #サ変
    if verb=="する":
        if yn("する may be 為る, an irregular verb, or other Godan(五段) verbs. Do you mean 為る?"):
            return 3
        else:
            return 0
    if verb.endswith("する"): return 3
    
    #～ずる
    if verb.endswith("ずる"): return 4

    #五段
    return 0

verb = input("Verb in HIRAGANA> ").strip()

#Check non-hiragana
chkKana(verb)

group = verb_group(verb)
#print(group)

if group == -1:
    print("It dosen't seem to be a verb.")
    exit()
if group == 0:
    #Godan
    x, y = hiragana_loc(verb[-1]) #last char

    print("Verb: " + verb)
    print("Verb Group: Godan(五段)")
    print("-----")

    #テ形(Te form)
    te_form = verb[:-1]
    if verb == "いく":
        print("Te form(テ形): いって")
        print("past simple: いった")
    else:
        if verb[-1] in ["う","つ","る"]:
            te_form += "って"
        elif verb[-1] in ["む","ぶ","ぬ"]:
            te_form += "んで"
        elif verb[-1] == "く":
            te_form += "いて"
        elif verb[-1] == "ぐ":
            te_form += "いで"
        elif verb[-1] == "す":
            te_form += "して"
        else:
            raise NotImplementedError
        print("Te form(テ形): " + te_form)

        ta_form = verb[:-1]
        if verb[-1] in ["う","つ","る"]:
            ta_form += "った"
        elif verb[-1] in ["む","ぶ","ぬ"]:
            ta_form += "んだ"
        elif verb[-1] == "く":
            ta_form += "いた"
        elif verb[-1] == "ぐ":
            ta_form += "いだ"
        else:
            raise NotImplementedError
        print("past simple: " + ta_form)
    print()

    #連用形(Infinitive)
    renyoukei = verb[:-1] + hiragana[x][1]
    print("Infinitive(連用形): " + renyoukei)
    print("masu form(マス形): " + renyoukei + "ます")
    print()

    #未然形
    if verb[-1] == "う":
        print("Negative(ナイ形): " + verb[:-1] + "わ" + "ない")
        print("Causative: " + verb[:-1] + "わ" + "せる")
        print("Passive: " + verb[:-1] + "わ" + "れる")
        print("Causative passive: " + verb[:-1] + "わ" + "せられる")
    else:
        print("Negative(ナイ形): " + verb[:-1] + hiragana[x][0] + "ない")
        print("Causative: " + verb[:-1] + hiragana[x][0] + "せる")
        print("Passive: " + verb[:-1] + hiragana[x][0] + "れる")
        if verb[:-1] == "す":
            print("Causative passive: " + verb[:-1] + "させられる")
        else:
            print("Causative passive: " + verb[:-1] + hiragana[x][0] + "せられる" + " / " + verb[:-1] + hiragana[x][0] + "される")
    print("Presumptive: " + verb[:-1] + hiragana[x][4] + "う")
    print()

    #仮定形
    print("Conditional(仮定形): " + verb[:-1] + hiragana[x][3] + "ば")
    print("Potential: " + verb[:-1] + hiragana[x][3] + "る")
    print()

    #命令形
    print("Imperative(命令形): " + verb[:-1] + hiragana[x][3])
    print()
elif group == 1:
    #ichidan
    print("Verb: " + verb)
    print("Verb Group: Ichidan(一段)")
    print("-----")

    #連用形
    renyoukei = verb[:-1]
    print("Te form(テ形): " + renyoukei + "て")
    print("past simple: " + renyoukei + "た")
    print("Infinitive(連用形): " + renyoukei)
    print("masu form(マス形): " + renyoukei + "ます")
    print()

    #未然形
    print("Negative(ナイ形): " + renyoukei + "ない")
    print("Causative: " + renyoukei + "させる")
    print("Passive: " + renyoukei + "られる")
    print("Causavie Passive: " + renyoukei + "させられる")
    print("Presumptive: " + renyoukei + "よう")

    #仮定形
    print("Conditional(仮定形): " + renyoukei + "れば")
    print("Potential: " + renyoukei + "られる")

    #命令形
    print("Imperative(命令形): " + renyoukei + "ろ" + " / " + renyoukei + "よ")

elif group == 2:
    #来る
    print("Verb: くる")
    print("Verb Group: Irregular(カ行変格活用)")
    print("-----")

    #連用形
    renyoukei = verb[:-1]
    print("Te form(テ形): きて")
    print("past simple: きた")
    print("Infinitive(連用形): き")
    print("masu form(マス形): きます")
    print()

    #未然形
    print("Negative(ナイ形): こない")
    print("Causative: こさせる")
    print("Passive: こられる")
    print("Causavie Passive: こさせられる")
    print("Presumptive: こよう")

    #仮定形
    print("Conditional(仮定形): くれば")
    print("Potential: こられる")

    #命令形
    print("Imperative(命令形): こい")

elif group == 3:
    frontpart = ""
    if verb != "する": frontpart = verb[:-2]
    
    print("Verb: " + verb)
    print("Verb Group: Irregular(サ行変格活用)")
    print("-----")

    #連用形
    renyoukei = verb[:-1]
    print("Te form(テ形): " + frontpart + "して")
    print("past simple: " + frontpart + "した")
    print("Infinitive(連用形): " + frontpart + "し")
    print("masu form(マス形): " + frontpart + "します")
    print()

    #未然形
    print("Negative(ナイ形): " + frontpart + "しない")
    print("Causative: " + frontpart + "させる")
    print("Passive: " + frontpart + "される")
    print("Causavie Passive: " + frontpart + "させられる")
    print("Presumptive: " + frontpart + "しよう")

    #仮定形
    print("Conditional(仮定形): " + frontpart + "すれば")
    print("Potential: " + frontpart + "できる")

    #命令形
    print("Imperative(命令形): " + frontpart + "しろ" + " / " + frontpart + "せよ")

elif group == 4:
    #https://ja.wiktionary.org/wiki/%E8%AB%96%E3%81%9A%E3%82%8B

    if verb != "する": frontpart = verb[:-2]
    
    print("Verb: " + verb)
    print("Verb Group: Irregular(サ行変格活用)")
    print("-----")

    #連用形
    renyoukei = verb[:-1]
    print("Te form(テ形): " + frontpart + "じて")
    print("past simple: " + frontpart + "じた")
    print("Infinitive(連用形): " + frontpart + "じ")
    print("masu form(マス形): " + frontpart + "じます")
    print()

    #未然形
    print("Negative(ナイ形): " + frontpart + "じない")
    print("Causative: " + frontpart + "じさせる")
    print("Passive: " + frontpart + "ぜられる")
    print("Causavie Passive: " + frontpart + "じさせられる")
    print("Presumptive: " + frontpart + "じよう")

    #仮定形
    print("Conditional(仮定形): " + frontpart + "ずれば")
    print("Potential: " + frontpart + "ずれる")

    #命令形
    print("Imperative(命令形): " + frontpart + "じろ" + " / " + frontpart + "ぜよ")