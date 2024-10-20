def evaluate_artifact(artifact, character_data):
    """성유물을 평가하여 캐릭터와의 매칭 결과를 반환하는 함수"""
    matching_characters = []

    for character in character_data:
        print(f"캐릭터: {character['name']} 검사 중...")  # 디버깅 로그

        preferred_sets = []
        if character.get('preferred_set_1'):
            preferred_sets.append(character['preferred_set_1']['set'])

        if character.get('preferred_set_2'):
            preferred_sets.append(character['preferred_set_2']['set'])

        # main_stats 접근 및 확인
        main_stats = character.get('main_stats', {})
        print(f"{character['name']}의 main_stats: {main_stats}")  # main_stats 전체 출력

        # 해당 부위의 주 옵션이 있는지 확인
        part_stats = main_stats.get(artifact['part'], [])
        print(f"{character['name']}의 {artifact['part']}의 주옵션: {part_stats}")  # 주 옵션 로그

        # 주 옵션 일치 확인
        is_main_stat_matching = artifact['main_stat'] in part_stats
        print(f"주 옵션 일치 여부: {is_main_stat_matching}")  # 디버깅 로그

        valid_sub_stats_1_data = character.get('valid_sub_stats_1', [])
        valid_sub_stats_2_data = character.get('valid_sub_stats_2', [])
        if valid_sub_stats_1_data is None:
            valid_sub_stats_1_data = []
        if valid_sub_stats_2_data is None:
            valid_sub_stats_2_data = []

        valid_sub_stats_1 = [stat for stat in artifact['sub_stats'] if stat in valid_sub_stats_1_data]
        valid_sub_stats_2 = [stat for stat in artifact['sub_stats'] if stat in valid_sub_stats_2_data]
        
        print(f"유효 부옵션 (우선순위 1): {valid_sub_stats_1}, (우선순위 2): {valid_sub_stats_2}")  # 디버깅 로그

        if artifact['set'] in preferred_sets and is_main_stat_matching:
            score = len(valid_sub_stats_1) * 2 + len(valid_sub_stats_2)
            result = {
                "character": character['name'],
                "valid_sub_stats_1": len(valid_sub_stats_1),
                "valid_sub_stats_2": len(valid_sub_stats_2),
                "total_score": score,
                "type": "matching set"
            }
            matching_characters.append(result)
            print(f"{character['name']}이(가) 세트에 맞는 캐릭터로 추가됨.")  # 디버깅 로그
        elif is_main_stat_matching and (len(valid_sub_stats_1) > 0 or len(valid_sub_stats_2) > 0):
            score = len(valid_sub_stats_1) * 2 + len(valid_sub_stats_2)
            result = {
                "character": character['name'],
                "valid_sub_stats_1": len(valid_sub_stats_1),
                "valid_sub_stats_2": len(valid_sub_stats_2),
                "total_score": score,
                "type": "mercenary"
            }
            matching_characters.append(result)
            print(f"{character['name']}이(가) 용병 캐릭터로 추가됨.")  # 디버깅 로그
        else:
            print(f"{character['name']}이(가) 조건에 맞지 않음.")  # 디버깅 로그
    
    return matching_characters
