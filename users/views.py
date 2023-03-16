import json

from typing import Any, Dict, List, Union
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView


class FileAction:

    @staticmethod
    def load_file() -> List[Dict[str, Any]]:
        try:
            with open("users.json", "r") as file:
                return json.load(file)
        except (Exception,):
            return []

    @staticmethod
    def save_file(users: List[Dict[str, Any]]) -> Response:
        try:
            with open("users.json", "w") as file:
                json.dump(users, file)
        except Exception as error:
            print(error)
            return Response('Error', status.HTTP_304_NOT_MODIFIED)


class UsersAPIView(APIView):

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self.__users_list: List[Dict[str, Any]] = FileAction.load_file()

    def get(self, *args, **kwargs) -> Response:
        return Response(self.__users_list, status.HTTP_200_OK)

    def post(self, *args, **kwargs) -> Response:
        data: Dict[str, Any] = self.request.data
        new_user_id: int = self.__users_list[-1]['id'] + 1 if self.__users_list else 1
        data['id'] = new_user_id
        self.__users_list.append(data)
        FileAction.save_file(self.__users_list)
        return Response(data, status.HTTP_201_CREATED)


class UserUpdateDelete(APIView):

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self.users_list: List[Dict[str, Union[int, str]]] = FileAction.load_file()

    def get(self, request, pk, *args, **kwargs) -> Response:
        try:
            user = next(user for user in self.users_list if user['id'] == pk)
            return Response(user, status.HTTP_200_OK)
        except StopIteration:
            return Response('Not Found', status.HTTP_404_NOT_FOUND)

    def patch(self, request, pk, *args, **kwargs) -> Response:
        try:
            user = next(user for user in self.users_list if user['id'] == pk)
            user.update(request.data)
            FileAction.save_file(self.users_list)
            return Response(user, status.HTTP_206_PARTIAL_CONTENT)
        except StopIteration:
            return Response('Not Found', status.HTTP_404_NOT_FOUND)

    def put(self, *args, **kwargs) -> Response:
        pk: int = kwargs.get('pk')
        data: Dict[str, Any] = self.request.data
        try:
            user_id: int = next(index for index, user in enumerate(self.users_list) if pk == user['id'])
            self.users_list[user_id].update({"name": data['name'], "age": data['age']})
        except (StopIteration, KeyError, IndexError):
            return Response('Not Found', status.HTTP_404_NOT_FOUND)

        FileAction.save_file(self.users_list)
        return Response(self.users_list[user_id], status.HTTP_206_PARTIAL_CONTENT)

    def delete(self, *args, **kwargs) -> Response:
        pk: int = kwargs.get('pk')
        try:
            result: Dict[str, Union[int, str]] = next(user for user in self.users_list if pk == user['id'])
            self.users_list.remove(result)
        except (StopIteration, ValueError):
            return Response('Not found', status.HTTP_404_NOT_FOUND)

        FileAction.save_file(self.users_list)
        return Response('Deleted', status.HTTP_204_NO_CONTENT)
