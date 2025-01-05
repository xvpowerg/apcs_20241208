def testScore(score):
    #檢查 score 必須大於0 小於等於100
    #不在這個區間 顯示錯誤的成績
    #在這個區間 顯示成績
    if score < 0 or score > 100:
        #print("錯誤的成績")
        raise Exception("錯誤的成績")
    print(f"成績:{score}")
testScore(900)#錯誤的成績
testScore(85)#成績:85
