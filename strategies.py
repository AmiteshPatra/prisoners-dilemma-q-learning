# Import dependencies
import numpy as np
import keyboard


# Define the storage lists
action_history = {
    "player_1": [],
    "player_2": []
}
reward_history = {
    "player_1": [],
    "player_2": []
}


# Define the Q-learning agent
class QLearningAgent:
    def __init__(self, num_states, num_actions, lr=0.1, gamma=0.9, epsilon=0.1):
        self.num_actions = num_actions
        self.lr = lr  # Learning rate
        self.gamma = gamma  # Discount factor
        self.epsilon = epsilon  # Exploration-exploitation trade-off parameter
        self.q_values = np.zeros((num_states, num_actions))  # Q-values table

    def choose_action(self, state):
        if np.random.rand() < self.epsilon:
            return np.random.randint(self.num_actions)  # Explore randomly
        else:
            return np.argmax(self.q_values[state])  # Exploit learned values

    def update_q_values(self, state, action, reward, next_state, global_reward, max_reward):
        # Q-learning update rule
        self.q_values[state, action] += self.lr * (reward + self.gamma * np.max(self.q_values[next_state]) - self.q_values[state, action])


# Q-learning strategy
def ql_strategy(agent, state, round, opponent):
    return agent.choose_action(state)

# Always defect strategy
def always_defect_strategy(agent, state, round, opponent):
    return 1

# Always cooperate strategy
def always_cooperate_strategy(agent, state, round, opponent):
    return 0

# Tit-for-tat strategy
def tit_for_tat_strategy(agent, state, round, opponent):
    try:
        return action_history[f"player_{opponent}"][-1]
    except:
        return 0

# Human strategy (press 'h+c' key to cooperate, 'h+d' key to defect)
def human_strategy(agent, state, round, opponent):
    keyboard.wait('h')
    while True:
        if keyboard.is_pressed('c'):
            return 0
        elif keyboard.is_pressed('d'):
            return 1