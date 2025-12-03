# RDEデータセットテンプレート　 RDE_rdetoolkit_5mode_templates

## RDEデータセットテンプレートについて

RDE (Research Data Express) は、物質・材料についての研究データをオンラインで迅速に登録するため国立研究開発法人物質・材料研究機構（以下、NIMS）が開発したシステムです。生データを登録すると自動的にデータ駆動型のマテリアル研究に適した形に構造化してクラウドに蓄積します。これによりユーザーや研究グループ内での再利用や他の研究グループとのデータの共用が容易となり、マテリアル研究開発のDX化を支援します。

データセットテンプレートは、メタデータなどの定義ファイル(jsonなど)とプログラム(主にpython)で構成されるものであり、登録データの構造化、解析などを行いRDEシステムにデータ登録するために用いられます。登録データの種類などに合わせて用意されるものです。


## 提供する資料について

RDE_rdetoolkit_5mode_templatesデータセットテンプレートは、RDEToolKitが提供している5つのデータ登録方法の説明と実際に使える5つのデータセットテンプレートを提供しています。
なお、提供するデータセットテンプレートはデータ構造化処理は含まれていません。RDEToolKitのデータ登録機能を動かして理解するため、そしてこのテンプレートを元に構造化処理を追加して開発に利用していただくことを目的としています。

5つのデータ登録方法とは
1. Invoice mode
  - 1回の登録で1件のデータを登録できる
  - [Invoice mode用データセットテンプレート](./DatasetTemplates/mode_invoice/)
2. ExcelInvoice mode
  - 1回の登録で複数のデータを登録できる
  - 登録ファイル、送状項目をエクセル形式のファイルで指定
  - [ExcelInvoice mode用データセットテンプレート](./DatasetTemplates/mode_excelinvoice/)
3. SmartTableInvoice mode
  - 1回の登録で複数のデータを登録できる
  - Excelinvoiceをより使いやすくしたもの
  - 登録ファイル、送状項目をCSV、TSV、エクセル形式のいずれかののファイルで指定
  - [SmartTableInvoice mode用データセットテンプレート](./DatasetTemplates/mode_smarttableinvoice/)
4. MultiDataTile mode
  - 1回の登録で複数のデータを登録できる
  - ただし送状項目は同一
  - [MultiDataTile mode用データセットテンプレート](./DatasetTemplates/mode_multidatatile/)
5. RDEFormat mode
  - 構造化処理済みのRDEformat形式のファイル一式を入力ファイルとする
  - 1回の登録で1件または複数のデータを登録できる
  - [RDEFormat mode用データセットテンプレート](./DatasetTemplates/mode_rdeformat/)

解説は[解説](./5mode_operation_confirmation.md)を参照してください。

データセットテンプレートの利用方法はそれぞれテンプレートのreadme.mdを参照してください。

本データセットテンプレートはRDEToolKitを用いて作成されています。\
掲載しているテンプレートの動作確認はRDEToolKit 1.3.4で行いました。

## 関連リンク

- [RDEToolKit](https://github.com/nims-mdpf/rdetoolkit)

## 利用ルールおよびライセンス
 
* 本プログラムはMITライセンスで提供されています。


### RDEおよび本ツール関するお問い合わせ

ご不明な点につきましては、以下にお問い合わせください。

国立研究開発法人物質・材料研究機構
技術開発・共用部門 材料データプラットフォーム

お問い合わせ フォーム<br>
https://dice.nims.go.jp/contact/form.html

2025.12.3 公開