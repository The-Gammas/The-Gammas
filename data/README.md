# Data — local only

This directory documents where local data live; its contents are ignored by Git.

The current notebooks use the NMA-curated HCP task-fMRI subset with behavioural data. Follow the
official [NMA loader notebook](https://colab.research.google.com/github/NeuromatchAcademy/course-content/blob/main/projects/fMRI/load_hcp_task_with_behaviour.ipynb) and accept the
[HCP Data Use Terms](https://www.humanconnectome.org/study/hcp-young-adult/document/wu-minn-hcp-consortium-open-access-data-use-terms)
before using the dataset.

Jaime's data-preparation notebooks use this default location:

```text
data/
└── hcp_task/
    ├── regions.npy
    ├── subjects_list.txt
    └── subjects/
```

Set the `GAMMAS_DATA_DIR` environment variable if your data live elsewhere. Raw data, per-subject
behaviour, splits and other derived subject-level files must not be added to the public repository.

