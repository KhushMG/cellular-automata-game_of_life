import numpy as np
import cellpylib as cpl
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# custom implementation of game of life rule

class CustomRule(cpl.BaseRule):
  
  def __call__(self, n, c, t):
    if n[1][1] == 0:
      if np.sum(n) == 3:
        return 1
      else:
        return 0
    else:
      if np.sum(n) - 1 == 2 or np.sum(n) - 1 == 3:
        return 1
      else:
        return 0

rule = CustomRule()

cellular_automaton = cpl.init_simple2d(60,60)

# Glider
cellular_automaton[:,[28,29,30,30],[30,31,29,31]] = 1

# Blinker
cellular_automaton[:,[40,40,40],[15,16,17]] = 1

# Light Weight Space Ship
cellular_automaton[:, [18,18,19,20,21,21,21,21,20], [45,48,44,44,44,45,46,47,48]] = 1

cellular_automaton = cpl.evolve2d(
    cellular_automaton,
    timesteps=250,
    neighbourhood="Moore",
    apply_rule=rule,
    memoize="recursive",
)

fig, ax = plt.subplots()

ax.set_xlim((0,60))
ax.set_xlim((60,0))

img = ax.imshow(cellular_automaton[0], interpolation='nearest', cmap='Greys')

def init():
  img.set_data(cellular_automaton[0])
  return (img,)

def animate(i):
  img.set_data(cellular_automaton[i])
  return (img,)


anim = animation.FuncAnimation(fig, animate, init_func=init, frames=250, interval=50, blit=True, repeat=False)

plt.show()

"""
# game of life rule

cellular_automaton = cpl.init_random2d(60,60)
cellular_automaton = cpl.evolve2d(
    cellular_automaton,
    timesteps=250,
    neighbourhood='Moore',
    apply_rule=cpl.game_of_life_rule, memoize='recursive'
)

fig, ax = plt.subplots()
ax.set_xlim((0,60))
ax.set_ylim((0,60))

img = ax.imshow(cellular_automaton[0], interpolation='nearest', cmap='Greys')

def init():
  img.set_data(cellular_automaton[0])
  return (img, )


def animate(i):
    img.set_data(cellular_automaton[i])
    return (img,)


ani = animation.FuncAnimation(
    fig, animate, init_func=init, frames=250, interval=30, blit=True, repeat=False
)

plt.show()
"""
