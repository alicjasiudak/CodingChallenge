from abc import ABC, abstractmethod
from typing import Dict, List


class IAPIService(ABC):

    @abstractmethod
    def _fetch_json(self, endpoint: str) -> Dict:
        pass

    @abstractmethod
    def fetch_users(self) -> List[Dict]:
        pass

    @abstractmethod
    def fetch_user_by_name(self, username: str) -> Dict:
        pass

    @abstractmethod
    def fetch_user_by_id(self, user_id: str) -> Dict:
        pass

    @abstractmethod
    def fetch_sets(self) -> Dict:
        pass

    @abstractmethod
    def fetch_set_by_name(self, set_name) -> Dict:
        pass

    @abstractmethod
    def fetch_set_by_id(self, set_id) -> Dict:
        pass
