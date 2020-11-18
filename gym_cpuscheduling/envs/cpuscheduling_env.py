import gym
from gym import error, spaces, utils
import numpy as np


class CPUSchedulingEnv(gym.Env):
    def __init__(self, n_cores=10, rand_seed=None):
        # Set random seed
        if rand_seed: np.random.seed(rand_seed)
        
        # Env constants
        self.N_CORES = n_cores
        self.DURATIONS = [1, 2, 4, 8]
        self.PRIORITIES = [1, 2, 4, 8]

        # Gym
        self.action_space = spaces.Discrete(2)  # Accept or reject
        self.observation_space = spaces.Discrete(2)

    def step(self, action):
        # Parse action
        # reject = 0
        # accept = 1
        accept = bool(action)

        # Decrease 1 unit of duration in each core
        for core in range(self.N_CORES):
            if self.cores[core] > 0:
                self.cores[core] -= 1

        # Accept (only if a core is available)
        if accept and 0 in self.cores:
            # Compute reward
            reward = self.curr_priority
            # Assign process to a CPU core
            for core in range(self.N_CORES):
                if self.cores[core] == 0:
                    self.cores[core] = self.curr_duration
        else: # Reject
            reward = 0

        # Get next priority and duration
        self.curr_priority = np.random.choice(self.PRIORITIES)
        self.curr_duration = np.random.choice(self.DURATIONS)

        state = np.concatenate((self.cores, self.curr_priority, self.curr_duration))
        return state, reward, False, {}

    def reset(self):
        self.cores = np.zeros(self.N_CORES)
        self.curr_priority = np.random.choice(self.PRIORITIES)
        self.curr_duration = np.random.choice(self.DURATIONS)
        state = np.concatenate((self.cores, self.curr_priority, self.curr_duration))
        return state

    def render(self):
        pass

    def close(self):
        pass
