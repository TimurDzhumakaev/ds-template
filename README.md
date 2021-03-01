# Data Science template project

This is template of Git repository for Data Science projects. You can just do:

`cookiecutter https://github.com/TimurDzhumakaev/ds-template.git`

And then initialize your repository.

Please note that you must have `cookiecutter` library installed.

## Description of folders

`_experiments` is for drafts. Files in this directory not listed in Git.

`_legacy` is for obsolete scripts in your opinion. But someone can disagree, that's why you just don't remove files and only place in this folder.

`etl` is for reproducible process of feature extraction/feature engineering. Intended for production-like code, usage of Jupyter Notebooks in this directory is discouraged.

`train` is for model training scripts.

`utils` is for commonly used functions in project.

## config.yaml

This file is intended to be used as dictionary of data source names and model hyperparameters.
