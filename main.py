from pyscript import Element
import js

# 狀態變數
player_name = ""
player_gender = ""
current_stage = 1
current_floor = 1
hint_mode = True

def show_message(text):
    Element("game-area").element.innerHTML = f"<p>{text}</p>"

def show_input(prompt, input_id, button_text, next_func):
    Element("input-area").element.innerHTML = f"""
        <p>{prompt}</p>
        <input type="text" id="{input_id}">
        <button onclick="{next_func}()">{button_text}</button>
    """

def start_game():
    show_message("一場邏輯試煉即將展開。你將成為一名勇者。")
    Element("input-area").element.innerHTML = """
        <p>你想成為哪種勇者？</p>
        <button onclick="set_male()">男勇者</button>
        <button onclick="set_female()">女勇者</button>
    """

def set_male():
    global player_gender
    player_gender = "男勇者"
    ask_name()

def set_female():
    global player_gender
    player_gender = "女勇者"
    ask_name()

def ask_name():
    show_input("請輸入你的勇者名字：", "name-input", "確認", "set_name")

def set_name():
    global player_name
    player_name = js.document.getElementById("name-input").value
    if player_name.strip() == "":
        show_message("名字不能空白，請重新輸入。")
        ask_name()
    else:
        intro_first_stage()

def intro_first_stage():
    global current_stage, current_floor
    text = f"""你來到第 {current_stage} 關，也是這座迷宮的第 {current_floor} 層。
石頭大門緩緩開啟，上頭刻著：「學習目標：變數與輸入的基礎」。"""
    show_message(text)
    Element("input-area").element.innerHTML = """
        <button onclick="enter_stage()">進入迷宮</button>
    """

def enter_stage():
    if hint_mode:
        show_message(f"{player_gender} {player_name}，請輸入一個變數的名稱，例如：score")
    else:
        show_message("請輸入變數名稱：")
    Element("input-area").element.innerHTML = """
        <input type="text" id="var-name">
        <button onclick="check_variable()">確認</button>
    """

def check_variable():
    var_name = js.document.getElementById("var-name").value
    if var_name.isidentifier():
        show_message(f"太好了！你成功建立了一個變數：{var_name}。")
        Element("input-area").element.innerHTML = """
            <button onclick="stage_clear()">繼續</button>
        """
    else:
        show_message("這不是合法的變數名稱，請再試一次。")
        enter_stage()

def stage_clear():
    show_message("你成功通過了第一關！大門再次開啟，一道光照亮了前路。")
    Element("input-area").element.innerHTML = """
        <button onclick="next_stage()">前往下一層</button>
    """

def next_stage():
    global current_stage, current_floor
    current_stage += 1
    current_floor += 1
    show_message(f"（未實作）你已抵達第 {current_stage} 關，第 {current_floor} 層。更多關卡即將推出…")
    Element("input-area").element.innerHTML = ""

# 遊戲開始
start_game()
