from random import randint

from graphic_arts.start_game_banner import run_screensaver

description_list = {
    'warrior': {'damage': (3, 5),
                'block': (5, 10),
                'skill': '«Выносливость 105»',
                'description': 'Воитель — отличный боец ближнего боя'},
    'mage': {'damage': (5, 10),
             'block': (-2, 10),
             'skill': '«Атака 45»',
             'description': 'Маг — превосходный укротитель стихий'},
    'healer': {'damage': (-3, -1),
               'block': (2, 5),
               'skill': '«Защита 40»',
               'description': 'Лекарь — чародей, способный исцелять раны'}}


def attack(char_name: str, char_class: str) -> str:
    """Show current damage."""
    start_num = description_list[char_class]['damage'][0]
    end_num = description_list[char_class]['damage'][1]
    damage: int = 5 + randint(start_num, end_num)
    return (f'{char_name} нанёс урон противнику равный {damage}')


def defence(char_name: str, char_class: str) -> str:
    """Show current defence."""
    start_num = description_list[char_class]['block'][0]
    end_num = description_list[char_class]['block'][1]
    block = 10 + randint(start_num, end_num)
    return (f'{char_name} блокировал {block} урона')


def special(char_name: str, char_class: str) -> str:
    """Show special skill."""
    skill = description_list[char_class]['skill']
    return (f'{char_name} применил специальное умение {skill}')


def start_training(char_name: str, char_class: str) -> str:
    """Show greeting and description choosed character."""
    description = description_list[char_class]['description']
    print(f'{char_name}, ты {description}.')
    print('Потренируйся управлять своими навыками.')
    attack: str = 'attack — чтобы атаковать противника'
    defence: str = 'defence — чтобы блокировать атаку противника'
    special: str = 'special — чтобы использовать свою суперсилу'
    print('Введи одну из команд: {attack}, {defence} или {special}.')
    print('Если не хочешь тренироваться, введи команду skip.')
    cmd: str = None
    while cmd != 'skip':
        cmd = input('Введи команду: ')
        if cmd == 'attack':
            print(attack(char_name, char_class))
        if cmd == 'defence':
            print(defence(char_name, char_class))
        if cmd == 'special':
            print(special(char_name, char_class))
    return 'Тренировка окончена.'


def choice_char_class() -> str:
    approve_choice: str = ''
    char_class: str = ''
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


if __name__ == '__main__':
    run_screensaver()
    print('Приветствую тебя, искатель приключений!')
    print('Прежде чем начать игру...')
    char_name: str = input('...назови себя: ')
    print(f'Здравствуй, {char_name}! '
          'Сейчас твоя выносливость — 80, атака — 5 и защита — 10.')
    print('Ты можешь выбрать один из трёх путей силы:')
    print('Воитель, Маг, Лекарь')
    char_class: str = choice_char_class()
    print(start_training(char_name, char_class))
