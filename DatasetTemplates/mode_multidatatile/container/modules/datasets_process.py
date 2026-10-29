from rdetoolkit.errors import catch_exception_with_message
from rdetoolkit.models.rde2types import RdeDatasetPaths


@catch_exception_with_message(
    error_message="ERROR: failed in data processing", error_code=50
)
def dataset(paths: RdeDatasetPaths) -> None:
    # 各データ単位の入力ファイルの一覧を出力
    print(paths.rawfiles)
