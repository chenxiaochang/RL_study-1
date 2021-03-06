from stable_baselines import DQN
from stable_baselines.gail import generate_expert_traj
import gym
import highway_env

model = DQN('MlpPolicy', 'overtaking-v0', verbose=1)
      # Train a DQN agent for 1e5 timesteps and generate 10 trajectories
      # data will be saved in a numpy archive named `expert_cartpole.npz`
generate_expert_traj(model, 'expert_overtaking', n_timesteps=int(1e5), n_episodes=10)