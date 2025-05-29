from fastapi import FastAPI, Query
from recommendation import TourRecommender

app = FastAPI()
recommender = TourRecommender()  

@app.get("/recommend")
def recommend_tours(tour_name: str = Query(..., description="Tour name to base recommendations on")):
    result = recommender.recommend(tour_name)
    return {"recommended": result}
