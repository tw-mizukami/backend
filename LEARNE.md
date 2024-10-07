## DB初期化コマンド
flask db init

## マイグレーション作成コマンド
flask db migrate -m "init machine table"

    ## 追加
    flask db migrate -m "Added BoxNum table and relationship to LotInfo"

## マイグレーションの反映コマンド
flask db upgrade

## テーブル追加した場合にやること
modelsの__init__.pyに追加
マイグレーション作成コマンド
マイグレーションの反映コマンド

## リレーションシップ
 (ex)
  class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    age = Column(Integer)
 
    posts = relationship("Post", backref="users")    # Postとのリレーション
 
 
  class Post(Base):
    __tablename__ = 'posts'
    id = Column(Integer, primary_key=True)
    users_id = Column(Integer, ForeignKey('users.id'))
    title = Column(String)
    body = Column(Integer)
 
    user = relationship("User")
