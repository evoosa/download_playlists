import os.path

from consts import PLAYLISTS, BASE_DIR, SPOTIFY_BASE_URL
import glob
from datetime import datetime
import shutil

current_date = datetime.now()


class PlaylistDownloader:
    def __init__(self):
        # create the base output directory
        self.base_output_dir = os.path.join(BASE_DIR, f"new_music_{current_date.strftime('%d_%m_%Y')}")
        if not os.path.exists(self.base_output_dir):
            os.makedirs(self.base_output_dir)
        pass

    def download_playlist_diff(self, playlist_key):
        """ download new songs added to the given playlist """
        output_dir = os.path.join(self.base_output_dir, playlist_key)
        filenames = self._get_filenames(PLAYLISTS[playlist_key]['search_pattern'])
        # create empty files
        # download diff songs

    @staticmethod
    def _get_filenames(glob_pattern):
        filenames = []
        for filepath in glob.glob(glob_pattern):
            filenames.append(os.path.basename(filepath))
        return filenames

    @staticmethod
    def _create_empty_files(filenames, output_dir):
        for filename in filenames:
            output_file_path = os.path.join(output_dir, filename)
            with open(output_file_path, 'w'):
                pass

    def backup_playlists_to_external_drive(self, drive_letter):
        """ backup the downloaded playlists to the given external drive """
        pass
