
- `ID_scan.ipynb`: A Jupyter notebook that installs the `pytesseract` library.
- `ID_Scanner.py`: A Streamlit application that allows users to upload an image and extracts text from it using `pytesseract`.

## Installation

1. Clone the repository:
    ```sh
    git clone <repository-url>
    cd <repository-directory>
    ```

2. Install the required Python packages:
    ```sh
    pip install -r requirements.txt
    ```

3. Install Tesseract OCR:
    - Download and install Tesseract OCR from [here](https://github.com/tesseract-ocr/tesseract).
    - Update the [tesseract_cmd](http://_vscodecontentref_/2) path in [ID_Scanner.py](http://_vscodecontentref_/3) to the installed location of Tesseract OCR.

## Usage

1. Run the Streamlit application:
    ```sh
    streamlit run ID_Scanner.py
    ```

2. Open the application in your web browser. You will see an interface to upload an image.

3. Upload an image of an ID card. The application will extract and display the text from the image.

## Dependencies

- [streamlit](http://_vscodecontentref_/4)
- [cv2](http://_vscodecontentref_/5)
- [numpy](http://_vscodecontentref_/6)
- [pandas](http://_vscodecontentref_/7)
- [pytesseract](http://_vscodecontentref_/8)
- [matplotlib](http://_vscodecontentref_/9)
- `Pillow`

## License

This project is licensed under the MIT License.
