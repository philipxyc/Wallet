import multiprocessing, queue
import azure.cognitiveservices.speech as speechsdk

def start_node(task_queue, objdetect_tasks, objdetect_results, nav_tasks, nav_results)
	speech_key, service_region = "b1b54e5bcd8943f0b8106e000e1298d7", "eastasia"
	speech_config = speechsdk.SpeechConfig(subscription=speech_key, region=service_region)

	# Creates a recognizer with the given settings
	speech_recognizer = speechsdk.SpeechRecognizer(speech_config=speech_config)
	
	while True:
		try:
			task = task_queue.get_nowait()
			if task is None:
				break
		except queue.Empty:
			pass

		# Creates an instance of a speech config with specified subscription key and service region.
		# Replace with your own subscription key and service region (e.g., "westus").

		print("Say something...")

		# Starts speech recognition, and returns after a single utterance is recognized. The end of a
		# single utterance is determined by listening for silence at the end or until a maximum of 15
		# seconds of audio is processed.  The task returns the recognition text as result. 
		# Note: Since recognize_once() returns only a single utterance, it is suitable only for single
		# shot recognition like command or query. 
		# For long-running multi-utterance recognition, use start_continuous_recognition() instead.
		result = speech_recognizer.recognize_once()

		# Checks result.
		if result.reason == speechsdk.ResultReason.RecognizedSpeech:
		    print("Recognized: {}".format(result.text))
		elif result.reason == speechsdk.ResultReason.NoMatch:
		    print("No speech could be recognized: {}".format(result.no_match_details))
		elif result.reason == speechsdk.ResultReason.Canceled:
		    cancellation_details = result.cancellation_details
		    print("Speech Recognition canceled: {}".format(cancellation_details.reason))
		    if cancellation_details.reason == speechsdk.CancellationReason.Error:
		        print("Error details: {}".format(cancellation_details.error_details))
