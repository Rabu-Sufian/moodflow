# 🧠 MoodFlow: Emotion Classification with MLOps

**MoodFlow** is a simple but powerful MLOps project focused on classifying emotions in text (e.g., tweets). It is designed to explore the full machine learning workflow using:

- ✅ [DVC](https://dvc.org/) for data and model version control  
- ✅ [MLflow](https://mlflow.org/) for experiment tracking  
- ✅ [Apache Airflow](https://airflow.apache.org/) for pipeline orchestration (coming soon)

---

## 📁 Project Structure

```bash
moodflow/
├── data/
│   ├── simple/         # Dataset 1: split into train/test/validation
│   └── rich/           # Dataset 2: richer version, with additional label
├── models/             # Model artifacts (to be tracked with DVC)
├── .dvc/               # DVC metadata
├── .gitignore
├── .dvcignore
└── README.md
