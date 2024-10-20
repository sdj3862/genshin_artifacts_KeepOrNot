import json

def load_json(file_path):
    """JSON 파일을 불러와 Python 객체로 변환하는 함수"""
    with open(file_path, 'r', encoding='utf-8') as f:
        data = json.load(f)
    return data
