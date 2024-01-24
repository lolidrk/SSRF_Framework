# SSRF_Framework

## Overview

The SSRF_Framework is a tool designed to determine whether a given URL is benign or malicious, with a focus on identifying various malicious URLs and Server-Side Request Forgery (SSRF) vulnerabilities. The project provides two trained models, one utilizing LSTM and the other using XGBoost, to enhance the accuracy of the analysis.

## Getting Started

To get started with the SSRF_Framework, follow these steps:

1. **Clone the repository:**

    ```bash
    git clone https://github.com/lolidrk/SSRF_Framework.git
    ```

2. **Install the required libraries:**

    Make sure you have the necessary Python libraries installed. You can install them using: --will not work (currently in progress; please manually install libraries for now)

    ```bash
    pip install -r requirements.txt
    ```

## Running the Project

The SSRF_Framework by default uses the XGBoost model. To run the project with XGBoost, execute:

```bash
python3 accept.py
```

If you want to run the LSTM model, follow these steps:

1) Uncomment line number 4 in accept.py:
```bash
#import predicty_lstm
```
2) Change line number 18 from:
```bash
result = predict.make_prediction(url_features_data)
```
to:
```bash
result = predicty_lstm.make_prediction(url_features_data)
```
3) Run the project :
```bash
python3 accept.py
```
Make sure you have the correct libraries installed for the chosen model.

## Contributing
Feel free to contribute to the SSRF_Framework by opening issues or creating pull requests. Your feedback and enhancements are highly appreciated.

## License
This project is licensed under the MIT License.

