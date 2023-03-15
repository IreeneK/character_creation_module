from random import randint


def attack(char_name, char_class):
    def damage(x, y):
        return (5+randint(x, y))
    if char_class == 'warrior':
        return (f'{char_name} нанёс урон противнику равный {damage(3, 5)}')
    if char_class == 'mage':
        return (f'{char_name} нанёс урон противнику равный {damage(5, 10)}')
    if char_class == 'healer':
        return (f'{char_name} нанёс урон противнику равный {damage(-3, -1)}')


def defence(char_name, char_class):
    def block(x, y):
        return (10 + randint(x, y))
    if char_class == 'warrior':
        return (f'{char_name} блокировал {block(5, 10)} урона')
    if char_class == 'mage':
        return (f'{char_name} блокировал {block(-2, 2)} урона')
    if char_class == 'healer':
        return (f'{char_name} блокировал {block(2, 5)} урона')


def special(char_name, char_class):
    def skill(char_class):
        if char_class == 'warrior':
            return (f'«Выносливость {80 + 25}»')
        if char_class == 'mage':
            return (f'«Атака {5 + 40}»')
        if char_class == 'healer':
            return (f'«Защита {10 + 30}»')
    return (f'{char_name} применил специальное умение {skill(char_class)}')


def start_training(char_name, char_class):
    if char_class == 'warrior':
        print(f'{char_name}, ты Воитель — отличный боец ближнего боя.')
    if char_class == 'mage':
        print(f'{char_name}, ты Маг — превосходный укротитель стихий.')
    if char_class == 'healer':
        print(f'{char_name}, ты Лекарь — чародей, способный исцелять раны.')
    print('Потренируйся управлять своими навыками.')
    attack = 'attack — чтобы атаковать противника'
    defence = 'defence — чтобы блокировать атаку противника'
    special = 'special — чтобы использовать свою суперсилу'
    print('Введи одну из команд: {attack}, {defence} или {special}.')
    print('Если не хочешь тренироваться, введи команду skip.')
    cmd = None
    while cmd != 'skip':
        cmd = input('Введи команду: ')
        if cmd == 'attack':
            print(attack(char_name, char_class))
        if cmd == 'defence':
            print(defence(char_name, char_class))
        if cmd == 'special':
            print(special(char_name, char_class))
    return 'Тренировка окончена.'


def choice_char_class():
    approve_choice = None
    char_class = None
    while approve_choice != 'y':
        char_class = input('Введи название персонажа, '
                           'за которого хочешь играть: Воитель — warrior, '
                           'Маг — mage, Лекарь — healer: ')
        if char_class == 'warrior':
            print('Воитель — дерзкий воин ближнего боя. '
                  'Сильный, выносливый и отважный.')
        if char_class == 'mage':
            print('Маг — находчивый воин дальнего боя. '
                  'Обладает высоким интеллектом.')
        if char_class == 'healer':
            print('Лекарь — могущественный заклинатель. '
                  'Черпает силы из природы, веры и духов.')
        approve_choice = input('Нажми (Y), чтобы '
                               'подтвердить выбор, или любую другую кнопку, '
                               'чтобы выбрать другого персонажа ').lower()
    return char_class


def main():
    print('Приветствую тебя, искатель приключений!')
    print('Прежде чем начать игру...')
    char_name = input('...назови себя: ')
    print(f'Здравствуй, {char_name}! '
          'Сейчас твоя выносливость — 80, атака — 5 и защита — 10.')
    print('Ты можешь выбрать один из трёх путей силы:')
    print('Воитель, Маг, Лекарь')
    char_class = choice_char_class()
    print(start_training(char_name, char_class))


main()
