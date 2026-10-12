# Dataset setup and attribution

Run notebooks from the repository root. Downloaded data is ignored by Git.

## Credit Card Fraud Detection

- Source: [MLG/ULB on Kaggle](https://www.kaggle.com/datasets/mlg-ulb/creditcardfraud).
- Download and extract `creditcard.csv` into the repository root; Kaggle may require signing in.
- The local notebook records 284,807 rows, 31 columns, and 492 fraud cases. The `Class` column is the label; the remaining columns are input features.
- Use the provider's dataset description and usage conditions. The approximately 151 MB CSV is not bundled.

## MovieLens small

```sh
python scripts/download_datasets.py movielens
```

This creates `ml-latest-small/` with `ratings.csv`, `movies.csv`, `links.csv`, `tags.csv`, and the provider's `README.txt`. The notebook also includes its own download cell.

Source: [GroupLens MovieLens latest datasets](https://grouplens.org/datasets/movielens/latest/). The local notebook records 100,836 ratings from 610 users over 9,724 rated movies; the provider's movies table contains additional unrated entries. Latest datasets can change over time.

MovieLens has its own usage conditions, including acknowledgment and restrictions on commercial use; read the downloaded README. Citation: F. Maxwell Harper and Joseph A. Konstan (2015), *The MovieLens Datasets: History and Context*, ACM TiiS 5(4), Article 19. https://doi.org/10.1145/2827872.

## Online Retail

```sh
python scripts/download_datasets.py retail
```

This places `Online Retail.xlsx` in the repository root.

Source: [UCI Online Retail](https://archive.ics.uci.edu/dataset/352/online+retail), 541,909 transaction records. Citation: Chen, D. (2015), *Online Retail* [Dataset], UCI Machine Learning Repository. https://doi.org/10.24432/C5BW33. The provider lists a CC BY 4.0 license.

## CartPole

No dataset download is needed. Install `requirements-rl.txt`; experience is collected from the `CartPole-v1` Gymnasium environment during training.
