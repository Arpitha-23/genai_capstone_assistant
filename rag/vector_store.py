import numpy as np
import faiss


class VectorStore:

    def __init__(self):

        self.index = None

        self.documents = []


    # --------------------------------------------------
    # Build Vector Index
    # --------------------------------------------------

    def build(self, embeddings, documents):

        if not embeddings:

            raise ValueError(
                "No embeddings were provided."
            )

        vectors = np.array(
            embeddings,
            dtype="float32"
        )

        dimension = vectors.shape[1]

        self.index = faiss.IndexFlatL2(
            dimension
        )

        self.index.add(vectors)

        self.documents = documents


    # --------------------------------------------------
    # Search Similar Documents
    # --------------------------------------------------

    def search(
        self,
        query_embedding,
        top_k=3
    ):

        if self.index is None:

            return []

        query_vector = np.array(
            [query_embedding],
            dtype="float32"
        )

        distances, indices = self.index.search(
            query_vector,
            min(top_k, len(self.documents))
        )

        results = []

        for distance, index in zip(
            distances[0],
            indices[0]
        ):

            if index < 0:
                continue

            results.append(
                {
                    "document": self.documents[index],
                    "distance": float(distance)
                }
            )

        return results


    # --------------------------------------------------
    # Clear Store
    # --------------------------------------------------

    def clear(self):

        self.index = None

        self.documents = []