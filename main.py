from data_loader import load_json
from artifact_evaluator import evaluate_artifact

def main():
    # JSON 파일 로드
    character_data = load_json('data/character_artifact_data.json')
    
    # 사용자로부터 성유물 정보 입력
    artifact = {
        "part": input("성유물 부위를 입력하세요: "),
        "set": input("성유물 세트를 입력하세요: "),
        "main_stat": input("주 옵션을 입력하세요: "),
        "sub_stats": input("부 옵션들을 콤마로 구분해 입력하세요: ").split(", ")
    }

    # 성유물 평가
    result = evaluate_artifact(artifact, character_data)

    # 결과 출력
    if result:
        for r in result:
            print(f"캐릭터: {r['character']}")
            print(f"유효 부옵션 수 (우선순위 1): {r['valid_sub_stats_1']}")
            print(f"유효 부옵션 수 (우선순위 2): {r['valid_sub_stats_2']}")
            print(f"총 점수: {r['total_score']}")
            print(f"유형: {r['type']}")
            print("-" * 20)
    else:
        print("해당 성유물에 맞는 캐릭터가 없습니다.")

if __name__ == "__main__":
    main()