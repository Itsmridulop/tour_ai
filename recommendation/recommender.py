from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from db import get_tour_dataframe
from bson import ObjectId


class TourRecommender:
    def __init__(self):
        self.df = get_tour_dataframe()
        self._prepare()

    def _prepare(self):
        self.df.fillna('', inplace=True)
        self.df['content'] = (
            self.df['name'].astype(str) + ' ' +
            self.df['summary'].astype(str) + ' ' +
            self.df['description'].astype(str) + ' ' +
            self.df['difficulty'].astype(str) + ' ' +
            self.df['duration'].astype(str) + ' ' +
            self.df['price'].astype(str)
        )
        self.tfidf = TfidfVectorizer(stop_words='english')
        self.tfidf_matrix = self.tfidf.fit_transform(self.df['content'])
        self.cosine_sim = cosine_similarity(self.tfidf_matrix, self.tfidf_matrix)

    def _convert_object_ids(self,obj):
        if isinstance(obj, dict):
            return {k: self._convert_object_ids(v) for k, v in obj.items()}
        elif isinstance(obj, list):
            return [self._convert_object_ids(item) for item in obj]
        elif isinstance(obj, ObjectId):
            return str(obj)
        else:
            return obj

    def recommend(self, tour_name: str):
        if tour_name == 'all':
            results = self.df.to_dict(orient='records')
            return [self._convert_object_ids(doc) for doc in results]
        if tour_name not in self.df['name'].values:
            return []
        idx = self.df[self.df['name'] == tour_name].index[0]
        sim_scores = list(enumerate(self.cosine_sim[idx]))
        sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)
        tour_indices = [i[0] for i in sim_scores]
        results = self.df.iloc[tour_indices].to_dict(orient='records')
        return [self._convert_object_ids(doc) for doc in results]
