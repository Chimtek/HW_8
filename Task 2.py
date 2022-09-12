import requests


def get_token():
    with open('Task_2_token.txt', 'r') as fl:
        return fl.readline()


class YaUploader:
    files_url = f"https://cloud-api.yandex.net/v1/disk/resources/files"
    upload_url = f"https://cloud-api.yandex.net/v1/disk/resources/upload"

    def __init__(self, token: str):
        self.token = token
        self.header = {'Content-Type': 'application/json',
                   'Accept': 'application/json',
                   'Authorization': f'OAuth {self.token}'}

    def get_upload_link(self, file_path: str):
        """Метод возвращает ссылку для загрузки файла на яндекс диск"""
        params = {'path': file_path, 'overwrite': True}
        response = requests.get(self.upload_url, params=params, headers=self.header)

        if response.status_code != 200:
            print(f'Ошибка: {response.status_code}')

        href = response.json().get('href')
        if not href:
            print('Ссылка не получена', response.status_code)
        return href

    def upload(self, file_path):
        """Метод загружает файлы по списку file_list на яндекс диск"""
        href = self.get_upload_link(file_path)
        with open(file_path, 'rb') as file:
            response = requests.put(href, file)

        if response.status_code == 201:
            print(f'Файл {file_path} успешно загружен')
        else:
            print("Файл загрузить не удалось.", response.status_code)


if __name__ == '__main__':
    # Получить путь к загружаемому файлу и токен от пользователя
    path_to_file = r'result.txt'
    token = get_token()
    uploader = YaUploader(token)
    uploader.upload(path_to_file)
