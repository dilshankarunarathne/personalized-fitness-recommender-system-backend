from backend.blood_report_analyzer.ocr import ocr_img_base64


def analyze_blood_sugar_report(report_img_data):  # TODO
    # read base64 str image data
    img_data = ocr_img_base64(report_img_data)
    # convert to text using ocr module

    # process text using analyzer module
