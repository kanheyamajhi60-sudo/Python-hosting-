name: Continuous Loop with 1-min Refresh

on:
  workflow_dispatch:  # Only manual start

jobs:
  infinite-loop:
    runs-on: ubuntu-latest
    steps:
      - name: Run continuous loop
        run: |
          while true; do
            echo "Refresh at $(date)"
            # Apna ML script call karo
            # python3 model.py
            sleep 60   # Wait 1 minute
          done
