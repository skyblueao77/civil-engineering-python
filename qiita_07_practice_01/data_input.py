import io
import time

import pandas as pd
import requests

prec_no = "62"  # 大阪府
block_no = "47772"  # 大阪
year = 2025

all_month_dfs: list[pd.DataFrame] = []

print(f"{year}年の気象データを取得中...")

session = requests.Session()
session.headers.update(
    {
        "User-Agent": (
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"
            " (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
        ),
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
        "Referer": "https://www.data.jma.go.jp/stats/etrn/index.php",
    }
)

for month in range(1, 13):
    url = f"https://www.data.jma.go.jp/stats/etrn/view/daily_s1.php?prec_no={prec_no}&block_no={block_no}&year={year}&month={month}&day=&view="

    try:
        response = session.get(url, timeout=10)
        response.encoding = "utf-8"

        if response.status_code != 200:
            continue

        tables = pd.read_html(io.StringIO(response.text))

        target_df = None
        max_rows = 0

        for df in tables:
            if len(df) >= 20 and len(df) > max_rows:
                target_df = df
                max_rows = len(df)

        if target_df is not None:
            # 多重ヘッダーを1行の分かりやすい列名に整形
            if isinstance(target_df.columns, pd.MultiIndex):
                new_cols = []
                for col in target_df.columns:
                    col_parts = [
                        str(c).strip()
                        for c in col
                        if "Unnamed" not in str(c) and str(c).strip() != ""
                    ]
                    seen = set()
                    unique_parts = [
                        x for x in col_parts if not (x in seen or seen.add(x))
                    ]
                    new_cols.append("_".join(unique_parts))
                target_df.columns = new_cols

            target_df["月"] = month
            all_month_dfs.append(target_df)
            print(f"{month}月: 取得・整形成功")

    except Exception as e:
        print(f"{month}月: エラー発生 - {e}")

    time.sleep(1)

# データの結合と数値クリーニング
if len(all_month_dfs) > 0:
    df_all: pd.DataFrame = pd.concat(all_month_dfs, ignore_index=True)

    # 【修正点】正規表現を使わず（regex=False）、完全一致の記号を空文字に置換
    df_all = df_all.replace(["--", "///", "]", ")", "}"], "", regex=False)

    df_all["年"] = year

    file_name = f"osaka_weather_{year}_cleaned.csv"
    df_all.to_csv(file_name, index=False, encoding="utf_8_sig")
    print(f"\n整形完了・保存済み: {file_name}")
    print(df_all.head())
else:
    print("\nデータが取得できませんでした。")