# Created by yingwen at 2019-03-13
import gym
import numpy as np


class DummyBoxEnv:
    """A dummy box environment."""

    def __init__(self, random=True):
        super().__init__(random)

    @property
    def observation_space(self):
        """Return an observation space."""
        return gym.spaces.Box(low=-1, high=1, shape=(1, ), dtype=np.float32)

    @property
    def action_space(self):
        """Return an action space."""
        return gym.spaces.Box(
            low=-5.0, high=5.0, shape=(1, ), dtype=np.float32)

    def reset(self):
        """Reset the environment."""
        return np.zeros(1, dtype=np.float32)

    def step(self, action):
        """Step the environment."""
        return self.observation_space.sample(), 0, True, dict()
