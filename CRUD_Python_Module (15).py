# CRUD_Python_Module.py — CS-340
from pymongo import MongoClient, errors
from pymongo.collection import Collection

class AnimalShelter:
    def __init__(
        self,
        username: str | None = None,
        password: str | None = None,
        host: str = "127.0.0.1",
        port: int = 27017,
        db_name: str = "AAC",
        coll_name: str = "animals",
        auth_db: str = "admin",
        server_selection_timeout_ms: int = 3000,
        retry_fallback_noauth: bool = True,
    ):
        """
        Connect to MongoDB. Works whether auth is ON or OFF.
        If auth fails, automatically retries a no-auth connection.
        """
        self._client = None
        self._db = None
        self._coll = None

        def _make_uri(with_auth: bool) -> str:
            if with_auth and username and password:
                return (
                    f"mongodb://{username}:{password}@{host}:{port}/"
                    f"?authSource={auth_db}&retryWrites=true&w=majority"
                    f"&directConnection=true"
                )
            return f"mongodb://{host}:{port}/?directConnection=true"

        last_err = None

        # Try with credentials first (if provided)
        try:
            if username and password:
                uri = _make_uri(with_auth=True)
                self._client = MongoClient(uri, serverSelectionTimeoutMS=server_selection_timeout_ms)
                self._client.admin.command("ping")
                self._db = self._client[db_name]
                self._coll: Collection = self._db[coll_name]
                return
        except errors.PyMongoError as e:
            last_err = e
            if not retry_fallback_noauth:
                raise RuntimeError(f"MongoDB authentication failed: {e}") from e

        # Fallback to no-auth (common in Codio images)
        try:
            uri = _make_uri(with_auth=False)
            self._client = MongoClient(uri, serverSelectionTimeoutMS=server_selection_timeout_ms)
            self._client.admin.command("ping")
            self._db = self._client[db_name]
            self._coll: Collection = self._db[coll_name]
        except errors.PyMongoError as e:
            raise RuntimeError(
                f"MongoDB connection failed after fallback: {e}\nOriginal error: {last_err}"
            ) from e

    # ---------- CRUD Operations ----------

    # Create
    def create(self, data: dict) -> bool:
        if not isinstance(data, dict) or not data:
            raise ValueError("create() expects a non-empty dict")
        result = self._coll.insert_one(data)
        return result.acknowledged

    # Read (returns list of dicts)
    def read(self, query: dict | None = None, projection: dict | None = None) -> list[dict]:
        q = query or {}
        cursor = self._coll.find(q, projection)
        docs = list(cursor)
        for d in docs:
            if "_id" in d:
                d["_id"] = str(d["_id"])
        return docs

    # Update (returns modified count)
    def update(self, query: dict, new_values: dict) -> int:
        if not isinstance(query, dict) or not isinstance(new_values, dict):
            raise ValueError("update() expects dicts")
        result = self._coll.update_many(query, {"$set": new_values})
        return result.modified_count

    # Delete (returns deleted count)
    def delete(self, query: dict) -> int:
        if not isinstance(query, dict):
            raise ValueError("delete() expects a dict")
        result = self._coll.delete_many(query)
        return result.deleted_count
