from flask import Flask, request, jsonify, render_template
from data_loader import load_json
from artifact_evaluator import evaluate_artifact

app = Flask(__name__)

# JSON 데이터 불러오기
try:
    character_data = load_json('data/character_artifact_data.json')
except Exception as e:
    print(f"데이터 로딩 오류: {e}")

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/evaluate', methods=['POST'])
def evaluate():
    try:
        artifact = request.get_json()
        if not artifact:
            print("빈 데이터가 전달되었습니다.")
            return jsonify({"error": "빈 데이터가 전달되었습니다."}), 400
        
        print("받은 데이터:", artifact)  # 받은 데이터 로그
        result = evaluate_artifact(artifact, character_data)
        print("평가 결과:", result)  # 평가 결과 로그
        return jsonify(result), 200  # 상태 코드 200으로 응답

    except Exception as e:
        print(f"Error occurred: {e}")
        # 오류 로그와 함께 JSON 응답 반환
        return jsonify({"error": f"서버 오류가 발생했습니다: {e}"}), 500

if __name__ == '__main__':
    app.run(debug=True)
