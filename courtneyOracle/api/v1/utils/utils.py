#Add all preprocessing and utility functions here.
"""Simple Reader that reads transcript of youtube video. Mycode: backend Code"""
import re
from typing import Any, List, Optional
from youtube_transcript_api import YouTubeTranscriptApi

from langchain import OpenAI
from llama_index import SimpleDirectoryReader, GPTVectorStoreIndex, PromptHelper
from llama_index import LLMPredictor, ServiceContext
import sys
#from google.colab import drive
import os


class YoutubeTranscriptReader():
  def __init__(self,yt_link:List[str]):
    self.yt_link = yt_link

  def _extract_video_id(self,yt_link):
    #patterns to check validity of urls
    patterns = [r'^https?://(?:www\.)?youtube\.com/watch\?v=([\w-]+)',
                    r'^https?://(?:www\.)?youtube\.com/embed/([\w-]+)',
                    r'^https?://youtu\.be/([\w-]+)',]

    for pattern in patterns:
            match = re.search(pattern, yt_link)
            if match:
                return match.group(1)

    #Option to get also the timing of the video:
    """
    [
    {
        'text': 'Hey there',
        'start': 7.58,
        'duration': 6.13
    },
    {
        'text': 'how are you',
        'start': 14.08,
        'duration': 7.58
    },
    # ...
    ]
    """
    return None #in case no match is found

  ##
  def load_data(self,ytlinks:str,languages: Optional[List[str]] = ["en"],**load_kwargs: Any):
        """Load data from the input directory.
        Args:
            pages (List[str]): List of youtube links \
                for which transcripts are to be read.
        """

        #Results for single url
        for link in ytlinks:
            video_id = self._extract_video_id(link)
            srt = YouTubeTranscriptApi.get_transcript(video_id, languages=languages)
            transcript = ""
            for chunk in srt:
                transcript = transcript + chunk["text"]
            #results.append(transcript)
        return transcript

#Finish Backend code here.
#how to call the code from here?
"""
if __name__ == "__main__":
    video_id = ["https://www.youtube.com/watch?v=V264u5kFOTo"]

    print (YoutubeTranscriptReader(video_id).yt_link)
    current_Transcript_software = YoutubeTranscriptReader(video_id)

    #instantiate the class and call the member function:
    documents = current_Transcript_software.load_data(video_id)

    #Check the code to delive
"""


## Talking to Books

def construct_index(directory_path):
    # set maximum input size
    max_input_size = 4096
    # set number of output tokens
    num_outputs = 256
    # set maximum chunk overlap
    max_chunk_overlap = 20
    # set chunk size limit
    chunk_size_limit = 600

    prompt_helper = PromptHelper(max_input_size, num_outputs, max_chunk_overlap, chunk_size_limit=chunk_size_limit)

    # define LLM
    llm_predictor = LLMPredictor(llm=OpenAI(temperature=0, model_name="text-davinci-002", max_tokens=num_outputs))

    documents = SimpleDirectoryReader(directory_path).load_data()

    service_context = ServiceContext.from_defaults(llm_predictor=llm_predictor)
    index = GPTVectorStoreIndex.from_documents(documents, service_context=service_context)

    index.save_to_disk('index.json')
    return index

def ask_bot(input_index = 'index.json'):
  index = GPTVectorStoreIndex.load_from_disk(input_index)
  while True:
    query = input('What do you want to ask the bot?   \n')
    response = index.query(query, response_mode="compact")
    return response.response