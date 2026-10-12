"""Download source datasets into the repository root; leave existing files alone."""

import argparse
import io
import shutil
import urllib.request
import zipfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SOURCES = {
    'movielens': ('https://files.grouplens.org/datasets/movielens/ml-latest-small.zip',
                 ['ml-latest-small/' + name for name in
                  ('ratings.csv', 'movies.csv', 'links.csv', 'tags.csv', 'README.txt')]),
    'retail': ('https://archive.ics.uci.edu/static/public/352/online+retail.zip',
               ['Online Retail.xlsx']),
}


def download(dataset):
    url, members = SOURCES[dataset]
    missing = [name for name in members if not (ROOT / name).is_file()]
    if not missing:
        print(f'{dataset}: required files already exist; skipping.')
        return
    request = urllib.request.Request(url, headers={'User-Agent': 'ML-Projects-dataset-setup'})
    with urllib.request.urlopen(request, timeout=120) as response:
        archive_bytes = response.read()
    with zipfile.ZipFile(io.BytesIO(archive_bytes)) as archive:
        for name in missing:
            destination = ROOT / name
            destination.parent.mkdir(parents=True, exist_ok=True)
            # Extract only expected members, avoiding arbitrary paths from the archive.
            temporary = destination.with_name(destination.name + '.partial')
            try:
                with archive.open(name) as source, temporary.open('wb') as output:
                    shutil.copyfileobj(source, output)
                temporary.replace(destination)
            finally:
                temporary.unlink(missing_ok=True)
            print(f'Created {destination.relative_to(ROOT)}')


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('dataset', choices=['movielens', 'retail', 'all'])
    args = parser.parse_args()
    try:
        for dataset in SOURCES if args.dataset == 'all' else [args.dataset]:
            download(dataset)
    except (OSError, ValueError, KeyError, zipfile.BadZipFile) as error:
        parser.exit(1, f'Dataset download failed: {error}\nSee DATASETS.md for manual download links.\n')


if __name__ == '__main__':
    main()
