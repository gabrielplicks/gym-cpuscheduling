from gym.envs.registration import register


register(
    id='CPUScheduling-v0',
    entry_point='gym_cpuscheduling.envs:CPUSchedulingEnv'
)
