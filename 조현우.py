import random
from typing import Type

class Player:
    def __init__(self):
        self.hp = 50  # 초기 체력
        self.ad = 10  # 초기 공격력
        self.ap = 5   # 초기 마법력

    # 사용자가 입력한 점수에 따라 플레이어의 스테이터스 포인트를 설정하는 메서드입니다.
    def status_set(self, point: int):
        print("------------------------------------------------------------------------------") 
        print(f"{point}만큼의 스테이터스를 추가합니다. 체력, 공격력, 마법력 순으로 입력하세요\n(1 포인트 당 체력 = 3, 공격력 = 1, 마법력 = 1 증가)\n")
        print("플레이어의 기본 스탯은 체력: 50, 공격력: 10, 마법력: 5입니다.\n")
        
        """
        - [게임 진행] 체력, 공격력, 마법력을 입력받고 , 주어진 포인트와 일치하는지 아닌지 출력하는 함수입니다
        - 1-(1) 체력, 공격력, 마법력을 공백을 기준으로 입력받습니다.
        - 1-(2) 체력, 공격력, 마법력의 합이 주어진 포인트와 일치하는지 확인하고, 변경된 스탯을 적용해 출력합니다.
        
        """
        while True:
            while True:
                try:
                    #TODO 1-(1): 사용자로부터 플레이어의 체력, 공격력, 마법력을 공백을 기준으로 입력받습니다.
                    hp_points, ad_points, ap_points = map(int, input("체력, 공격력, 마법력을 입력하세요: ").split())
                    ##### END OF TODO 1-(1)(문제와 본 라인 사이에 코드를 작성하세요.) #####
                    break
                except:
                    print("hp, ad, ap는 정수로 입력해야 합니다. 다시 입력해주세요.")
                    continue
                    
            #TODO 1-(2): 입력한 포인트가 주어진 포인트와 일치하는지 확인합니다. (포인트 당 체력 = 3, 공격력 = 1, 마법력 = 1 증가)
            if hp_points + ad_points + ap_points == point:
                self.hp += hp_points * 3
                self.ad += ad_points
                self.ap += ap_points
                print(f"체력: {self.hp}, 공격력: {self.ad}, 마법력: {self.ap}\n")
                break
            else:
                print("입력한 능력치의 총합이 13와 같아야 합니다. 다시 입력해주세요.")
            ##### END OF TODO 1-(2)(문제와 본 라인 사이에 코드를 작성하세요.) #####

    """
    - [게임 진행] 각 행동에 따라 (1: 스테이터스 확인 + 일반 공격, 2: 기본 공격, 3: 마법 공격, 4: 체력 회복)에 따른 동작 처리를 합니다
    - 2-(1) 기본 공격을 수행합니다.
    - 2-(2) 마법 공격을 수행합니다.
    - 2-(3) 체력을 회복합니다.
    """

    def decrease_hp(self, damage: int):
        self.hp = max(self.hp - damage, 0)
    
    def check_status(self, enemy):
        # 플레이어와 적의 현재 상태를 출력합니다.
        print(f"현재 유저: 체력 {self.hp}, 공격력 {self.ad}, 마법력 {self.ap}")
        print(f"적: 체력 {enemy.hp}, 공격력 {enemy.ad}, 방어력 {enemy.ad_defence}, 마법방어력 {enemy.ap_defence}\n")
        # 적에게 일반 공격을 가합니다.
        damage = self.ad - enemy.ad_defence
        enemy.decrease_hp(damage)
        print(f"일반 공격으로 {damage}의 데미지를 주었습니다.\n")

    def basic_attack(self, enemy: Type["Enemy"]):
        """
        TODO 2-(1) 
        - 치명타 -> 1부터 10 사이의 랜덤한 숫자를 생성합니다.
        - 치명타가 2보다 큰 경우, 일반공격으로 간주합니다.
        - 치명타가 2보다 작거나 같은 경우, 치명타가 발생한 것으로 간주합니다. 치명타가 발생한 경우, 플레이어의 공격력에서 적의 방어력을 뺀 후, 그 값을 두 배로 만들어 적의 체력에서 뺍니다.
        - 플레이어가 적에게 가한 데미지를 출력합니다.
        """
        crit_chance = random.randint(1, 10)
        if crit_chance <= 2:  # 치명타 발생
            damage = max((self.ad - enemy.ad_defence) * 2, 0)
            print(f"치명타가 적용되어 {damage}의 데미지를 주었습니다.\n")
        else:  # 일반 공격
            damage = max(self.ad - enemy.ad_defence, 0)
            print(f"일반 공격으로 {damage}의 데미지를 주었습니다.\n")
        enemy.decrease_hp(damage)
        ##### END OF TODO 2-(1)(문제와 본 라인 사이에 코드를 작성하세요.) #####

    def magic_attack(self, enemy: Type["Enemy"]):
        """
        TODO 2-(2) 
        - 플레이어의 마법 공격력의 두 배에서 적의 마법 방어력을 뺀 만큼의 데미지를 주게 됩니다.
        - 플레이어가 적에게 가한 데미지를 출력합니다.
        """ 
        damage = max((self.ap * 2) - enemy.ap_defence, 0)
        print(f"마법 공격으로 {damage}의 데미지를 주었습니다.\n")
        enemy.decrease_hp(damage)
        ##### END OF TODO 2-(2)(문제와 본 라인 사이에 코드를 작성하세요.) #####
        
        
    def heal_self(self):
        """
        TODO 2-(3) 
        - 무작위로 5에서 10 사이의 값을 선택하여 플레이어의 체력에 더합니다.
        - 회복된 플레이어의 현재 체력을 출력합니다. 
        """
        heal_amount = random.randint(5, 10)
        self.hp += heal_amount
        print(f"체력을 {heal_amount}만큼 회복했습니다. 현재 체력: {self.hp}\n")
        ##### END OF TODO 2-(3)(문제와 본 라인 사이에 코드를 작성하세요.) #####
    
    def attack(self, enemy: Type["Enemy"], player_index: int):
        # 사용자로부터 input key를 받아옵니다.
        while True:
            try:
                print("------------------------------------------------------------------------------") 
                print(f"{player_index + 1}번 플레이어의 차례입니다. 행동을 선택하세요. (1: 스테이터스 확인 + 일반 공격, 2: 기본 공격, 3: 마법 공격, 4: 체력 회복, exit: 종료)\n")
                input_key = input()             
                input_key = int(input_key)
                if input_key < 1 or input_key > 4:
                    print("1~4 사이의 정수를 입력해주세요.")
                    continue
                break
            except ValueError:
                print("잘못된 입력입니다. 숫자를 입력해주세요.")

        if input_key == 1:
            self.check_status(enemy)
    
        elif input_key == 2:
            self.basic_attack(enemy)

        elif input_key == 3:
            self.magic_attack(enemy)

        elif input_key == 4:
            self.heal_self()

