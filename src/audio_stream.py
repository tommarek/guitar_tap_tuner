#!/usr/bin/env python3

import pyaudio


class AudioStream:
    """

    """
    audio = pyaudio.PyAudio()

    def __init__(self, device=None, rate=None, chunksize=1024):
        self.device = device or self.get_device()
        self.rate = rate
        self.buffer = None
        self.chunksize = chunksize

        self.new_data = False
        self.started = False

        self.stram = self.audio.open(
            format=pyaudio.paInt16,
            channels=1,
            input_device_index=mic_id,
            frames_per_buffer=1024,
            rate=self.rate or mic_info['defaultSampleRate'],
            input=True,
            stream_callback=self.stream_callback)
        )

    def stream_callback(self, data, frame_count, time_info, status):
        if self.started:
            self.buffer.append_data(np.frombuffer(data, dtype=np.int16))
            self.new_data = True

        return (data, pyaudio.paContinue)

    def start_stream(self, )

    def test_mic(self, mic_id):
        """
        test if mic_id is a valid microphone
        """
        try:
            mic_info = self.audio.get_device_info_by_index(mic_id)
            if mic_info['maxInputChannels'] < 1:
                return False

            stream = self.audio.open(
                format=pyaudio.paInt16,
                channels=1,
                input_device_index=mic_id,
                frames_per_buffer=1024,
                rate=self.rate or mic_info['defaultSampleRate'],
                input=True,
            )
            stream.close()
            return True
        except Exception as e:
            return False

    def get_device(self):
        """
        Get available input devices and select the first one if available
        """
        available_mic_ids = [mic_id for mic_id in range(self.audio.get_device_count()) if test_mic(mic_id)]

        if available_mic_ids:
            for mic_id in available_mic_ids:
                mic_info = self.audio.get_device_info_by_index(mic_id)
                print(f'MICROPHONE{mic_id} = {str(mic_info)}')
            return available_mic_ids[0]

        return None
