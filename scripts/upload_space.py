import os
from pathlib import Path
from huggingface_hub import HfApi

SPACE_ID = "Mubtakir/bayaan-demo"
FOLDER = "hf_space/bayaan_demo"


def main():
    token = os.getenv("HF_TOKEN")
    if not token:
        raise SystemExit("HF_TOKEN environment variable is required (export HF_TOKEN=...)")

    folder = Path(FOLDER)
    print("Folder:", folder.resolve())
    print("Exists:", folder.exists())
    if not folder.exists():
        raise SystemExit("Folder not found")
    print("Top-level files:", [p.name for p in folder.iterdir()])

    api = HfApi()
    api.upload_folder(
        repo_id=SPACE_ID,
        repo_type="space",
        folder_path=FOLDER,
        token=token,
        commit_message="feat(space): add full Bayan parser validation (vendored) with fallback",
    )
    print("[OK] Space updated:", SPACE_ID)
    print("URL:", f"https://huggingface.co/spaces/{SPACE_ID}")


if __name__ == "__main__":
    main()

