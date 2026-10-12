# ML Projects

Four hands-on machine learning projects by Navya Barnwal, exploring anomaly detection, recommendation systems, customer segmentation, and reinforcement learning. The notebooks emphasize building the underlying algorithms and inspecting their behavior through metrics and plots.

## Projects

| Project | Notebook | Main ideas | Project notes |
| --- | --- | --- | --- |
| Credit card fraud detection | [Anomaly_Detection.ipynb](Anomaly_Detection.ipynb) | Gaussian density estimation, imbalanced data, precision/recall, threshold selection | [README](docs/anomaly-detection.md) |
| Movie recommendations | [Collaborative_Filtering.ipynb](Collaborative_Filtering.ipynb) | Matrix factorization, regularization, gradient descent, genre similarity | [README](docs/movie-recommendations.md) |
| Customer segmentation | [Kmeans.ipynb](Kmeans.ipynb) | RFM features, standardization, K-means from scratch, elbow method | [README](docs/customer-segmentation.md) |
| CartPole reinforcement learning | [Reinforcement_learning.ipynb](Reinforcement_learning.ipynb) | DQN, experience replay, target networks, epsilon-greedy exploration | [README](docs/cartpole-dqn.md) |

## Getting started

Clone this repository and run commands from its root directory:

```sh
git clone https://github.com/Naviie-7/ML-Projects.git
cd ML-Projects
python -m venv .venv
```

Activate the environment with `.venv\Scripts\Activate.ps1` in Windows PowerShell, or `source .venv/bin/activate` on macOS/Linux. Then install the dependencies:

```sh
python -m pip install -r requirements.txt
```

For CartPole, install the additional dependencies instead:

```sh
python -m pip install -r requirements-rl.txt
```

Prepare data as described in [DATASETS.md](DATASETS.md), then launch:

```sh
python -m jupyterlab
```

Open a notebook, select the environment's Python kernel, restart the kernel, and run all cells in order. Keep the working directory at the repository root so the relative dataset paths resolve. Dependencies are unpinned; this is a setup manifest rather than an exact environment lockfile.

## Data and results

Raw datasets and ZIP archives are excluded from Git. `scripts/download_datasets.py` downloads MovieLens or Online Retail from their original providers; `creditcard.csv` must be downloaded separately from Kaggle. CartPole requires no external dataset.

The notebooks retain saved charts and substantive outputs from the original local experiments. These are historical examples, not newly verified benchmarks. Training is not fully seeded, and saved outputs may reflect earlier exploratory executions; fresh runs can differ. See the individual project notes for evaluation limits and possible next steps.

## Repository contents

```text
ML-Projects/
  Anomaly_Detection.ipynb
  Collaborative_Filtering.ipynb
  Kmeans.ipynb
  Reinforcement_learning.ipynb
  README.md
  DATASETS.md
  requirements.txt
  requirements-rl.txt
  docs/                       # Project READMEs and saved figures
  scripts/download_datasets.py
```

## Acknowledgments

Data comes from [ULB's Credit Card Fraud Detection dataset on Kaggle](https://www.kaggle.com/datasets/mlg-ulb/creditcardfraud), [GroupLens MovieLens](https://grouplens.org/datasets/movielens/latest/), and [UCI Online Retail](https://archive.ics.uci.edu/dataset/352/online+retail). The CartPole environment is provided by [Gymnasium](https://gymnasium.farama.org/environments/classic_control/cart_pole/).

Dataset usage conditions remain those of their providers. No repository-wide software license has been selected.
