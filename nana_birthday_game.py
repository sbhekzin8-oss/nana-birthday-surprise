import streamlit as st
from pathlib import Path
import html

BASE = Path(__file__).resolve().parent
VIDEO_PATH = BASE / "nana_birthday_surprise.mp4"
SONG_PATH = BASE / "lovely.mp3"  # Add a legally obtained copy of the song here.

st.set_page_config(page_title="For Nana ♡", page_icon="🌙", layout="centered")

QUESTIONS = [
    {"q": "Who created the heavens and the earth?", "options": ["Moses", "God", "David", "Noah"], "answer": "God", "verse": "Genesis 1:1"},
    {"q": "Who built the ark?", "options": ["Peter", "Abraham", "Noah", "Solomon"], "answer": "Noah", "verse": "Genesis 6–9"},
    {"q": "Where was Jesus born?", "options": ["Nazareth", "Jerusalem", "Bethlehem", "Jericho"], "answer": "Bethlehem", "verse": "Matthew 2:1"},
    {"q": "How many disciples did Jesus choose?", "options": ["7", "10", "12", "40"], "answer": "12", "verse": "Luke 6:13"},
    {"q": "What is the first book of the Bible?", "options": ["Exodus", "Genesis", "Psalms", "Matthew"], "answer": "Genesis", "verse": "Genesis 1:1"},
    {"q": "What is the shortest verse in many English Bible translations?", "options": ["Pray always", "Jesus wept", "God is love", "Be still"], "answer": "Jesus wept", "verse": "John 11:35"},
]
DEFAULTS = {"step": 0, "feeling": "", "question": 0, "answers": {}, "feedback": "", "sing": "", "video_open": False, "quest_started": False, "song_bytes": None}
for key, value in DEFAULTS.items():
    if key not in st.session_state:
        st.session_state[key] = value

