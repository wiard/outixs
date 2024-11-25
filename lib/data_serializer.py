import json
import pickle


class DataSerializer:
    @staticmethod
    def serialize_to_json(data, file_path):
        try:
            with open(file_path, "w") as f:
                json.dump(data, f, indent=4)
                print(f"Data serialized to JSON and saved at {file_path}")
        except Exception as e:
            print(f"Error serializing to JSON: {e}")
            raise

    @staticmethod
    def deserialize_from_json(file_path):
        try:
            with open(file_path, "r") as f:
                data = json.load(f)
                print(f"Data deserialized from JSON at {file_path}")
                return data
        except Exception as e:
            print(f"Error deserializing from JSON: {e}")
            raise

    @staticmethod
    def serialize_to_pickle(data, file_path):
        try:
            with open(file_path, "wb") as f:
                pickle.dump(data, f)
                print(f"Data serialized to pickle and saved at {file_path}")
        except Exception as e:
            print(f"Error serializing to pickle: {e}")
            raise

    @staticmethod
    def deserialize_from_pickle(file_path):
        try:
            with open(file_path, "rb") as f:
                data = pickle.load(f)
                print(f"Data deserialized from pickle at {file_path}")
                return data
        except Exception as e:
            print(f"Error deserializing from pickle: {e}")
            raise
