"""
List: TODO
* make create a new type car by user.
* make graphic part:
    . menu
    . attack, win, lose animations.
"""

from random import randrange, choice


class Vehicle:
    """A parent/common class"""

    def __init__(self, name="_", health=100, damage=10, money=0, upgrade_price=20, armor=0):
        self.name = name
        self.health = health
        self.damage = damage
        self.armor = armor
        self.money = money
        self.upgrade_price = upgrade_price
        self.health_next_rise = 15
        self.damage_next_rise = 5
        self.armor_next_rise = 5
        self.level = 1

    def increase_money(self, min_value=10, max_value=16):
        """Randomly increases the money in the given range(from min_value to max_value)"""
        self.money += randrange(min_value, max_value)

    def attack(self, *cars):
        """randomly attacks a car from imputed cars by self.damage ± 2 and increases money for both cars"""
        car = choice(cars)
        force = randrange(self.damage - 2, self.damage + 3) - car.armor
        if force > 0:
            car.health -= force
            print(f'{self.name} attacked {car.name} by force {force} !!!')
        else:
            print(f"{self.name} tried to attack {car.name}, but the armor is stronger than attack.")
        self.increase_money()
        car.increase_money(5, 11)

    def is_upgradable(self):
        """Checks if upgrade is available. returns True uf yes and False if no"""
        return self.money >= self.upgrade_price

    def upgrade_damage(self):
        """Upgrades damage if enough money and increases upgrade_price"""
        if self.is_upgradable():
            self.money -= self.upgrade_price
            self.damage += self.damage_next_rise
            self.level += 1
            self.damage_next_rise += 2
            self.upgrade_price += 5
            print("The damage successfully upgraded")
        else:
            print("Not enough money")
            print(f"{self.upgrade_price} $ is needed for upgrade. You have {self.money} $")

    def upgrade_health(self):
        """Upgrades health if enough money and increases upgrade_price"""
        if self.is_upgradable():
            self.money -= self.upgrade_price
            self.health += self.health_next_rise
            self.level += 1
            self.health_next_rise += 10
            self.upgrade_price += 5
            print("The health successfully upgraded")
        else:
            print("Not enough money")
            print(f"{self.upgrade_price} $ is needed for upgrade. You have {self.money} $")

    def upgrade_armor(self):
        """Upgrades armor if enough money and increases upgrade_price"""
        if self.is_upgradable():
            self.money -= self.upgrade_price
            self.armor += self.armor_next_rise
            self.level += 1
            self.armor_next_rise += 1
            self.upgrade_price += 5
            print("The armor successfully upgraded")
        else:
            print("Not enough money")
            print(f"{self.upgrade_price} $ is needed for upgrade. You have {self.money} $")

    def choose_a_target(self, targets):
        """From terminal takes a car name and returns target from targets"""
        target_dict = {}
        for j in targets:
            if j.name == self.name:
                continue
            target_dict[j.name] = j
        while True:
            target = input(f"Available cars to attack: {list(target_dict.keys())}\n"
                           "Enter the target cars name to attack: ")
            if target in target_dict.keys():
                return target_dict[target]
            else:
                print("Imputed wrong target name.")

    def print_current_status(*cars, all_info=False):
        """Prints current status of cars"""
        for car in cars:
            if all_info:
                print(f"{car.name}:"
                      f" level = {car.level},"
                      f" health = {car.health},"
                      f" armor = {car.armor},"
                      f" money = {car.money} $,"
                      f" damage = {car.damage} ± 2,"
                      f" next upgrade price = {car.upgrade_price} $,"
                      f" health next rise = {car.health_next_rise},"
                      f" damage next rise = {car.damage_next_rise},"
                      f" armor next rise = {car.armor_next_rise}.")
            else:
                print(f"{car.name}:"
                      f" health = {car.health},"
                      f" armor = {car.armor},"
                      f" money = {car.money} $,"
                      f" damage = {car.damage} ± 2.")

    def action(self, *target_cars):
        """
        Takes action command from terminal and do action for given car.
        As second argument takes target_cars_list to attack.
        """
        while True:
            move = input("Please input a command : ")
            if move == "uh":
                self.upgrade_health()
            elif move == "ud":
                self.upgrade_damage()
            elif move == "ua":
                self.upgrade_armor()
            elif move == "i":
                self.print_current_status()
            elif move == "ai":
                Vehicle.print_current_status(*target_cars, all_info=True)
            elif move == "a":
                self.attack(self.choose_a_target(target_cars))
                break
            elif move == "h":
                print("Action commands help:"
                      "\n\"uh\": upgrade the health,"
                      "\n\"ud\": upgrade the damage,"
                      "\n\"ua\": upgrade the armor,"
                      "\n\"a\": attack,"
                      "\n\"i\": display the current car info,"
                      "\n\"ai\": display all cars info,"
                      "\n\"h\": display this command")
            else:
                print(f"Imputed wrong command: {move}.\n(Enter \"h\" for help.)")


class Bmw(Vehicle):
    """A child from class Vehicle with separate default parameters"""

    def __init__(self, name="BMW", health=100, damage=20):
        super().__init__(name, health, damage)
    # def __repr__(self):
    #     return "bmw"


class Mercedes(Vehicle):
    """A child from class Vehicle with separate default parameters"""

    def __init__(self, name="Mercedes", health=110, damage=15):
        super().__init__(name, health, damage)


