def format_result(results):
    """결과를 보기 좋게 포맷팅하는 함수"""
    for result in results:
        print(f"캐릭터: {result['character']}, 유효 부옵션 수: {result['valid_sub_stats']}")
