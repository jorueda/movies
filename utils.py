def clean_no_release_date(data: dict) -> dict:
    data["results"] = [item for item in data["results"]
                       if item.get("release_date")]
    return data


def get_director(data: dict) -> list:
    return [
        {
            "id": item["id"],
            "name": item["name"]
        }
        for item in data["crew"]
        if item["job"] == "Director"
    ]


def clean_related_movies_data(data: dict) -> dict:
    data["cast"] = [item for item in data["cast"] if item.get(
        "release_date") and item.get("character")]
    data["crew"] = [item for item in data["crew"]
                    if item.get("release_date") and item.get("job")]
    return data
