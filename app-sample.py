# -*- coding:utf-8 -*-

import streamlit as st
from streamlit_option_menu import option_menu
from home import run_home

def main():
    with st.sidebar:
        selected = option_menu(
            "대시보드 메뉴",
            ['홈', '탐색적 자료분석', '부동산 예측'],
            icons=['house', 'file-bar-graph', 'graph-up-arrow'],
            menu_icon="cast",
            default_index=0
        )

    if selected == "홈":
        run_home()
    elif selected == "탐색적 자료분석":
        st.warning("탐색적 자료분석은 준비 중입니다.")
    elif selected == "부동산 예측":
        st.warning("부동산 예측은 준비 중입니다.")
    else:
        st.error("알 수 없는 메뉴입니다.")

if __name__ == "__main__":
    main()
