# high_and_low_game.py
# computer_number が your number よりも大きいか小さいかを当ててもらう。

from random import randint

def get_answer():     # H か L を入力してもらう。
  while True:         # 無限ループを作成。
    ans = input("High(H) or Low(L) > ")
    if ans.upper() == "H" or ans.upper() == "L":     # H L の時無限ループを脱出, .upper()で大文字に変換
      break
  return ans.upper()


def main():
  player_count = 0
  computer_count = 0

  while player_count < 5 and computer_count < 5:     # 5回勝つと終了
    player_number = randint(1,13)     # 1 以上 13 以下をランダム
    print ("Your number:{}".format(player_number))     #.format で player_number を {}内に表示

    computer_number = randint(1,13)     # 1 以上 13 以下をランダム
    print ("Computer number: ?")

    answer = get_answer()
    balance = computer_number - player_number

    if balance == 0:
      print ("even")
    elif balance > 0 and answer == "H":
      print ("Hit!! あたり！")
      player_count += 1
    elif balance < 0 and answer == "L":
      print ("Hit!! あたり！")
      player_count += 1
    else:
      print ("Miss! 残念！")
      computer_count += 1

    print ("Computer number:{}".format(computer_number))     #.format で computer_number を {}内に表示
    print ("Next >>")
    print ("-------------------------")

  if player_count == 5:     # 5回勝つと終了
    print ("You Win!! あなたの勝ちです！")
  else:
    print ("You Lose! あなたの負けです！")


if __name__ == '__main__':     # 直接実行された時 main 関数を呼び出し
  main()
