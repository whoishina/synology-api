from __future__ import annotations
from typing import Optional
from . import base_api


class AdminConsole(base_api.BaseApi):

    def status_info(self) -> dict[str, object] | str:
        api_name = 'SYNO.SynologyDrive'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'get_status'}

        return self.request_data(api_name, api_path, req_param)

    def config_info(self) -> dict[str, object] | str:
        api_name = 'SYNO.SynologyDrive.Config'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'get'}

        return self.request_data(api_name, api_path, req_param)

    def connections(self) -> dict[str, object] | str:
        api_name = 'SYNO.SynologyDrive.Connection'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'summary'}

        return self.request_data(api_name, api_path, req_param)

    def drive_check_user(self) -> dict[str, object] | str:
        api_name = 'SYNO.SynologyDrive'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'check_user'}

        return self.request_data(api_name, api_path, req_param)

    def active_connections(self) -> dict[str, object] | str:
        api_name = 'SYNO.SynologyDrive.Connection'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'list'}

        return self.request_data(api_name, api_path, req_param)

    def active_sync_connections(self) -> dict[str, object] | str:
        api_name = 'SYNO.SynologyDriveShareSync.Connection'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'list'}

        return self.request_data(api_name, api_path, req_param)

    def share_active_list(self) -> dict[str, object] | str:
        api_name = 'SYNO.SynologyDrive.Share'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'list_active'}

        return self.request_data(api_name, api_path, req_param)

    def log(self,
            share_type: str = 'all',
            get_all: bool = False,
            limit: int = 1000,
            keyword: str = '',
            date_from: int = 0,
            date_to: int = 0,
            username: str = '',
            target: str = 'user'
            ) -> dict[str, object] | str:
        api_name = 'SYNO.SynologyDrive.Log'
        info = self.gen_list[api_name]
        api_path = info['path']

        if get_all:
            get_all = 'true'
        elif not get_all:
            get_all = 'false'
        else:
            return 'get_all must be True or False'

        req_param = {'version': info['maxVersion'], 'method': 'list', 'share_type': share_type, 'get_all': get_all,
                     'limit': limit, 'keyword': keyword, 'datefrom': date_from, 'dateto': date_to, 'username': username,
                     'target': target}

        return self.request_data(api_name, api_path, req_param)

    def c2fs_share(self) -> dict[str, object] | str:
        api_name = 'SYNO.C2FS.Share'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'list'}

        return self.request_data(api_name, api_path, req_param)

    def settings(self) -> dict[str, object] | str:
        api_name = 'SYNO.SynologyDrive.Settings'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'list'}

        return self.request_data(api_name, api_path, req_param)

    def db_usage(self) -> dict[str, object] | str:
        api_name = 'SYNO.SynologyDrive.DBUsage'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'get'}

        return self.request_data(api_name, api_path, req_param)

    def delete_status(self) -> dict[str, object] | str:
        api_name = 'SYNO.SynologyDrive.Node.Delete'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'status'}

        return self.request_data(api_name, api_path, req_param)

    def file_property_transfer_status(self) -> dict[str, object] | str:
        api_name = 'SYNO.SynologyDrive.Migration.UserHome'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'status'}

        return self.request_data(api_name, api_path, req_param)

    def user_sync_profile(self, user: str = '', start: int = 0, limit: str | int = 'null') -> dict[str, object] | str:
        api_name = 'SYNO.SynologyDrive.Profiles'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'list', 'start': start, 'limit': limit, 'user': user}

        return self.request_data(api_name, api_path, req_param)

    def index_pause(self, time_pause: int = 60) -> dict[str, object] | str:
        api_name = 'SYNO.SynologyDrive.Index'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'set_native_client_index_pause',
                     'pause_duration': time_pause}

        return self.request_data(api_name, api_path, req_param)

class DriveShareSync(base_api.BaseApi):
    def active_sync_connections(self) -> dict[str, object] | str:
        """
        Get the list of active sync connections
        """
        api_name = 'SYNO.SynologyDriveShareSync.Connection'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'list'}
        return self.request_data(api_name, api_path, req_param)

    def get_session_config(self, session_id: str):
        api_name = 'SYNO.SynologyDriveShareSync.Session'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'get', 'sess_id': session_id}
        return self.request_data(api_name, api_path, req_param)

    def update_filter_paths(self, session_id: int, paths: list[str], mode: str = 'add') -> dict[str, object] | str:
        """
        Update the filter paths for a given session.
        :param session_id: The session ID
        :param paths: The paths to add or remove from the filter
        :param mode: The mode to use (add or remove)
        :return: The response from the API
        """
        api_name = 'SYNO.SynologyDriveShareSync.Session'
        filter = self.get_session_config(session_id)['data']
        if filter is None:
            return 'Session not found'

        # update filter paths
        if mode == 'add':
            filter['filtered_paths'] = filter['filtered_paths'] + paths
        elif mode == 'remove':
            filter['filtered_paths'] = [x for x in filter['filtered_paths'] if x not in paths]
        else:
            return 'Invalid mode or path not found in filtered paths'

        # unique paths
        filter['filtered_paths'] = list(set(filter['filtered_paths']))
        info = self.gen_list[api_name]
        update_filter_path_param = {
            'version': info['maxVersion'],
            'method': 'set',
            'api': 'SYNO.SynologyDriveShareSync.Session',
            'sess_list': [
                {
                    'sess_id': session_id,
                    'filtered_max_upload_size': filter['filtered_max_upload_size'],
                    'filtered_extensions': filter['filtered_extensions'],
                    'filtered_names': filter['filtered_names'],
                    'user_defined_extensions': filter['user_defined_extensions'],
                    'user_defined_names': filter['user_defined_names'],
                    'filtered_paths': filter['filtered_paths'],
                    'enable_file_filter': True
                    }
                ]
            }
        # return req_param
        compound_data = [update_filter_path_param]
        return self.batch_request(compound_data, method='post')
