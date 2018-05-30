import pymongo

# BSON - Binary Json
def main():
    # client = pymongo.MongoClient('mongodb://47.106.134.92:27017')
    client = pymongo.MongoClient(host='47.106.134.92',port=27017)
    # 创建数据库
    db = client.zhihu
    # 创建集合（数据表）
    pages_cache = db.webpages

    # 一次插入多个数据（用列表装载）
    # pages_cache.insert_many([
    #     {'_id':1,'url':'http://www.baidu.com','content':'one_shit'},
    #     {'_id':2,'url':'http://www.google.com','content':'two_shit'},
    #     {'_id':3,'url':'http://www.sina.com','content':'three_shit'}
    # ])

    # 更新数据（先找到该数据 -- {'_id':3}，再指定更新规则 -- {'$set':{xxxxx}}）
    # 如果没有$set字段，更新部分会覆盖原有的所有数据
    # pages_cache.update({'_id':3},{'$set':{xxxxx}})

    # upsert字段 -- 数据存在，即为更新，不在，即为插入
    # pages_cache.update({'_id':4,},{'$set':{'url':'http://www.runoob.com','content':'hello,world'}},upsert=True)

    # 生成插入对象
    # page= pages_cache.insert_one({'url':'http://www.baidu.com','content':'hahaha'})
    # 获取插入对象的id
    # print(page.inserted_id)

    # 删除指定数据
    # pages_cache.remove({'url':'http://www.baidu.com'})

    # 计算集合中的数据条数
    print(pages_cache.find().count())
    # 按照内容排序
    for doc in pages_cache.find().sort('content'):
        print(doc)

    # 文档中嵌套文档
    pages_cache.insert_one({
        'url':'http://www.math.com',
        'content':'bull shit',
        'owner':{
            'name':'Lee',
            'id_card':'620',
            'age':50
        }
    })

if __name__ == '__main__':
    main()