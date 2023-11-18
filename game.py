import pgzrun
from thing import *

WIDTH = 1000
HEIGHT = 600

idle_anim = [
    'zombie/idle/tile000',
    'zombie/idle/tile001',
]
run_anim = [
    'zombie/run/tile002',
    'zombie/run/tile003',
    'zombie/run/tile004',
    'zombie/run/tile005',
]
jump_anim = [
    'zombie/jump/tile006',
    'zombie/jump/tile007',
    'zombie/jump/tile008',
    'zombie/jump/tile009',
    'zombie/jump/tile010',
    'zombie/jump/tile011',
    'zombie/jump/tile012',
    'zombie/jump/tile013',
]
death_anim = [
    'zombie/death/tile014',
    'zombie/death/tile015',
    'zombie/death/tile016',
    'zombie/death/tile017',
    'zombie/death/tile018',
    'zombie/death/tile019',
    'zombie/death/tile020',
    'zombie/death/tile021',
]

zombie = Actor(run_anim[0])
zombie.images = run_anim
zombie.scale = 6
zombie.right = WIDTH
zombie.bottom = HEIGHT - 50
zombie.fps = 6


atk1 = [
    'mage/atk1/tile000',
    'mage/atk1/tile001',
    'mage/atk1/tile002',
    'mage/atk1/tile003',
    'mage/atk1/tile004',
    'mage/atk1/tile005',
    'mage/atk1/tile006',
    'mage/atk1/tile007',

]
atk2 = [
    'mage/atk2/tile000',
    'mage/atk2/tile001',
    'mage/atk2/tile002',
    'mage/atk2/tile003',
    'mage/atk2/tile004',
    'mage/atk2/tile005',
    'mage/atk2/tile006',
    'mage/atk2/tile007'
] 
idle = [
    'mage/idle/tile000',
    'mage/idle/tile001',
    'mage/idle/tile002',
    'mage/idle/tile003',
    'mage/idle/tile004',
    'mage/idle/tile005'

]
death = [
    'mage/death/tile000',
    'mage/death/tile001',
    'mage/death/tile002',
    'mage/death/tile003',
    'mage/death/tile004',
    'mage/death/tile005',
    'mage/death/tile006'
]
mage = Actor(idle[0])
mage.images = idle
mage.scale = 2
mage.bottom = HEIGHT + 50
mage.fps = 10
mage.hp = 5

question = 'type to atak'
typed = ''





def update():
    if mage.hp > 0:
        global typed
        zombie.animate()
        mage.animate()
        zombie.move_back(2)

        if zombie.collide_pixel(mage):
            zombie.left = WIDTH
            mage.hp -= 1
            typed = ''
              
        else:
            zombie.move_back(1)
    else:
        mage.images = death
        mage.animate()





def on_key_down(key):
    if mage.hp > 0:
        global typed
        print(key)
        if key in range(97, 122+1):
            print(chr(key))
            typed += chr(key)
        if key == 32:
            print('SPACE')
            typed+=' '
        if key == keys.BACKSPACE:
            print('DEL')
            typed = typed[0:-1]

        if typed == question:
            zombie.left = WIDTH
            typed = ''




def draw():
    screen.clear()
    screen.draw.text(f'HP: {mage.hp}', (10,10),fontsize=50)
    screen.draw.text(question, (WIDTH/3,HEIGHT/10), fontsize=60)
    screen.draw.text(typed, (WIDTH/3,HEIGHT/10),color='orange', fontsize=60)
    zombie.draw()
    mage.draw()
    if mage.hp <= 0:
        screen.draw.text(f'You Lose',(WIDTH/2-80, HEIGHT/2), fontsize=80)














pgzrun.go()