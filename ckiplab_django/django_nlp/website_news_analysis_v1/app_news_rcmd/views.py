from django.shortcuts import render
from django.http import JsonResponse
import pandas as pd
from django.views.decorators.csrf import csrf_exempt


# Notice: using different gensim version will cause errors
from gensim.models.doc2vec import Doc2Vec

# Load news data
import app_user_keyword.views as userkeyword_views
def load_df_data_v2():
    # import and use df from app_user_keyword 
    global df # global variable
    df = userkeyword_views.df

# call load data function when starting server
load_df_data_v2()

# Load doc2vec model
def load_doc2vec_model():
    global model # global variable 
    model = Doc2Vec.load("app_news_rcmd/dataset/cna_news_doc2vec.model")

# call load model function when starting server
load_doc2vec_model()

#-- home page
def home(request):
    return render(request, "app_news_rcmd/home.html")

#-- API (three APIs) 3個APIs
#-- API: input category
@csrf_exempt
def api_cate_news(request):
    cate = request.POST['category']
    response = get_cate_latest_news(cate)
    return JsonResponse({"latest_news": response})

#-- API: input keywords, get top 5 similar news 
#@csrf_exempt
def api_keywords_similar_news(request):
    keywords = request.POST['tokens']
    keywords = [t for t in keywords.split()]
    response = get_keywords_most_similar(keywords)
    return JsonResponse({"data": response})

#-- API: input news_id, and then get news information
@csrf_exempt
def api_news_content(request):
    item_id = request.POST['news_id']
    content = get_news_content(item_id)
    related = get_itemid_most_similar(item_id)
    # print(related)
    return JsonResponse({"news_content": content, "related_news": related})


# -- Given a item_id, get document information
def get_news_content(item_id):
    df_item = df[df.item_id == item_id]
    title = df_item.iloc[0].title
    content = df_item.iloc[0].content
    category = df_item.iloc[0].category
    link = df_item.iloc[0].link
    date = df_item.iloc[0].date
    photo_link = df_item.iloc[0].photo_link
    # if photo_link value is NaN, replace it with empty string 
    if pd.isna(photo_link):
        photo_link=''

    news_info = {
        "id": item_id,
        "category": category,
        "title": title,
        "content": content,
        "link": link,
        "date": date,
        "photo_link": photo_link
    }

    return news_info

#-- Given a category, get the latest news
def get_cate_latest_news(cate):
    items = []
    df_cate = df[df.category == cate]

    # get the last news (the latest news)
    df_cate = df_cate.tail(5)  # Only 5 pieces
    # only return 10 news

    for i in range( len(df_cate)):
        item_id = df_cate.iloc[i].item_id    
        title = df_cate.iloc[i].title
        content = df_cate.iloc[i].content
        category = df_cate.iloc[i].category
        link = df_cate.iloc[i].link
        photo_link = df_cate.iloc[i].photo_link
        # if photo_link value is NaN, replace it with empty string 
        if pd.isna(photo_link):
            photo_link=""

        item = {
            "id": item_id, 
            "category": category, 
            "title": title,
            "content": content, 
            "link": link,
            "photo_link": photo_link
        }

        items.append(item)
    
    return items

#--Given news keywords, find similar documents 
def get_keywords_most_similar(keywords):
    new_vector = model.infer_vector(keywords)
    similar_items = model.docvecs.most_similar(positive=[new_vector], topn=5)
    items = []
    for item_id, score in similar_items:
        df_item = df[df.item_id == item_id]
        
        title = df_item.iloc[0].title
        content = df_item.iloc[0].content
        category = df_item.iloc[0].category
        link = df_item.iloc[0].link
        photo_link = df_item.iloc[0].photo_link
        # if photo_link value is NaN, replace it with empty string 
        if pd.isna(photo_link):
            photo_link=''

        score = round(score, 2)
        
        item = {
            "id": item_id, 
            "category": category, 
            "title": title, 
            "link": link,
            'score': score, 
            "photo_link": photo_link
            }
        items.append(item)

    return items

#-- Given item_id, get three similar news based on the doc2vec model
def get_itemid_most_similar(item_id):
    similar_items = model.docvecs.most_similar(positive=[item_id], topn=3)
    items = []
    for item_id, score in similar_items:
        df_item = df[df.item_id == item_id]
        title = df_item.iloc[0].title
        content = df_item.iloc[0].content
        category = df_item.iloc[0].category
        link = df_item.iloc[0].link
        photo_link = df_item.iloc[0].photo_link
        # if photo_link value is NaN, replace it with empty string 
        if pd.isna(photo_link):
            photo_link=''

        score = round(score, 2)
        item = {
            "category": category, 
            "title": title, 
            "link": link,
            "id": item_id, 
            'score': score, 
            "photo_link": photo_link
            }
        items.append(item)
    return items

print("app_doc2vec -- 今日新聞瀏覽與新聞推薦載入成功!")
