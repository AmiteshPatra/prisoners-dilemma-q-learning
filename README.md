# Prisoner's Dilemma Agent with Q-learning

## Overview

This repository contains an implementation of a Q-learning-based agent for playing the classic Prisoner's Dilemma game. The agent learns optimal strategies through interactions with various opponent strategies, aiming to maximize long-term rewards.

## Features

- **Q-Learning Algorithm**: Utilizes the Q-learning algorithm to learn optimal strategies over successive interactions.
- **Multiple Opponent Strategies**: Allows the agent to play against different opponent strategies, including "always defect," "always cooperate," and "tit-for-tat."
- **Evaluation Metrics**: Provides evaluation metrics such as cooperation rates and total rewards for analyzing the agent's performance.

## Installation

The project code can be run two ways:

### Using the pre-made evironment
1. Clone this repository to your local machine.
2. Change directory to `cd prisoners-dilemma-q-learning`.
2. Activate the qlpd environment `.\qlpd\Scripts\activate.bat`
3. Run the `game.py` script to train and evaluate the Q-learning agent.

### By installing dependencies
1. Clone this repository to your local machine.
2. Install the required dependencies using `pip install -r requirements.txt`.
3. Run the `game.py` script to train and evaluate the Q-learning agent.

## Usage

```python
python game.py
```

## Results

The agent's performance against different opponent strategies is evaluated, showcasing its ability to adapt and learn optimal strategies over time.

## License

Permission is hereby granted, free of charge, to any person obtaining a copy of this research work and associated documentation files, to deal in the Research Work without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Research Work, and to permit persons to whom the Research Work is furnished to do so.

## Acknowledgments

- This project was inspired by the work of researchers in reinforcement learning and game theory.
- Special thanks to Axelrod for his contributions to the field.

---