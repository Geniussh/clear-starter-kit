![CLEAR](https://clear-benchmark.github.io/img/examples_new.png)

# [CLEAR](https://www.aicrowd.com/challenges/cvpr-2022-clear-challenge/) | Starter Kit 
[![Discord](https://img.shields.io/discord/565639094860775436.svg)](https://discord.gg/fNRrSvZkry)

This repository is the CLEAR **Submission template and Starter kit**! Clone the repository to compete now!

**This repository contains**:
*  **Documentation** on how to submit your models to the leaderboard
*  **The procedure** for best practices and information on how we evaluate your agent, etc.
*  **Starter code** for you to get started!

# Table of Contents

1. [Competition Procedure](#competition-procedure)
2. [How to access and use dataset](#how-to-access-and-use-dataset)
3. [How to start participating](#how-to-start-participating)
4. [How do I specify my software runtime / dependencies?](#how-do-i-specify-my-software-runtime-dependencies-)
5. [What should my code structure be like ?](#what-should-my-code-structure-be-like-)
6. [How to make submission](#how-to-make-submission)
7. [Important links](#-important-links)


#  Competition Procedure

[Continual LEArning on Real-World Imagery (CLEAR)](https://clear-benchmark.github.io/) is the first continual image classification benchmark dataset with a natural temporal evolution of visual concepts in the real world that spans a decade (2004-2014). This competition will be an opportunity for researchers and machine learning enthusiasts to experiment and explore state-of-the-art Continual Learning (CL) algorithms on this novel dataset. In addition, submissions will be evaluated with our novel streaming evaluation protocols that we have proposed in the [paper](https://arxiv.org/abs/2201.06289). 

The challenge consists of two stages: 
- **Stage 1**  

Participants train their models locally using the public dataset consisting of 10 public trainsets following the streaming protocol, i.e. train today and test on tomorrow. Participants upload their models (10 in total, each is a model checkpoint train consecutively on the 10 trainsets) along with their training script as one submission to AICrowd for evaluation against our private hold-out testset. Each of the 10 models will be evaluated on the 10 hold-out testsets, obtaining an 10x10 accuracy matrix. The evaluation metrics are 4 different summarization of the accuracy matrix, i.e. In-Domain Accuracy (mean of diagonal), Next-Domain Accuracy (mean of superdiagonal), Forward Transfer (mean of upper triangular entries), Backward Transfer (mean of lower triangular entries). Details about these metrics can be found in the paper. We take a weighted average of the 4 metrics when determining the rankings in  the leaderboard.

_The following is a high level description of how this process works_

![](https://i.imgur.com/xzQkwKV.jpg)

1. **Sign up** to join the competition [on the AIcrowd website](https://www.aicrowd.com/challenges/cvpr-2022-clear-challenge/).
2. **Fork** this repo and start developing your solution.
3. **Train** your models for ... and write your predictor code as described in [how to write your own predictor](#how-to-write-your-own-predictor) section.
4. [**Submit**](#how-to-submit-a-model) your trained models to [AIcrowd Gitlab](https://gitlab.aicrowd.com) for evaluation [(full instructions below)](#how-to-submit-a-model). The automated evaluation setup will evaluate the submissions against the test dataset to compute and report the metrics on the leaderboard of the competition.

- **Stage 2**  

The top 3 teams on the public leaderboard in Stage 1 will be asked to provide a dockerized environment to train their models on our own servers. We will validate each team's models submitted to the leaderboard by training their models within the specified time limit, comparing the accuracy with the baselines, as well as verifying that they did not use auxilary information to train the model (e.g., pre-trained network, additional labeled data, and etc.). Teams with invalid submissions will be removed from the leaderboard, and remaining top-3 teams with valid submissions will be eligible for the awards.

# How to write your own predictor?

We require that you place your models in `models` directory and use the interface defined in `run.py`. 

# How to start participating?

## Setup

1. **Add your SSH key** to AIcrowd GitLab

You can add your SSH Keys to your GitLab account by going to your profile settings [here](https://gitlab.aicrowd.com/profile/keys). If you do not have SSH Keys, you will first need to [generate one](https://docs.gitlab.com/ee/ssh/README.html#generating-a-new-ssh-key-pair).

2.  **Clone the repository**

    ```
    git clone git@gitlab.aicrowd.com:<your-username>/clear-starter-kit.git
    ```

3. **Install** competition specific dependencies!
    ```
    cd mnist-starter-kit
    pip install -r requirements.txt
    ```

4. Try out the random predictor by running `python local_evaluation.py`.

5. Write your own predictor as described in [how to write your own predictor](#how-to-write-your-own-predictor) section.

6. Make a submission as described in [how to make a submission](#how-to-make-a-submission) section.

## How do I specify my software runtime / dependencies ?

We accept submissions with custom runtime, so you don't need to worry about which libraries or framework to pick from.

The configuration files typically include `requirements.txt` (pypi packages), `environment.yml` (conda environment), `apt.txt` (apt packages) or even your own `Dockerfile`.

You can check detailed information about the same in the 👉 [RUNTIME.md](docs/runtime.md) file.

## What should my code structure be like ?

Please follow the example structure as it is in the starter kit for the code structure.
The different files and directories have following meaning:

```
.
├── aicrowd.json           # Submission meta information - like your username
├── apt.txt                # Packages to be installed inside docker image
├── evaluation_utils/      # Directory containing helper scripts for evaluation (DO NOT EDIT)
├── requirements.txt       # Python packages to be installed
├── local_evaluation.py    # Helper script for local evaluations
└── evaluation_setup.py    # IMPORTANT: Add your data transform and model loading functions that are consistent with your trained models
```

Finally, **you must specify an AIcrowd submission JSON in `aicrowd.json` to be scored!** 

The `aicrowd.json` of each submission should contain the following content:

```json
{
  "challenge_id": "clear-2022",
  "authors": [
    "your-aicrowd-username"
  ],
  "description": "(optional) description about your awesome agent",
  "gpu": true
}
```

This JSON is used to map your submission to the challenge - so please remember to use the correct `challenge_id` as specified above.

Also, make sure the ```gpu``` flag is true so we can speed up the evaluation. 

## How to make a submission?

We have added a quick submission utility script as part of this starter kit, to keep things simple. You can make submission as follows:

```
./submit.sh <unique-submission-name>

Example: ./submit.sh "bayes v0.1"
```

In case you don't want to use this utility script, please check out the submission guidelines [SUBMISSION.md](docs/SUBMISSION.md).


**Best of Luck** :tada: :tada:

## Contributing

🙏 You can share your solutions or any other baselines by contributing directly to this repository by opening merge request.

- Add your implementation.
- Test it out using `python local_evaluation.py`.
- Add any documentation for your approach at top of your file.
- Create merge request! 🎉🎉🎉 

## Contributors

- Shihao Shen
- Zhiqiu Lin
- Jia Shi
- Siqi Zeng

# 📎 Important links


💪 &nbsp;Challenge Page: https://www.aicrowd.com/challenges/cvpr-2022-clear-challenge

🗣️ &nbsp;Discussion Forum: https://www.aicrowd.com/challenges/cvpr-2022-clear-challenge/discussion

🏆 &nbsp;Leaderboard: https://www.aicrowd.com/challenges/cvpr-2022-clear-challenge/leaderboards
