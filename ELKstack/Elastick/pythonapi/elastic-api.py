from elasticsearch import Elasticsearch

# Initialisation du client Elasticsearch
es = Elasticsearch()

# Fonction pour vérifier si un index existe
def check_index(index_name):
    return es.indices.exists(index=index_name)

# Fonction pour créer un index
def create_index(index_name):
    if not check_index(index_name):
        print(f"Index '{index_name}' n'existe pas. Création de l'index...")
        es.indices.create(index=index_name, ignore=400)
        print(f"Index '{index_name}' créé.")
    else:
        print(f"Index '{index_name}' existe déjà.")

# Fonction pour insérer des documents dans un index
def insert_documents(index_name):
    # Documents à insérer
    doc1 = {"title": "Inception", "director": "Christopher Nolan", "year": 2010}
    doc2 = {"title": "The Dark Knight", "director": "Christopher Nolan", "year": 2008}
    doc3 = {"title": "Star Wars: A New Hope", "director": "George Lucas", "year": 1977}
    doc4 = {"title": "Star Wars: The Force Awakens", "director": "J.J. Abrams", "year": 2015}
    
    # Insertion des documents
    es.index(index=index_name, doc_type="_doc", id=1, body=doc1)
    es.index(index=index_name, doc_type="_doc", id=2, body=doc2)
    es.index(index=index_name, doc_type="_doc", id=3, body=doc3)
    es.index(index=index_name, doc_type="_doc", id=4, body=doc4)
    print(f"Documents insérés dans l'index '{index_name}'.")

# Fonction pour effectuer une recherche avec critères booléens
def search_movies_with_bool(index_name):
    try:
        # Requête booléenne avec 'must', 'must_not', et 'should'
        res = es.search(index=index_name, body={
            "query": {
                "bool": {
                    "must": [
                        { "match": { "title": "Star Wars" }}
                    ],
                    "must_not": {
                        "match": { "director": "George Miller" }
                    },
                    "should": [
                        { "match": { "title": "Star" }},
                        { "match": { "director": "George Lucas" }}
                    ]
                }
            }
        })

        # Affichage des résultats
        if res['hits']['total']['value'] > 0:
            print("Résultats trouvés avec la logique booléenne :")
            for hit in res['hits']['hits']:
                print(hit['_source'])
        else:
            print("Aucun film trouvé avec les critères booléens.")

    except Exception as e:
        print(f"Erreur lors de la recherche : {e}")

# Fonction pour effectuer une agrégation par année
def aggregate_movies_by_year(index_name):
    try:
        # Agrégation simple pour compter les films par année
        res = es.search(index=index_name, body={
            "aggs": {
                "nb_par_annee": {
                    "terms": {
                        "field": "year"
                    }
                }
            }
        })
        
        # Affichage des résultats de l'agrégation
        print("Agrégation des films par année :")
        for bucket in res['aggregations']['nb_par_annee']['buckets']:
            print(f"Année {bucket['key']} : {bucket['doc_count']} films")
    
    except Exception as e:
        print(f"Erreur lors de l'agrégation : {e}")

# Fonction principale
def main():
    index_name = "movies"

    # Vérifier et créer l'index
    create_index(index_name)

    # Insérer des documents dans l'index
    insert_documents(index_name)

    # Effectuer une recherche avec la logique booléenne
    search_movies_with_bool(index_name)

    # Effectuer une agrégation pour compter les films par année
    aggregate_movies_by_year(index_name)

if __name__ == "__main__":
    main()