class Opel(Vehicle):
    """A child from class Vehicle with separate default parameters"""

    def __init__(self, name="Mercedes", health=100, damage=15, money=5, upgrade_price=10):
        super().__init__(name, health, damage, money, upgrade_price)


def draw_a_car(name):
    car_pic = f"""
                                <{name}>
          ,-----------------.                    ,-----------------.
         /,--------.--------.\\                  /,--------.--------.\\
        /:       '---' ,--.  :\\                ::       '---'       ::
       (.'------------'----`-',)               ||__,-=-.____________||
     ,' \\`.        $        ,'/ `.           ,( \\.        &        ,/ ).
   ,'-.--. `.------^------.' .--,-`.       ,'-.-. `,------^------.' ,-,-`.
  ((__)) |,'    ___|___    `.| ((__))     ((__))|\\/    ___|___    \\/|((__))
  |`--' _|_________|_________|_ `--'|     |`--' |_________|_________| `--'|
  | __,',--.__|____|____|__,--.`.__ |     | __,',-.__|____|____|__,-.`.__ |
  ||__`_`--'._|____|____|__`--','__||     ||__`.`-'__|____|____|__`-','__||
 (___          |Mercedes|         ___)   (___         |  BMW  |         ___)
    |````|``---'-------'---``|````|         |```|-----'-------'-----|```|
    '----'                   '----'         '---'                   '---'
    """
    print(car_pic)


def select_difficulty_level():
    """Takes difficulty level, returns 1 or 2 as int"""
    difficulty = {"1": 1, "2": 2}
    while True:
        try:
            return difficulty[input("Please select a difficulty level (1 or 2): ")]
        except KeyError:
            print("Wrong input. Please try again.")


def default_or_init():
    """Takes answer from terminal, returns True if yes(y) or False if no(n) """
    imputes_dict = {"y": True, "n": False}
    while True:
        try:
            return imputes_dict[input("Do you want to input cars yourself? (y/n): ")]
        except KeyError:
            print("Wrong input. Please try again.")


def take_cars_number_from_terminal():
    """Takes number from terminal and returns as a int"""
    while True:
        try:
            cars_number = int(input("Please input gamers number: "))
            if cars_number <= 1:
                raise ValueError
        except ValueError:
            print("Imputed char is not a number or less then 2. Please try again")
        else:
            return cars_number


def take_a_car():
    """Creates and returns an object car imputed from terminal"""
    while True:
        car_type = input("Please enter cars type (b: Bmw, m: Mercedes, o: Opel, i: info about cars): ")
        if car_type == "b":
            return Bmw(input("Please input cars name: "))
        elif car_type == "m":
            return Mercedes(input("Please input cars name: "))
        elif car_type == "o":
            return Opel(input("Please input cars name: "))
        elif car_type == "i":
            print("Bmw: health = 100, money = 0 $, damage = 20, upgrade price at the beginning = 20\n"
                  "Mercedes: health = 110, money = 0 $, damage = 15, upgrade price at the beginning = 20\n"
                  "Opel: health = 100, money = 5 $, damage = 15, upgrade price at the beginning = 10")
            continue
        print("Wrong input. Please try again.")


def init_cars():
    """Takes cars from terminal and returns as a list"""
    if default_or_init():
        cars_number = take_cars_number_from_terminal()
        cars_l = []
        for j in range(1, cars_number + 1):
            while True:
                print(f"Please select {j}-th car.")
                car = take_a_car()
                if car.name in [elem.name for elem in cars_l]:
                    print(f"warning: The name \"{car.name}\" already is used. try again.")
                else:
                    cars_l.append(car)
                    break
        return cars_l
    else:
        return [Bmw("b"), Mercedes("m"), Opel("o")]


def remove_loser(cars: list):
    """Checks if some of cars lose (health <=0). removes a loser from cars list if yes"""
    for car in cars:
        if car.health <= 0:
            print(f"{car.name} lose!!!")
            cars.remove(car)


def min_health_cars(list_of_cars: list):
    """Returns a min_health_cars list from list_of_cars"""
    min_health = list_of_cars[0].health
    for car in list_of_cars:
        if car.health < min_health:
            min_health = car.health
    min_health_cars_l = []
    for car in list_of_cars:
        if car.health == min_health:
            min_health_cars_l.append(car)
    return min_health_cars_l


# === main ===
dif_level = select_difficulty_level()
cars_list = init_cars()
enemy = Vehicle("Enemy")

print("Start the game !!!")
draw_a_car("Cars battle!!!")
print("The battle of following cars begins!!!:")
Vehicle.print_current_status(*cars_list)
a_round = 1
while len(cars_list) > 1:
    print(f"\nStart the {a_round}-th round!!!")
    for next_car in cars_list:
        print(f"\nNow is {next_car.name}'s turn")
        next_car.action(*cars_list)
    # === Enemy's turn BEGIN === #
    enemy.damage = randrange(5 + a_round, 11 + a_round)
    if dif_level == 1:
        enemy.attack(*cars_list)
    else:  # dif_level == 2
        enemy.attack(*min_health_cars(cars_list))
    # === Enemy's turn END === #
    remove_loser(cars_list)
    print(f"The {a_round}-th round is finished!!!.")
    a_round += 1
try:
    print(f"\n{cars_list[0].name} win !!!")
except IndexError:
    print("Enemy win !!!")
