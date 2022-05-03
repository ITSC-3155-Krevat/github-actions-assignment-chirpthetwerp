from src.models import Cat, db


class CatRepo:

    def get_all_cats(self) -> list[Cat]:
        cats = Cat.query.all()
        return cats

    def get_cat(self, cat_id: int) -> Cat | None:
        cat = Cat.query.get(cat_id)
        return cat

    def create_cat(self, name: str, breed: str, num_legs: int) -> Cat:
        new_cat = Cat(name, breed, num_legs)
        db.session.add(new_cat)
        db.session.commit()
        return new_cat

    def delete_cat(self, cat_id: int) -> Cat | None:
        cat_to_delete = Cat.query.get(cat_id)
        db.session.delete(cat_to_delete)
        db.session.commit()
        return cat_to_delete


cat_repo_singleton = CatRepo()
