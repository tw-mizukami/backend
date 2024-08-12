##DB初期化コマンド
flask db init

##マイグレーション作成コマンド
flask db migrate -m "init machine table"

##マイグレーションの反映コマンド
flask db upgrade

##テーブル追加した場合にやること
modelsの__init__.pyに追加
マイグレーション作成コマンド
マイグレーションの反映コマンド
