# Import dependencies
import matplotlib.pyplot as plt
from IPython import display
from strategies import *
from statistics import mean


# Initialize parameters
plt.ion()       # Matplotlib interactive mode for plotting
plt.rcParams.update({'font.size': 8})
payoff_matrix = np.array([[3, 0], [5, 1]])  # [Cooperate, Defect]


# Define the environment (Prisoner's Dilemma)
class PrisonersDilemmaEnv:
    def __init__(self):
        self.num_actions = 2  # Cooperate or Defect
        self.num_states = 4   # State corresponding to each pair of choice

    def step(self, action1, action2):
        # Payoff matrix for the Prisoner's Dilemma game
        return payoff_matrix[action1, action2], payoff_matrix[action2, action1]


# Main training loop
def prisoner_dilemma(num_episodes, num_rounds, strategy_player1, strategy_player2):

    # Create the environments and agents
    env = PrisonersDilemmaEnv()
    agent1 = QLearningAgent(env.num_states, env.num_actions)
    agent2 = QLearningAgent(env.num_states, env.num_actions)

    # Lists to store total rewards for plotting
    total_rewards1 = []
    total_rewards2 = []
    cooperation_rate1 = []
    cooperation_rate2 = []
    action_history['player_1'] = []
    action_history['player_2'] = []
    reward_history['player_1'] = []
    reward_history['player_2'] = []

    # Training loop
    for episode in range(num_episodes):
        
        # Break early out of training
        if plt.waitforbuttonpress(timeout=0.01):
            return

        state = np.random.randint(env.num_states)  # Initial state is randomly chosen

        # Initialize rewards and cooperation rate for each episode
        total_reward1 = 0
        total_reward2 = 0
        num_cooperate1 = 0
        num_cooperate2 = 0
        
        for round in range(num_rounds):
            
            # Agents choose actions
            action1 = strategy_player1(agent1, state, round, '2')
            action2 = strategy_player2(agent2, state, round, '1')

            # Update cooperation rates
            if action1 == 0:
                num_cooperate1 += 1
            if action2 == 0:
                num_cooperate2 += 1
            
            # Agents take actions in the environment and receive rewards
            reward1, reward2 = env.step(action1, action2)
            total_reward1 += reward1
            total_reward2 += reward2

            # Update action and reward memory
            action_history["player_1"].append(action1)
            action_history["player_2"].append(action2)
            reward_history["player_1"].append(reward1)
            reward_history["player_2"].append(reward2)

            # Agents update Q-values
            next_state = 2 * action1 + 1 * action2  # Next state is based on the current action set
            agent1.update_q_values(state, action1, reward1, next_state, reward1+reward2, payoff_matrix[0, 0]*2)
            agent2.update_q_values(state, action2, reward2, next_state, reward1+reward2, payoff_matrix[0, 0]*2)

            # Change state
            state = next_state

        # Update the lists for plotting
        total_rewards1.append(total_reward1)
        total_rewards2.append(total_reward2)
        cooperation_rate1.append(num_cooperate1)
        cooperation_rate2.append(num_cooperate2)
        
        # Print episode summary
        print(f"Episode {episode + 1} ended with total reward for Player 1: {total_reward1}, Player 2: {total_reward2}")

        # Plot total rewards over episodes
        display.clear_output(wait=True)
        display.display(plt.gcf())
        plt.clf()
        plt.plot(total_rewards1, label=f'{strategy_player1.__name__} reward', color='red')
        plt.plot(total_rewards2, label=f'{strategy_player2.__name__} reward', color='blue')
        plt.plot(cooperation_rate1, label=f'{strategy_player1.__name__} cooperation rate', linestyle = 'dashed', color='red')
        plt.plot(cooperation_rate2, label=f'{strategy_player2.__name__} cooperation rate', linestyle = 'dashed', color='blue')
        plt.xlabel('Episodes')
        plt.ylabel('Total Reward')
        plt.title('Total Reward over Episodes')
        plt.legend()
        plt.tight_layout()
        plt.show(block = False)
        plt.savefig('plot.png', dpi = 200)


if __name__ == '__main__':
    try:
        num_episodes = 100
        num_rounds_per_episode = 100

        # Call the training loop
        prisoner_dilemma(num_episodes, num_rounds_per_episode, ql_strategy, tit_for_tat_strategy)

        plt.ioff()  # Turn off interactive mode
    
    except KeyboardInterrupt:
        pass