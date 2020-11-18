import gym
from gym import error, spaces, utils
import numpy as np


class CPUSchedulingEnv(gym.Env):
    def __init__(self, rand_seed=None):
        # Set random seed
        if rand_seed: np.random.seed(rand_seed)
        pass

    def step(self, action):
        pass

    def reset(self):
        pass

    def render(self):
        pass

    def close(self):
        pass