class Enemy:
    """ 
    - [게임 진행]
    - 3-(1) 대상 플레이어의 체력을 적의 공격력 만큼 감소시킵니다.
    - 3-(2) 적의 행동에 무작위 값을 할당합니다.
    """
    # 적의 속성을 초기화합니다: 체력 (hp), 공격력 (ad), 공격 방어력 (ad_defence), 마법 방어력 (ap_defence), 최대 체력 (max_hp)
    def __init__(self, list_num: int):
        self.max_hp = 100 * list_num 
        self.hp = 100 * list_num     
        self.ad = 25    
        self.ad_defence = 7
        self.ap_defence = 7
    
    def decrease_hp(self, damage: int):
        self.hp = max(self.hp - damage, 0)
    
    def basic_attack(self, player: Type[Player], player_index: int):
        #TODO 3-(1): 공격 대상 플레이어의 체력을 적의 공격력만큼 감소시키고, 공격 받은 플레이어의 남은 체력을 출력합니다.
        damage = self.ad
        player.decrease_hp(damage)
        print(f"{player_index + 1}번 유저에게 {damage}의 데미지. 적의 공격으로 현재 남은 체력은 {player.hp}입니다.\n")
        ##### END OF TODO 3-(1)(문제와 본 라인 사이에 코드를 작성하세요.) #####

    def heal_self(self):
        healing_amount = 7
        if self.max_hp < (self.hp + healing_amount):
            print("적이 회복했지만 적은 이미 최대체력입니다.\n")
        else:
            self.hp += healing_amount
            print(f"적의 회복으로 현재 적의 체력은 {self.hp}입니다.\n")

    def attack(self, player: Type[Player], player_index: int):
      
        print("------------------------------------------------------------------------------") 
        print("적의 차례입니다.\n")
        #TODO 3-(2): enemy_action 변수에 무작위값을 할당합니다. (1부터 10사이)
        enemy_action = random.randint(1, 10)
        ##### END OF TODO 3-(2)(문제와 본 라인 사이에 코드를 작성하세요.) #####
        
        if enemy_action == 1:
            print("적은 섣불리 움직이지 못하고 있습니다.\n")
        elif 2 <= enemy_action <= 8:
            self.basic_attack(player, player_index)
        else:
            self.heal_self()
        return enemy_action

