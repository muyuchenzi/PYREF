# Q learning的
import numpy as np
import pandas as pd
import time

# https://www.bilibili.com/video/BV13W411Y75P?p=6
# 完全不懂这个在搞什么。
np.random.seed(2)
N_STATES = 6
ACTION = ['left', 'right']
EPSILON = 0.9
ALPHA = 0.1
LAMBDA = 0.9
MAX_EPISODES = 13
FRESH_TIME = 0.01


def build_q_table(n_states, action):
    table = pd.DataFrame(
        np.zeros((n_states, len(action))),
        columns=action
    )
    # print(table)
    return table


def chose_action(state, q_table):
    state_action = q_table.iloc[state, :]
    if (np.random.uniform() > EPSILON) or (state_action.all() == 0):
        action_name = np.random.choice(ACTION)
    else:
        action_name = state_action.argmax()
    return action_name


def get_env_feedback(S, A):
    if A == 'right':
        if S == N_STATES - 2:
            S_ = "terminal"
            R = 1
        else:
            S_ = S + 1
            R = 0
    else:
        R = 0
        if S == 0:
            S_ = S
        else:
            S_ = S - 1
    return S_, R


def update_env(S, episode, step_counter):
    env_list = ['-'] * (N_STATES - 1) + ['T']
    if S == "terminal":
        interacton = f"Episode:{episode + 1} total_step={step_counter}"
        print(interacton, end='')
        time.sleep(2)
        print('\r                              ', end='')
    else:
        env_list[S] = 'o'
        interacton = ''.join(env_list)
        print(f'\r{interacton}')
        time.sleep(FRESH_TIME)


def rl():
    q_table = build_q_table(N_STATES, ACTION)
    for episode in range(MAX_EPISODES):
        step_counter = 0
        S = 0
        is_terminal = False
        update_env(S, episode, step_counter)
        while not is_terminal:
            A = chose_action(S, q_table)
            S_, R = get_env_feedback(S, A)
            q_predict = q_table.loc[S, A]
            if S_ != 'terminal':
                q_target = R + LAMBDA * q_table.loc[S_, :].max()
            else:
                q_target = R
                is_terminal = True
        q_table.iloc[S, A] += ALPHA * (q_target - q_predict)
        S = S_
        update_env(S, episode, step_counter + 1)
        step_counter += 1
    return q_table


if __name__ == '__main__':
    q_tabel = rl()
    print(r'\r\nQ-table:\n')
    print(q_tabel)
