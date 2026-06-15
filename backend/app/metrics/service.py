from app.metrics.repository import (
    get_metrics,
)


class MetricsService:

    def get_metrics(self,db):

        result = (get_metrics(db=db))

        return {
            "documents": result[0],
            "chunks": result[1],
            "questions": result[2],
            "evaluations": result[3],
        }