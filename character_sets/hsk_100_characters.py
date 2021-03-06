# -*- coding: utf-8 -*-
"""
100 Chinese characters pulled from HSK vocaburlary lists

To produce this list I ran:
---------------------------
    from load.build_dataset import get_or_create_class_label_count_pickle
    from hsk import filter_classes_by_hsk_level

    label_counts = get_or_create_class_label_count_pickle()
    classes = label_counts.keys()
    HSK_100_CLASS_LABELS = sorted(filter_classes_by_hsk_level(classes, hsk_levels=(1,2)))[:100]
"""

HSK_100_CLASS_LABELS = [
    "一",
    "七",
    "三",
    "上",
    "下",
    "不",
    "两",
    "个",
    "九",
    "也",
    "书",
    "买",
    "了",
    "二",
    "五",
    "些",
    "人",
    "从",
    "他",
    "件",
    "会",
    "住",
    "你",
    "做",
    "八",
    "六",
    "再",
    "写",
    "冷",
    "几",
    "出",
    "别",
    "到",
    "十",
    "千",
    "卖",
    "去",
    "叫",
    "号",
    "吃",
    "吗",
    "吧",
    "听",
    "呢",
    "和",
    "哪",
    "喝",
    "四",
    "回",
    "在",
    "坐",
    "块",
    "外",
    "多",
    "大",
    "太",
    "女",
    "她",
    "好",
    "姓",
    "字",
    "它",
    "完",
    "家",
    "对",
    "小",
    "少",
    "就",
    "岁",
    "年",
    "开",
    "往",
    "很",
    "忙",
    "快",
    "您",
    "想",
    "慢",
    "懂",
    "我",
    "找",
    "新",
    "日",
    "是",
    "晴",
    "最",
    "月",
    "有",
    "本",
    "来",
    "次",
    "每",
    "比",
    "水",
    "洗",
    "点",
    "热",
    "爱",
    "狗",
    "猫",
]
