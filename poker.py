import math
import random
import copy

# トランプの初期化
def card_initialize():
      card_list = [0 for i in range(52)]
      return card_list

# カードを配る
def card_distribute(card_list,used_set=set()):
      """
      card_list : 52 length list
      """
      hand = []
      used_set = used_set
      while(len(hand) != 5):
            element = random.randint(0,51)
            if element not in used_set:
                  hand.append(element)
                  used_set.add(element)
            
            
      hand.sort()
      return hand, used_set


# 手札の整理
def hand_making(hand):
      """
            hand : 5 length list
      """

      hand_number_list = []
      for i in hand:
            hand_number_list.append(i % 13 + 1)
      hand_suit = []
      for i in hand:
            if i <= 13:
                  hand_suit.append("Heart")
            elif i <= 26:
                  hand_suit.append("Spade")
            elif i <= 39:
                  hand_suit.append("Diamond")
            else:
                  hand_suit.append("Club")
      
      hands = [hand_number_list,hand_suit]
      return hands

# 手札の数字を辞書化
def pair_discriminator_function(hand):
      pair_discriminator = dict()
      # pair_discriminatorの初期化
      for number in hand:
            pair_discriminator[number] = 0
      for number in hand:
            pair_discriminator[number] += 1
      return pair_discriminator

# 役を判定する
def judgment_of_the_role(hand):
      '''
      hand : 2*5 array
      '''
      role = 0 # High card
      max_num = max(hand[0])
      straight_flug = 0 # straightの判定
      flush_flug = 0 # flushの判定
      pair_discriminator = pair_discriminator_function(hand[0])



      # suit_discriminator:
      suit_discriminator = dict()
      for suit in hand[1]:
            suit_discriminator[suit] = 0
      for suit in hand[1]:
            suit_discriminator[suit] += 1
      

      # One pair
      if max(pair_discriminator.values()) == 2 and len(pair_discriminator) == 4:
            role = 1
            
            
      # Two pair
      elif max(pair_discriminator.values()) == 2 and len(pair_discriminator) == 3:
            role = 2 


      # Three of a kind
      elif max(pair_discriminator.values()) == 3 and len(pair_discriminator) == 3:
            role = 3
      
      # Full house
      elif max(pair_discriminator.values()) == 3 and len(pair_discriminator) == 2:
            role = 6

      # Four of a kind
      elif max(pair_discriminator.values()) == 4 :
            role = 7

      # straight
      diff = []
      hand_sorted_num = copy.deepcopy(hand[0])
      hand_sorted_num.sort()
      for num1,num2 in zip(hand_sorted_num[1:],hand_sorted_num[:-1]):
            diff.append(num1-num2)
      
      if diff == [1,1,1,1] or hand_sorted_num == [0,9,10,11,12]:
            role = 4
            straight_flug = 1
            #print("str:",1)
      
      #if diff == :
      #      role = 4
      #      straight_flug == 1


      # Flush
      if max(suit_discriminator.values()) == 5:
            role = 5
            flush_flug = 1
            #print("flu:",1)

      # straight flush
      if flush_flug == 1 and straight_flug == 1:
            role = 8

      # Royal straight flush
      if hand[0] == [0,9,10,11,12] and flush_flug == 1:
            role = 9
      

      '''
      if len(pair_discriminator) == 4:
            role = 1
      elif len(pair_discriminator) == 3:
            
      elif len(pair_discriminator) == 2:
      '''
      return role

# 役を出力する
def role2name(role):
      """
            role : int
      """
      if role == 0:
            print("high cards...")
      elif role == 1:
            print("one pair!")
      elif role == 2:
            print("two pair!")
      elif role == 3:
            print("three of a kind!")
      elif role == 4:
            print("straight!!")
      elif role == 5:
            print("flush!!")
      elif role == 6:
            print("a full house!!!")
      elif role == 7:
            print("four of a kind!!!!")
      
      elif role == 8:
            print("straight flush!!!!")
      elif role == 9:
            print("Royal straight flush!!!!!")
      else :
            print("five of a kind!!!!!")

def card1to14(hand):
      for num in hand:
            if num == 1:
                  hand.remove(num)
                  hand.append(14)
      return hand

def judgment_game(player_role,enemy_role,player_card,enemy_card):
      player_card[0] = card1to14(player_card[0])
      enemy_card[0] = card1to14(enemy_card[0])
      if player_role > enemy_role:
            print("player win!")
      elif player_role < enemy_role:
            print("player lose...")
      else :
            if player_role == 0:
                  if max(player_card[0]) > max(enemy_card[0]):
                        print("player win!")
                  elif max(player_card[0]) < max(enemy_card[0]):
                        print("player lose...")
                  else :
                        print("draw.")

            if player_role == 1:
                  player_discriminator = pair_discriminator_function(player_card[0])
                  enemy_discriminator = pair_discriminator_function(enemy_card[0])
                  max_P_num = max(player_discriminator, key=player_discriminator.get)
                  kick_P_num = max([kv for kv in player_discriminator.items() if kv[1] == min(player_discriminator.values())])[0]
                  max_E_num = max(enemy_discriminator, key=enemy_discriminator.get)
                  kick_E_num = max([kv for kv in enemy_discriminator.items() if kv[1] == min(enemy_discriminator.values())])[0]
                  if max_P_num > max_E_num:
                        print("player win!")
                  elif max_P_num < max_E_num:
                        print("player lose...")
                  else :
                        if kick_P_num > kick_E_num:
                              print("player win!")
                        elif kick_P_num < kick_E_num:
                              print("player lose...")
                        
                        else :
                              print("draw.")

                  

# main文
if __name__ == "__main__":
      card_list = card_initialize()
      my_role = 0
      enemy_role = 0
      my_card, my_used_set = card_distribute(card_list)
      my_card = hand_making(my_card)
      my_role = judgment_of_the_role(my_card)
      enemy_card, enemy_used_set = card_distribute(card_list, my_used_set)
      enemy_card = hand_making(enemy_card)
      enemy_role = judgment_of_the_role(enemy_card)

      print(my_card)
      print(enemy_card)
      role2name(my_role)
      role2name(enemy_role)

      judgment_game(my_role,enemy_role,my_card,enemy_card)

