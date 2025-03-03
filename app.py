# -*- coding:utf-8 -*-

# seoul_real_estate.csv 로드
#      ↓
# app07.py (메인 실행파일, 메뉴 선택)
#      ↓
# 홈 / 탐색적 자료분석 / 부동산 예측 (메뉴 이동)
#      ↓
# 탐색적 자료분석 선택 시 eda_home.py 실행
#      ↓
# 통계분석 선택 시 stat.py 내부 showStat() 실행
#      ↓
# 두 집단 t-검정 또는 상관분석 선택 후 실행

import streamlit as st
from streamlit_option_menu import option_menu
from home import run_home
from utils import load_data
from eda.eda_home import run_eda

def main():
    total_df = load_data()
    with st.sidebar:
        selected = option_menu("대시보드 메뉴", ['홈', '탐색적 자료분석', '부동산 예측'], 
                               icons=['house', 'file-bar-graph', 'graph-up-arrow'], menu_icon="cast", default_index=0)
    if selected == "홈":
        run_home()
    elif selected == "탐색적 자료분석":
        run_eda(total_df)
    elif selected == "부동산 예측":
        pass
    else:
        print("error..")
        
if __name__ == "__main__":
    main()