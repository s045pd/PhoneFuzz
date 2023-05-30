import argparse
from itertools import product
from typing import Generator

from phone import Phone
from streamlit.runtime.scriptrunner import get_script_run_ctx

operator = [
    "移动",
    "联通",
    "电信",
    "电信虚拟运营商",
    "联通虚拟运营商",
    "移动虚拟运营商",
]

p = Phone()


def phone_gen(template: str) -> Generator:
    """
    根据手机号模版枚举所有手机号
    """
    code_number = template.count("*")
    for item in product(*[range(10) for i in range(code_number)]):
        number = template
        for i in range(code_number):
            number = number.replace("*", str(item[i]), 1)
        yield number


def filter_with_location(number: str, config: dict) -> None or dict:
    """
    查询手机号，根据配置过滤

    config格式:{
        "province":"xx",
        "city":"xx",
        "phone_type":"xx",
        "area_code":"xx",
        "zip_code":"",
    }

    """
    result = p.find(number)
    if not result:
        return
    if len([0 for k, v in config.items() if result.get(k) == v]) == len(config):
        return result


def search(number: str, config: dict) -> Generator:
    """
    实际运行方法
    """
    config = {
        k: v
        for k, v in {
            "province": config.get("province"),
            "city": config.get("city"),
            "phone_type": config.get("phone_type"),
            "area_code": config.get("area_code"),
            "zip_code": config.get("zip_code"),
        }.items()
        if v
    }

    for item in phone_gen(number):
        if result := filter_with_location(item, config):
            yield result


def ui():
    import pandas as pd
    import streamlit as st

    @st.cache_data
    def convert_df(df):
        return df.to_csv(index=False).encode("utf-8")

    # 创建输入框和提交按钮
    st.title("PhoneFuzz")
    phone_number = st.text_input(
        ":iphone:号码 :", placeholder="123****1234、123**123456"
    ).strip()
    province = st.text_input(":office: 省份:", placeholder="北京、上海").strip()
    city = st.text_input(":house_buildings: 城市:").strip()
    postal_code = st.text_input(":postbox: 邮编:").strip()
    phone_type = st.selectbox(":department_store: 运营商:", pd.Series([None] + operator))
    if st.button("提交"):
        # 运行生成器，生成数据
        data = search(
            phone_number,
            {
                "province": province,
                "city": city,
                "postal_code": postal_code,
                "phone_type": phone_type,
            },
        )
        df = pd.DataFrame(data)
        st.dataframe(df)
        st.download_button(
            label="导出",
            data=convert_df(df),
            file_name=f"{phone_number}.csv",
            mime="text/csv",
        )


def cli():
    args_parser = argparse.ArgumentParser()
    args_parser.add_argument("-p", "--province", default="", help="省份")
    args_parser.add_argument("-c", "--city", default="", help="城市")
    args_parser.add_argument(
        "-t", "--phone_type", default="", help="运营商", choices=operator
    )
    args_parser.add_argument("-z", "--zip_code", default="", help="邮编")
    args_parser.add_argument(
        "-d", "--detail", action=argparse.BooleanOptionalAction, help="输出详情"
    )
    args_parser.add_argument("phone", help="手机号模版")
    args = args_parser.parse_args()

    for index, item in enumerate(
        search(
            args.phone,
            {
                "province": args.province,
                "city": args.city,
                "phone_type": args.phone_type,
                "area_code": args.area_code,
                "zip_code": args.zip_code,
            },
        )
    ):
        if not args.detail:
            print(index, item["phone"])
            continue
        print(index, item)


def main():
    if get_script_run_ctx():
        return ui()
    else:
        return cli()


if __name__ == "__main__":
    main()
