class Weapon:
    def __init__(self, name, damage, rad) -> None:
        self.name = name
        self.damage = damage
        self.rad = rad

    def hit(self, actor, target):
        if not target.is_alive():
            print('Враг уже повержен')
        else:
            distance_x = target.get_coords()[0] - actor.get_coords()[0]
            distance_y = target.get_coords()[1] - actor.get_coords()[1]
            distance = (distance_x ** 2 + distance_y ** 2) ** 0.5
            if distance > self.rad:
                print(f'Враг слишком далеко для оружия {self.name}')
            else:
                print(f'Врагу нанесен урон оружием {self.name} в размере {self.damage}')
                target.get_damage(self.damage)

    def __str__(self) -> str:
        return self.name

class BaseCharacter:
    def __init__(self, pos_x, pos_y, hp) -> None:
        self.pos_x = pos_x
        self.pos_y = pos_y  
        self.hp = hp

    def move(self, delta_x, delta_y):
        self.pos_x += delta_x
        self.pos_y += delta_y

    def is_alive(self):
        if self.hp > 0:
            return True
        else:
            return False

    def get_damage(self, amount):
        self.hp -= amount

    def get_coords(self):
        return tuple([self.pos_x, self.pos_y])

class BaseEnemy(BaseCharacter):
    def __init__(self, pos_x, pos_y, weapon, hp) -> None:
        super().__init__(pos_x, pos_y, hp)
        self.weapon = weapon

    def hit(self, target):
        if type(target) == MainHero:
            self.weapon.hit(self, target)
        else:
            print(f'Могу ударить только Главного героя')

    def __str__(self) -> str:
        return f'Враг на позиции ({self.pos_x, self.pos_y}) с оружием {self.weapon}'


class MainHero(BaseCharacter):
    def __init__(self, pos_x, pos_y, name, hp) -> None:
        super().__init__(pos_x, pos_y, hp)
        self.name = name
        self.inventory = []
        self.count = 0

    def hit(self, target):
        if len(self.inventory) == 0:
            print('Я безоружен')
        elif type(target) == BaseEnemy:
            self.inventory[self.count].hit(self, target)
        else:
            print('Могу ударить только Врага')

    def add_weapon(self, weapon):
        if type(weapon) == Weapon:
            print(f'Подобрал {weapon}')
            self.inventory.append(weapon)
        else:
            print('Это не оружие')

    def next_weapon(self):
        if len(self.inventory) == 0:
            print('Я безоружен')
        elif len(self.inventory) == 1:
            print('У меня только одно оружие')
        else:
            self.count += 1
            print(f'Сменил оружие на {self.inventory[self.count]}')

    def heal(self, amount):
        if self.hp + amount <= 200:
            self.hp += amount
            print(f'Полечился, теперь здоровья {self.hp}')
        else:
            self.hp = 200
            print(f'Полечился, теперь здоровья {self.hp}')



weapon1 = Weapon("Короткий меч", 5, 1)
weapon2 = Weapon("Длинный меч", 7, 2)
weapon3 = Weapon("Лук", 3, 10)
weapon4 = Weapon("Лазерная орбитальная пушка", 1000, 1000)
princess = BaseCharacter(100, 100, 100)
archer = BaseEnemy(50, 50, weapon3, 100)
armored_swordsman = BaseEnemy(10, 10, weapon2, 500)
archer.hit(armored_swordsman)
armored_swordsman.move(10, 10)
print(armored_swordsman.get_coords())
main_hero = MainHero(0, 0, "Король Артур", 200)
main_hero.hit(armored_swordsman)
main_hero.next_weapon()
main_hero.add_weapon(weapon1)
main_hero.hit(armored_swordsman)
main_hero.add_weapon(weapon4)
main_hero.hit(armored_swordsman)
main_hero.next_weapon()
main_hero.hit(princess)
main_hero.hit(armored_swordsman)
main_hero.hit(armored_swordsman)