class Game:
    """ 
    - [게임 시작] 
    - 4-(1) 체력이 0이하인 플레이어의 인덱스를 제거합니다.
    - 4-(2) 타깃 플레이어를 랜덤으로 반환합니다.
    - 4-(3) 타깃 플레이어와 플레이어의 인덱스를 설정합니다.
    """
    def __init__(self):
        self.status_point = 13
        self.player_list = []

    def set_players(self):
        while True:
            try:
                list_num = int(input("플레이어 인원을 정하세요: "))
                if list_num <= 0:
                    print("플레이어 인원은 1 이상이어야 합니다.")
                    continue
                break
            except ValueError:
                print("잘못된 입력입니다. 숫자를 입력해주세요.")

        for _ in range(list_num):
            player = Player()
            player.status_set(self.status_point)
            self.player_list.append(player)

    
    def set_enemy(self):
        self.enemy = Enemy(len(self.player_list))

    def turn_check(self): 
        """
        TODO 4-(1)
        - 각 플레이어에 대해 반복하면서 플레이어의 체력이 0 이하인 경우, 
        해당 플레이어의 인덱스를 제거합니다. 
        - 람다 함수를 사용해 문제를 풀어보세요! (사용하지 않아도됩니다)
        """
        self.player_list = list(filter(lambda player: player.hp > 0, self.player_list))
        ##### END OF TODO 4-(1)(문제와 본 라인 사이에 코드를 작성하세요.) ##### 
        if len(self.player_list) == 0 or self.enemy.hp == 0:
            return False
        else:
            return True
        
    def select_target_player(self):
        """
        TODO 4-(2): 남은 플레이어들 중에서 무작위로 한 명을 선택해 반환해주세요!
        """
        return random.choice(self.player_list)
        ##### END OF TODO 4-(2)(문제와 본 라인 사이에 코드를 작성하세요.) ##### 

    def game(self):
        self.set_players()
        self.set_enemy()

        while(self.turn_check()):
            # 플레이어의 공격이 시작됩니다.
            for player_index, player in enumerate(self.player_list):
                player.attack(self.enemy, player_index)
                if self.enemy.hp == 0:
                    break
        
            if (self.turn_check()):
                #TODO 4-(3): 주어진 함수를 사용해 적이 공격할 대상과 해당 대상의 인덱스를 target_player, target_index에 할당합니다.
                target_player = self.select_target_player()
                target_index = self.player_list.index(target_player)
                ##### END OF TODO 4-(3)(문제와 본 라인 사이에 코드를 작성하세요.) #####

                self.enemy.attack(target_player, target_index)
            else:
                break
            
        if self.enemy.hp <= 0:
            print("축하합니다! 승리하셨습니다!")
        else:
            print("아쉽지만 패배하셨습니다.")

def main():
    game = Game()
    game.game()

if __name__=="__main__":
    main()
