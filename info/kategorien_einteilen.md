import os
from pathlib import Path
from sentence_transformers import SentenceTransformer

# For docker container only!

model_name = "sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2"

model_dir = Path("/model")
model_dir.mkdir(parents=True, exist_ok=True)

model = SentenceTransformer(model_name)
model.save(os.fspath(model_dir))


RUN python /app/download_model.py
RUN mkdir -p /models
