import pandas as pd

df = pd.read_csv("youtube-ing.csv")
soru1 = df.head(10)
soru2 = df[5:].head()
soru3a = df.columns
soru3b = len(soru3a)
soru4 = df.drop(['thumbnail_link','comments_disabled','ratings_disabled','video_error_or_removed','description'],axis=1)
soru5like = df.likes.mean()
soru5dislike = df.dislikes.mean()
soru6 = df[["likes","dislikes"]].head(50)
soru7 = df[df["views"]==df["views"].max()]["title"]
soru8 = df[df["views"]==df["views"].min()]["title"]
soru9 = df.sort_values("views",ascending=True).head(10).title
soru10 = df.groupby('category_id').likes.mean()
soru11 = df.groupby('category_id').comment_count.head(38915)
soru12 = df.groupby('category_id').count()
#soru13
df["titleLong"] = df["title"].str.len()
#soru14
df["numberOfTag"] = df["tags"].count()
soru15 = df[df["likes"]>df["dislikes"]].head(100).sort_values("likes",ascending=False)[["likes","dislikes"]]



print(df)
print("<<<<<<<<<<**********>>>>>>>>>>")
print(soru15)
