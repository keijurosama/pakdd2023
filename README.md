# pakdd2023-case-study

## Dataset

- tokyo2021_user_tv_sessions_data.zip
	- Contains all users watching log as sequence of tuple (userid, Program broadcast date (start), program name, watch time)
    - download at https://drive.google.com/file/d/15a0uVakCtw0ew3tLEwzNrrsHl2x7tsGk/view?usp=sharing
- tokyo2021_tv_programs_properties.csv
	- Contains properties of TV programs, for example if it is olympic-related, a news, about sport, a movie, its on-air time, etc.
- tokyo2021_olympics_properties.csv
	- Contains properties of the olympics TV program with details about the type of sport, if japan got a medal, etc.

## Notebooks

### Prerequisites

- Python 3.7.3
- pylfit v0.3.0 (https://github.com/Tony-sama/pylfit)
- tensorflow-estimator==1.15.1
- tensorboard==2.0.0
- tensorflow==1.15.0
- tensorflow-gpu==1.14


### Case study
		
- PAKDD2023 Case_study.ipynb
	- Convert user sessions into STAMP/NARM expected input, divide into train/test data.
    - For both STAMP and NARM model
        - Fit the model to the train data.
        - Extract predictions and attentions of the model over test data
        - Mask sessions data according to attention
        - Compute properties of each sessions to form a LFIT input dataset
        - Fit a DMVLP LFIT model to the encoded data
        - Weight and extract best rules that can explain for each tv program why it can appear after a session

# Notes
- STAMP and NARM  source code (in algorithms/) adapted from session-rec (https://github.com/rn5l/session-rec)