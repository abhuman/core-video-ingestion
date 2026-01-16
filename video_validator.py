import subprocess
from core.validators.validator import Validator
from core.domain.errors import VideoValidationError

class VideoValidator(Validator):
    def validate(self, video_path):
        try:
            video_codec = subprocess.check_output([
                "ffprobe","-v","error",
                "-select_streams","v:0",
                "-show_entries","stream=codec_name",
                "-of","default=nk=1:nw=1",
                video_path
            ]).decode().strip()

            audio_codec = subprocess.check_output([
                "ffprobe","-v","error",
                "-select_streams","a:0",
                "-show_entries","stream=codec_name",
                "-of","default=nk=1:nw=1",
                video_path
            ]).decode().strip()

            if video_codec != "h264" or audio_codec != "aac":
                raise VideoValidationError("Codec policy violation")

        except Exception:
            raise VideoValidationError("Video validation failed")
