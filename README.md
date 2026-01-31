# OBS Python Scripts

Hello! These are some python script(s) I've written for OBS Virtual Camera.

## Usage

1. Clone this repo: ```git clone https://github.com/DatBogie/obs-py-scripts.git```
2. `cd` into repo.
3. Write `obs-py-scripts/.env` (replace values in '<>'s, value after the '|' is the default/recommended value):

    ```dotenv
    OBS_HOST="<YOUR_hostname | localhost>"
    OBS_PORT=<YOUR_PORT | 4455>
    OBS_PASSWORD="<YOUR_WebSocket_SERVER_PASSWORD>"
    ```

4. Setup `.venv` (Windows may use `python` or `py` instead of `python3`, depending on how you installed it):

    ```sh
    python3 -m venv .venv;pip3 install -r requirements.txt
    ```

5. Run (or use an IDE/editor like VSCode):

    ```sh
    python3 <script_name>.py
    ```

6. To stop a script, focus the terminal and press any key.  
   **Stopping via this method allows the script to reset certain effects. Otherwise, it may ruin your Virtual Camera setup!**

## Scripts

- ### `default.py`

  1. Create a scene called "Virtual Camera".
  2. Create two image sources: "Bunnies", and "Bird".
  3. Set the "Bird" source to any image you'd like and position it where you'd like. It will float around.
  4. Any images in `obs-py-scripts/random_images` will randomly flash in and fade out on-screen. Ensure there is at least one image in the `random_images` folder, and no invalid files.

  #### Settings

  ```dotenv
  OBS_SCRIPT_DEFAULT_RANDOM_CHANCE_IN=<CHANCE_IMG_FLASHES_ONE_OUT_OF_NUM | 10>
  OBS_SCRIPT_DEFAULT_DELAY=<MIN_TIME_BTWN_IMG_FLASHES | 6>
  ```
