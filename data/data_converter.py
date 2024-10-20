import pandas as pd
import json
import os
import numpy as np

def convert_csv_to_json(csv_file_path, json_file_path):
    try:
        # CSV 파일을 읽기
        data = pd.read_csv(csv_file_path)
        print("CSV 파일을 성공적으로 읽었습니다.")
        
        # NaN 값을 None으로 대체
        data = data.replace({np.nan: None})
        
        # "main_stats"와 "valid_sub_stats"를 처리
        records = []
        for index, row in data.iterrows():
            # main_stats를 딕셔너리 형태로 구성
            main_stats = {
                "flower": [row['flower']] if pd.notna(row['flower']) else [],
                "feather": [row['feather']] if pd.notna(row['feather']) else [],
                "sand": row['sand'].split(", ") if pd.notna(row['sand']) else [],
                "goblet": row['goblet'].split(", ") if pd.notna(row['goblet']) else [],
                "circlet": row['circlet'].split(", ") if pd.notna(row['circlet']) else []
            }

            # valid_sub_stats를 리스트로 변환
            valid_sub_stats_1 = row['valid_sub_stats_1'].split(", ") if pd.notna(row['valid_sub_stats_1']) else []
            valid_sub_stats_2 = row['valid_sub_stats_2'].split(", ") if pd.notna(row['valid_sub_stats_2']) else []

            # preferred_set_1과 2를 딕셔너리 형태로 변환
            preferred_set_1 = {
                "set": row['preferred_set_1'],
                "priority": 1
            } if pd.notna(row['preferred_set_1']) else None

            preferred_set_2 = {
                "set": row['preferred_set_2'],
                "priority": 2
            } if pd.notna(row['preferred_set_2']) else None

            # 한 캐릭터의 데이터를 딕셔너리로 구성
            character_data = {
                "name": row['name'],
                "main_stats": main_stats,
                "valid_sub_stats_1": valid_sub_stats_1,
                "valid_sub_stats_2": valid_sub_stats_2,
                "preferred_set_1": preferred_set_1,
                "preferred_set_2": preferred_set_2
            }
            
            records.append(character_data)
            print(f"캐릭터 {row['name']} 데이터 변환 완료: {character_data}")  # 디버깅 출력 추가

        # JSON 파일로 저장
        with open(json_file_path, 'w', encoding='utf-8') as json_file:
            json.dump(records, json_file, ensure_ascii=False, indent=4)
        print(f"JSON 파일로 성공적으로 변환되었습니다: {json_file_path}")

    except FileNotFoundError:
        print(f"파일을 찾을 수 없습니다: {csv_file_path}")
    except Exception as e:
        print(f"오류가 발생했습니다: {e}")

if __name__ == "__main__":
    # 파일 경로 설정
    current_dir = os.path.dirname(os.path.abspath(__file__))
    csv_file_path = os.path.join(current_dir, 'character_artifact_data.csv')
    json_file_path = os.path.join(current_dir, 'character_artifact_data.json')
    
    # CSV 파일을 JSON 파일로 변환
    convert_csv_to_json(csv_file_path, json_file_path)
