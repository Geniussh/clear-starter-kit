// todo: replace banner

![MNIST]()

# [MNIST](https://www.aicrowd.com/challenges/mnist/) | Starter Kit 
[![Discord](https://img.shields.io/discord/565639094860775436.svg)](https://discord.gg/fNRrSvZkry)

This repository is the MNIST **Submission template and Starter kit**! Clone the repository to compete now!

**This repository contains**:
*  **Documentation** on how to submit your models to the leaderboard
*  **The procedure** for best practices and information on how we evaluate your agent, etc.
*  **Starter code** for you to get started!

//todo: Add starter notebook

> **NOTE:** 
If you are resource-constrained or would not like to setup everything in your system, you can make your submission from inside Google Colab too. [**Check out the beta version of the Notebook.**](https://colab.research.google.com/drive/14FpktUXysnjIL165hU3rTUKPHo4-YRPh?usp=sharing)



# Table of Contents

1. [Competition Procedure](#competition-procedure)
2. [How to access and use dataset](#how-to-access-and-use-dataset)
3. [How to start participating](#how-to-start-participating)
4. [How do I specify my software runtime / dependencies?](#how-do-i-specify-my-software-runtime-dependencies-)
5. [What should my code structure be like ?](#what-should-my-code-structure-be-like-)
6. [How to make submission](#how-to-make-submission)
7. [Important links](#-important-links)


#  Competition Procedure

The MNIST Challenge is an opportunity for researchers and machine learning enthusiasts to test their skills by creating a system able to ...

In this challenge, you will train your models locally and then upload them to AIcrowd (via git) to be evaluated. 

**The following is a high level description of how this process works**

// todo: replace image with competition specific one

![](https://i.imgur.com/xzQkwKV.jpg)

1. **Sign up** to join the competition [on the AIcrowd website](https://www.aicrowd.com/challenges/mnist/).
2. **Fork** this repo and start developing your solution.
3. **Train** your models for ... and write your predictor code as described in [how to write your own predictor](#how-to-write-your-own-predictor) section.
4. [**Submit**](#how-to-submit-a-model) your trained models to [AIcrowd Gitlab](https://gitlab.aicrowd.com) for evaluation [(full instructions below)](#how-to-submit-a-model). The automated evaluation setup will evaluate the submissions against the test dataset to compute and report the metrics on the leaderboard of the competition.

# How to write your own predictor?

We recommend that you place your models in `models` directory (though it is not mandatory) and use the interface defined in `run.py`. 

# How to start participating?

## Using this repository

This repository contains a submission template.

```bash
# Clone the repository
git clone https://gitlab.aicrowd.com/aicrowd/mnist-starter-kit.git
cd mnist-starter-kit

# Install dependencies
pip install -r requirements.txt

# Run codebase locally
python rollout.py
```

todo: some description of what the script does


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
└── run.py                 # IMPORTANT: Add your own predictor
```

Finally, **you must specify an AIcrowd submission JSON in `aicrowd.json` to be scored!** 

The `aicrowd.json` of each submission should contain the following content:

```json
{
  "challenge_id": "mnist",
  "authors": [
    "your-aicrowd-username"
  ],
  "description": "(optional) description about your awesome agent"
}
```

This JSON is used to map your submission to the challenge - so please remember to use the correct `challenge_id` as specified above.

## How to make a submission?

We have added a quick submission utility script as part of this starter kit, to keep things simple. You can make submission as follows:

```
./submit.sh <unique-submission-name>

Example: ./submit.sh "bayes v0.1"
```

In case you don't want to use this utility script, please check out the submission guidelines [submission.md](docs/submission.md).


**Best of Luck** :tada: :tada:

## Contributing

🙏 You can share your solutions or any other baselines by contributing directly to this repository by opening merge request.

- Add your implementation.
- Test it out using `python local_evaluation.py`.
- Add any documentation for your approach at top of your file.
- Create merge request! 🎉🎉🎉 

## Contributors

// todo

# 📎 Important links


💪 &nbsp;Challenge Page: https://www.aicrowd.com/challenges/mnist

🗣️ &nbsp;Discussion Forum: https://www.aicrowd.com/challenges/mnist/discussion

🏆 &nbsp;Leaderboard: https://www.aicrowd.com/challenges/mnist/leaderboards
