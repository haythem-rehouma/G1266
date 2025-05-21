import gym
import numpy as np
import random
import matplotlib.pyplot as plt
from collections import deque
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
from tensorflow.keras.optimizers import Adam


# DQN Agent class
class DQNAgent:
    def __init__(self, state_size, action_size):
        self.state_size = state_size  # Size of the state space
        self.action_size = action_size  # Size of the action space
        self.memory = deque(maxlen=2000)  # Experience replay memory
        self.gamma = 0.95  # Discount factor for future rewards
        self.epsilon = 1.0  # Exploration rate
        self.epsilon_decay = 0.995  # Decay rate for exploration
        self.epsilon_min = 0.01  # Minimum exploration rate
        self.learning_rate = 0.001  # Learning rate for the optimizer
        self.model = self._build_model()  # Build the Q-network model

    def _build_model(self):
        model = Sequential()
        model.add(Dense(24, input_dim=self.state_size, activation='relu'))  # Hidden layer 1
        model.add(Dense(24, activation='relu'))  # Hidden layer 2
        model.add(Dense(self.action_size, activation='linear'))  # Output layer
        model.compile(loss='mse', optimizer=Adam(learning_rate=self.learning_rate))  # Compile the model
        return model

    def act(self, state):
        if np.random.rand() <= self.epsilon:
            return random.randrange(self.action_size)  # Explore
        return np.argmax(self.model.predict(state))  # Exploit

    def replay(self, batch_size):
        minibatch = random.sample(self.memory, batch_size)  # Sample a minibatch
        for state, action, reward, next_state, done in minibatch:
            target = reward + (self.gamma * np.max(self.model.predict(next_state)) if not done else 0)  # Calculate target
            target_f = self.model.predict(state)  # Get the current Q-values
            target_f[0][action] = target  # Update the target Q-value for the action taken
            self.model.fit(state, target_f, epochs=1, verbose=0)  # Train the model
        if self.epsilon > self.epsilon_min:
            self.epsilon *= self.epsilon_decay  # Decay the exploration rate

# Initialize the environment and the agent
env = gym.make("CartPole-v1")  # Create the CartPole environment
state_size = env.observation_space.shape[0]  # Get the size of the state space
action_size = env.action_space.n  # Get the number of actions available
agent = DQNAgent(state_size, action_size)  # Create the DQN agent

episodes = 5  # Number of episodes to train
rewards = []  # List to store rewards for each episode

# Set up real-time plotting
plt.ion()  # Turn on interactive mode for real-time plotting
fig, ax = plt.subplots()  # Create a figure and axes
line, = ax.plot([], [], 'b-', marker='o')  # Initialize the line object for plotting
ax.set_xlim(0, episodes)  # Set x-axis limits (number of episodes)
ax.set_ylim(0, 500)  # Set y-axis limits (max reward, adjust if needed)
ax.set_xlabel('Episodes')  # Label for x-axis
ax.set_ylabel('Total Reward')  # Label for y-axis
ax.set_title('Real-Time Rewards during Training')  # Title of the plot

# Training loop
for e in range(episodes):
    state = env.reset()[0]  # Reset the environment and get initial state
    state = np.reshape(state, [1, state_size])  # Reshape state for model input
    total_reward = 0  # Initialize total reward for the episode

    for _ in range(500):  # Limit to 500 steps per episode
        action = agent.act(state)  # Select action based on the current state
        next_state, reward, done, truncated, _ = env.step(action)  # Take action and observe result
        next_state = np.reshape(next_state, [1, state_size])  # Reshape next state for model input
        agent.memory.append((state, action, reward, next_state, done))  # Store experience in memory
        state = next_state  # Update current state
        total_reward += reward  # Accumulate reward
        if len(agent.memory) > 32:  # Train the agent if enough samples are available
            agent.replay(32)
        if done:  # Check if the episode is finished
            break

    rewards.append(total_reward)  # Append the total reward for the episode
    print(f"Episode {e + 1}/{episodes}, Total Reward: {total_reward}")  # Print the episode result

    # Update the plot in real-time
    line.set_xdata(range(1, e + 2))  # Update x-data (episodes)
    line.set_ydata(rewards)  # Update y-data (total rewards)
    ax.draw_artist(line)  # Draw the updated line
    fig.canvas.flush_events()  # Update the canvas to show new data

plt.ioff()  # Turn off interactive mode
plt.show()  # Show the final plot with all data

env.close()  # Close the environment
