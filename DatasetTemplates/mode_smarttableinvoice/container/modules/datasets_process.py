from rdetoolkit.errors import catch_exception_with_message
from rdetoolkit.models.rde2types import RdeInputDirPaths, RdeOutputResourcePath

@catch_exception_with_message(error_message="ERROR: failed in data processing")
def dataset(srcpaths: RdeInputDirPaths, resource_paths: RdeOutputResourcePath) -> None:
    # 各データ単位の入力ファイルの一覧を出力
    print(resource_paths.rawfiles)