st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Cinzel:wght@500;700;900&family=Nunito:wght@400;700;900&display=swap');
.stApp {background:radial-gradient(ellipse at top,#26183d 0%,#0b0b14 48%,#040407 100%);color:#f4efff;font-family:Nunito,sans-serif}
.block-container{max-width:800px;padding-top:1.2rem;padding-bottom:2.5rem}
.hero,.card{background:linear-gradient(145deg,#191526ee,#0b0b13f7);border:1px solid #8068ad;border-radius:24px;padding:24px;text-align:center;box-shadow:0 0 30px #8b5cf633;animation:fadeIn .65s ease both;margin-bottom:12px}
@keyframes fadeIn{from{opacity:0;transform:translateY(12px)}to{opacity:1;transform:translateY(0)}}
@keyframes heartbeat{0%,100%{transform:scale(1)}14%{transform:scale(1.16)}28%{transform:scale(1)}42%{transform:scale(1.1)}70%{transform:scale(1)}}
@keyframes floatUp{0%{transform:translateY(12px);opacity:0}20%{opacity:.9}100%{transform:translateY(-35px);opacity:0}}
.heart-stage{position:relative;height:125px;display:flex;align-items:center;justify-content:center;overflow:hidden;background:radial-gradient(ellipse at center,#512144 0%,#191326 55%,transparent 80%);border-radius:18px;margin:8px 0 16px}
.heart{font-size:72px;line-height:1;animation:heartbeat 2.1s ease-in-out infinite;filter:drop-shadow(0 0 15px #fb7185);display:inline-block}
.spark{position:absolute;color:#f9a8d4;font-size:20px;animation:floatUp 3s ease-in-out infinite}.s1{left:17%;top:62%}.s2{left:75%;top:62%;animation-delay:1s}.s3{left:34%;top:15%;animation-delay:1.6s}.s4{left:84%;top:18%;animation-delay:.7s}
.hero h1{font-family:Cinzel,serif;color:#f0d5ff;font-size:clamp(2rem,6vw,3.2rem);font-weight:900;text-shadow:0 0 18px #a78bfa66}
h2,h3{color:#dfc9ff;font-family:Cinzel,serif}p,label,.stMarkdown{color:#eee8ff}
.stProgress>div>div>div>div{background:#d16bba}
div.stButton>button{border:1px solid #a78bfa;border-radius:14px;background:linear-gradient(135deg,#30213f,#151322);color:#fff5ff;font-weight:800;min-height:2.9rem;transition:all .2s}
div.stButton>button:hover{border-color:#f0abfc;box-shadow:0 0 18px #a78bfa77;color:white;transform:translateY(-1px)}
div[data-testid="stRadio"] label{background:#171727;border:1px solid #51446c;border-radius:12px;padding:8px 12px;margin:5px 0}
.stAlert{background:#171727;border:1px solid #7764a8;color:#fff}footer{visibility:hidden}
</style>
""", unsafe_allow_html=True)

st.markdown("""
<div class="hero">
  <div class="heart-stage"><span class="spark s1">✦</span><span class="spark s2">♡</span><span class="spark s3">✧</span><span class="spark s4">✦</span><span class="heart">💗</span></div>
  <div style="color:#c4b5fd;letter-spacing:.25em;font-weight:900;font-size:.78rem">A MIDNIGHT BIRTHDAY SURPRISE</div>
  <h1>Happy Birthday, Nana ♡</h1>
  <p>A little world of moonlight, faith, and birthday magic made just for you. 🌙✝️</p>
  <div style="font-size:1.4rem">☾ ✦ 🕯️ ✦ ☽</div>
</div>
""", unsafe_allow_html=True)

if not st.session_state.video_open:
    st.markdown("<div class='card'><h2>A birthday movie for Nana 🎂</h2><p>Turn your sound on if you can, then open your surprise.</p></div>", unsafe_allow_html=True)
    if st.button("🎬 Open Nana's birthday video", use_container_width=True):
        st.session_state.video_open = True
        st.rerun()
    st.stop()

if not st.session_state.quest_started:
    if VIDEO_PATH.exists():
        st.video(str(VIDEO_PATH), autoplay=True, muted=False)
    else:
        st.info("Put nana_birthday_surprise.mp4 in the same folder as this Python file to show the birthday video.")
    if st.button("Start Nana's birthday quest ✨", use_container_width=True):
        st.session_state.quest_started = True
        st.rerun()
    st.stop()

if st.session_state.step == 0:
    st.markdown("<div class='card'><div class='heart-stage'><span class='spark s1'>✦</span><span class='spark s2'>♡</span><span class='heart'>💗</span></div><h2>Hey, Nana, birthday princess 👑</h2><p>First, tell me how your special day went.</p></div>", unsafe_allow_html=True)
    a,b,c=st.columns(3)
    with a:
        if st.button("✨ Amazing!", use_container_width=True): st.session_state.feeling="amazing"; st.session_state.step=2; st.rerun()
    with b:
        if st.button("🌌 Pretty good", use_container_width=True): st.session_state.feeling="good"; st.session_state.step=2; st.rerun()
    with c:
        if st.button("🖤 A little tough", use_container_width=True): st.session_state.feeling="tough"; st.session_state.step=2; st.rerun()

elif st.session_state.step == 2:
    messages={"amazing":"Yay! I hope God filled your day with joy and beautiful moments. ✨", "good":"I hope your day had little moments that made you smile. May God bless your new year. 🌙", "tough":"I'm sorry it was a tough day. You are still precious, and I hope God brings you comfort and peace. 🖤"}
    st.markdown(f"<div class='card'><div style='font-size:2.8rem'>💜✨</div><h2>A little birthday blessing</h2><p>{messages.get(st.session_state.feeling, '')}</p><h3>Ready for the Bible challenge, Nana?</h3><p>Six questions about the Bible are waiting. If you miss one, you'll see <b>“Sorry, princess 🖤”</b> and learn the answer.</p></div>", unsafe_allow_html=True)
    if st.button("Begin the faith quiz ✦", use_container_width=True): st.session_state.step=3; st.rerun()

elif st.session_state.step == 3:
    i=st.session_state.question
    if i < len(QUESTIONS):
        q=QUESTIONS[i]
        st.progress(i/len(QUESTIONS), text=f"Question {i+1} of {len(QUESTIONS)} · Nana's faith quest")
        st.markdown(f"<div class='card'><div style='font-size:2rem'>✦ 🕯️ ✝️ 🕯️ ✦</div><h2>Question {i+1}</h2><h3>{html.escape(q['q'])}</h3></div>", unsafe_allow_html=True)
        selected=st.radio("Choose your answer:", q["options"], key=f"answer_{i}", label_visibility="collapsed")
        if st.button("Lock in answer 🔐", use_container_width=True, key=f"submit_{i}"):
            st.session_state.answers[i]=selected
            if selected == q["answer"]: st.session_state.feedback=f"correct|Correct, princess! ✨ You got it. ({q['verse']})"
            else: st.session_state.feedback=f"wrong|Sorry, princess 🖤 The correct answer is **{q['answer']}**. Read {q['verse']} to learn more."
            st.session_state.step=4; st.rerun()
    else:
        st.session_state.step=5; st.rerun()

elif st.session_state.step == 4:
    kind, message=st.session_state.feedback.split("|",1)
    if kind == "correct":
        st.success(message)
        st.markdown("<div class='card'><div style='font-size:3rem'>👑✨</div><h2>Well done, Nana!</h2><p>Keep growing in faith and learning God's Word.</p></div>", unsafe_allow_html=True)
    else:
        st.warning(message)
        st.markdown("<div class='card'><div style='font-size:3rem'>🌙🖤</div><h2>It's okay, princess</h2><p>Every question is a chance to learn. You've got this!</p></div>", unsafe_allow_html=True)
    if st.button("Next question ✦", use_container_width=True):
        st.session_state.question += 1; st.session_state.feedback=""; st.session_state.step=3; st.rerun()

elif st.session_state.step == 5:
    score=sum(1 for i,q in enumerate(QUESTIONS) if st.session_state.answers.get(i)==q["answer"])
    st.markdown(f"<div class='hero'><div style='font-size:3.5rem'>👑🌙✝️</div><h1>Quest complete, Nana!</h1><h2>{score} / {len(QUESTIONS)} correct</h2><p>May you keep your faith close and your heart hopeful.</p><p style='color:#d8b4fe'>“The Lord is my strength and my shield.” — Psalm 28:7</p></div>", unsafe_allow_html=True)
    st.markdown("<div class='card'><h3>One last birthday surprise… 🎶</h3><p>Would you like to hear <i>Lovely</i> by Billie Eilish and Khalid?</p><p style='font-size:.9rem;color:#c4b5fd'>The song file needs to be supplied separately; the app cannot download copyrighted music for you.</p></div>", unsafe_allow_html=True)
    if SONG_PATH.exists():
        if st.button("💗 Yes, play my song!", use_container_width=True): st.session_state.sing="yes"; st.session_state.step=6; st.rerun()
        if st.button("🌙 Maybe another time", use_container_width=True): st.session_state.sing="no"; st.session_state.step=7; st.rerun()
    else:
        song_upload = st.file_uploader("Add a song audio file you have permission to use (MP3/WAV/M4A)", type=["mp3","wav","m4a"], key="song_upload")
        if song_upload is not None:
            st.session_state.song_bytes = song_upload.getvalue()
            st.audio(st.session_state.song_bytes, format="audio/mpeg", autoplay=False)
            st.caption("Press play to listen. Browsers may block automatic sound playback.")
        a,b=st.columns(2)
        with a:
            if st.button("💗 Yes, play the song", use_container_width=True):
                if st.session_state.song_bytes: st.session_state.sing="yes"; st.session_state.step=6; st.rerun()
                else: st.info("Choose an audio file first, Nana's surprise is waiting! 🎶")
        with b:
            if st.button("🌙 Maybe another time", use_container_width=True): st.session_state.sing="no"; st.session_state.step=7; st.rerun()

elif st.session_state.step == 6:
    st.markdown("<div class='card'><div style='font-size:3rem'>🎧💗</div><h2>A song for Nana</h2><p>Enjoy your little birthday soundtrack. 🌙</p></div>", unsafe_allow_html=True)
    if SONG_PATH.exists(): st.audio(str(SONG_PATH), format="audio/mpeg", autoplay=True)
    elif st.session_state.song_bytes: st.audio(st.session_state.song_bytes, autoplay=True)
    st.caption("If it doesn't start automatically, tap play—some browsers block autoplay.")
    if st.button("Finish the birthday quest ✨", use_container_width=True): st.session_state.step=7; st.rerun()

else:
    st.markdown("<div class='hero'><div style='font-size:4rem'>🌑 ✨ 👑</div><h1>Happy Birthday, Nana ♡</h1><p>May God guide you, protect you, and fill your year with peace, joy, love, and purpose.</p><div style='font-size:1.6rem'>✝️ ☾ ✦ ☽</div><p>You are loved and celebrated today. 🖤</p></div>", unsafe_allow_html=True)
    if st.button("Play the game again", use_container_width=True):
        for key,value in DEFAULTS.items(): st.session_state[key]=value
        st.rerun()

st.caption("Made for Nana with faith, moonlight, and birthday magic. ✦")
